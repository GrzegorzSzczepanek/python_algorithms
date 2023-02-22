from collections import Counter
import re

def top_3_words(text):
    words = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in words.most_common(3)]
