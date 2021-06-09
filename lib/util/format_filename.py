def format_filename(string):
    x, y = '<>:"//\|?*', "()-`______"

    trans_table = string.maketrans(x, y)
    return string.translate(trans_table)
