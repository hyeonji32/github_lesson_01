def decimal_to_hexadecimal(decimal_num):
    """
    Convert decimal number to hexadecimal.
    """
    if decimal_num == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        decimal_num = decimal_num // 16
    return hexadecimal
                
