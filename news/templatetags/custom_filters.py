from django import template

register = template.Library()


def lower(text):
    if text[1:] != text[1:].lower():
        return False
    else:
        return True


def change_word(text):
    word = text[0]
    for i in text:
        if i.isalpha():
            word += '*'
        else:
            word += i
    return word


def censor1(string):
    if isinstance(string, str):
        text_split = string.split()
        new_line = []
        for word in text_split:
            if not lower(word):
                new_line.append(change_word(word))
            else:
                new_line.append(word)
    return ' '.join(new_line)


@register.filter()
def censor(value):
    return censor1(value)
