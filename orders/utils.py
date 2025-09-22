from .models immport Coupon

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    :param length: Length of the coupon code(default = 10)
    :return: Unique coupon code string
    """
    alphabet = string.ascii_uppercase + string.digits

    while True:
        code = ''.join(secrets.choice(alphabet) for _in range(length))
        # Ensure uniqueness in DB
        if not Coupon.objects.filter(code=code).exists():
            return code


            