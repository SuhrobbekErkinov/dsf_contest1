def typeBasedTransformer(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            result[key] = value ** 2
        elif isinstance(value, str):
            result[key] = value[::-1]
        elif isinstance(value, bool):
            result[key] = not value
        elif isinstance(value, (list, tuple)):
            result[key] = value[::-1]
        elif isinstance(value, dict):
            result[key] = {v: k for k, v in value.items()}
        else:
            result[key] = value
    return result