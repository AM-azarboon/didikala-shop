from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


# Arithmetic numbers only
def arithmetic_numbers(value):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for num in value:
        if num not in numbers:
            error = _("Invalid input")
            raise ValidationError(error, code="INVALID_INPUT")


# Check mobile number format(Iran)
def mobile_format_check(string):
    mobile_regex = "^09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}$"
    if re.search(mobile_regex, string):
        return True

    return False


# Check email format
def email_format_check(string):
    try:
        validate_email(string)
        return True
    except ValidationError:
        return False
