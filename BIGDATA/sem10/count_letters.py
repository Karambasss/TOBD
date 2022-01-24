#запихиваем весь код в отдельный файл
from collections import Counter

def count_letters(file):
    fp = open(file)
    text = fp.read().lower()
    fp.close()
    return Counter(text)
