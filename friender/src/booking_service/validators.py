from django.forms import ValidationError


def validate_yahoo_email(value) -> None:
    if "yahoo.com" not in value:
        raise ValidationError("Email must be a yahoo.com email address.")