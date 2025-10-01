def str_to_bool(value):
    if isinstance(value, str):
        return value.lower() in ["true", "1", "si", "sí"]
    return bool(value)

        
def safe_int(value, default=None):
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return None 