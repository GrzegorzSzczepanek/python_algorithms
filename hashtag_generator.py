def generate_hashtag(s):
    return False if len(s) < 1 or len(s) > 140 else  "#" + s.title().replace(" ", "")
