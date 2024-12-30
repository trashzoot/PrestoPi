def urlencode(params):
    encoded = []
    for key, value in params.items():
        encoded.append(f"{key}={quote(str(value))}")
    return "&".join(encoded)

def quote(string):
    safe = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
    result = ""
    for char in string:
        if char in safe:
            result += char
        else:
            result += f"%{ord(char):02X}"
    return result