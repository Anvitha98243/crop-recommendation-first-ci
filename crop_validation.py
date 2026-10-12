
REQUIRED_FEATURES = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall",
]


def validate_crop_input(data):
    for feature in REQUIRED_FEATURES:
        if feature not in data:
            return False

        try:
            value = float(data[feature])
        except (ValueError, TypeError):
            return False

        if value < 0:
            return False

    return False
