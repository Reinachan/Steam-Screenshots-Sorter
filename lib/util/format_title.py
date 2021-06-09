import re


def format_title(title):
    formated_title = title

    if title.endswith("on Steam"):
        formated_title = title[:-9]

    formated_title = re.sub("^Save [0-9]{1,3}% on ", "", formated_title)

    if formated_title.isupper():
        formated_title = formated_title.title()

    return formated_title
