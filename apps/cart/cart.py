from apps.product.models import ProductCustom
from .models import Cart, CartItem
from django.http import Http404


CART_SESSION_ID = 'cart'  # Save 'cart' in variable


class SessionCart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)  # Get user cart from sessions

        # Check if 'cart' is not exists
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart  # Set current user cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            product = ProductCustom.objects.get(idkc=item['idkc'])  # Get current product with idkc

            item['product'] = product
            item['total_price'] = int(product.selling_price * item['quantity'])  # Save total price
            yield item

    def total_price(self):
        cart = self.cart.copy()
        total_price = 0

        for item in cart.values():
            product = ProductCustom.objects.get(idkc=item['idkc'])  # Get each product
            price = int(product.selling_price * item['quantity'])  # Save item price(for all quantities)
            total_price += price

        return total_price

    def base_total_price(self):
        cart = self.cart.copy()
        base_total_price = 0

        for item in cart.values():
            product = ProductCustom.objects.get(idkc=item['idkc'])  # Get each product
            price = int(product.base_price * item['quantity'])  # Save item price(for all quantities)
            base_total_price += price

        return base_total_price

    def cart_add(self, idkc, quantity=0):
        product = ProductCustom.objects.get(idkc=idkc)  # Get current product

        if product.quantity > 1:

            # Add new product to cart
            if idkc not in self.cart:
                self.cart[idkc] = {
                    'idk': product.product.idk,
                    'idkc': product.idkc,
                    'quantity': 0,
                }

        if product.quantity > self.cart[idkc]['quantity']:
            self.cart[idkc]['quantity'] += int(quantity)  # Add extra quantity

        if self.cart[idkc]['quantity'] < 1:
            self.cart[idkc]['quantity'] = 1  # Fix to 1

        self.save()

    def cart_remove(self, idkc):
        if idkc in self.cart:
            del self.cart[idkc]  # Del item if exists

        self.save()  # Save cart

    def cart_delete(self):
        try:
            del self.session[CART_SESSION_ID]
        except self.session.DoesNotExists:
            self.save()

    def save(self):
        self.session.modified = True  # Set session modified as True to allow changes


# ModelCart
class ModelCart:
    def __init__(self, request):
        self.user = request.user  # Get user with request

        try:
            cart = Cart.objects.get(user=self.user)  # Get user ModelCart
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=self.user)  # Create Cart if not exists

        self.cart = cart  # Save in self.cart

    def __iter__(self):
        items = CartItem.objects.filter(cart=self.cart)  # Get all Cart items

        for item in items:
            item.total_price = int(item.quantity * item.product.selling_price)  # Calculate total price of this Item
            item.base_total_price = int(item.quantity * item.product.base_price)  # Calculate base total price of this Item
            item.save()
            yield item  # Iterate one by one

    def total_price(self):
        items = CartItem.objects.filter(cart=self.cart)
        total_price = 0

        for item in items:
            total_price += item.total_price

        # Save the cart total price
        self.cart.total_price = total_price
        self.cart.save()

        return total_price

    def base_total_price(self):
        items = CartItem.objects.filter(cart=self.cart)
        base_total_price = 0

        for item in items:
            base_total_price += item.base_total_price

        return base_total_price

    def cart_add(self, idkc, quantity=0):
        try:
            product = ProductCustom.objects.get(idkc=idkc)  # Get current product
        except ProductCustom.DoesNotExist:
            raise Http404

        try:
            cart_item = CartItem.objects.get(product=product, cart=self.cart)  # Just get the CartItem if exists
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(product=product, cart=self.cart)  # Create Item in CartItem for current Cart

        cart_item.idkc = product.idkc  # Save ProductCustom idkc

        if product.quantity > cart_item.quantity:
            cart_item.quantity += quantity  # Add or minus extra quantity

        if cart_item.quantity < 1:
            cart_item.quantity = 1  # Fix to 1 quantity

        cart_item.total_price = int(cart_item.quantity * cart_item.product.selling_price)  # Calculate total price of this Item
        cart_item.base_total_price = int(cart_item.quantity * cart_item.product.base_price)  # Calculate base total price of this Item
        cart_item.save()  # Save the CartItem

        self.total_price()

    def cart_remove(self, idkc):
        product = ProductCustom.objects.get(idkc=idkc)  # Get current product

        if CartItem.objects.filter(product=product, cart=self.cart).exists():
            CartItem.objects.get(product=product, cart=self.cart).delete()  # Remove CartItem from database if exists

    def cart_delete(self):
        try:
            Cart.objects.get(user=self.user).delete()
        except Cart.DoesNotExist:
            return None

    def cart_merge(self, request):
        session_cart = request.session.get(CART_SESSION_ID)

        if session_cart:
            for item in session_cart.values():
                # Check if Item is not in ModelCart then add it
                if not CartItem.objects.filter(cart=self.cart, product__idkc=item['idkc']).exists():
                    product = ProductCustom.objects.get(idkc=item['idkc'])  # Get current product from database
                    CartItem.objects.create(cart=self.cart, product=product, idkc=product.idkc, quantity=item['quantity'], total_price=int(item['quantity']*product.selling_price)).save()  # Create new item inside ModelCart

            del request.session[CART_SESSION_ID]
