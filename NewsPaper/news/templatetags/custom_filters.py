from django import template

register = template.Library()

@register.filter()
def censor(text):
    stop_words = ('bad', 'boring')

    for word in text.split():
        if word.lower() in stop_words:
            text = text.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return text