def remove_char_at(str, n):
    if n >= 0:
        new_string = str[:n] + str[n + 1:]
        return (new_string)
    else:
        return (str)
