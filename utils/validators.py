def validate_name(name):

    if not name.strip():
        raise ValueError("Name cannot be empty")

    return name.strip()


def validate_password(password):

    if len(password) < 4:
        raise ValueError("Password must contain at least 4 characters")

    return password


def validate_amount(amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    return amount