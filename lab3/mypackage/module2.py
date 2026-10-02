import re


def find_common_word_in_file(file_path: str) -> str | None:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    raw_sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in raw_sentences if s.strip()]

    if not sentences:
        return None

    common_words = None

    for sentence in sentences:

        words = set(re.findall(r"[а-яА-ЯёЁa-zA-Z]+(?:-[а-яА-ЯёЁa-zA-Z]+)?", sentence.lower()))

        if common_words is None:
            common_words = words
        else:
            common_words &= words

    if common_words:
        return next(iter(common_words))

    return None