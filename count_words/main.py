from collections import Counter
import re


def count_words(s):
    s = re.sub(r"[^a-zA-Z ']", "", s)
    words = s.lower().split(" ")
    return Counter(words)