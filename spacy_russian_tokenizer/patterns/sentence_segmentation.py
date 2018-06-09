SENTENCE_TERMINAL_CHARS = '.!?\u203C\u203D\u2047\u2048\u2049\u3002\uFE52\uFE57\uFF01\uFF0E\uFF1F\uFF61\u2026\r\t'
SENTENCE_TERMINAL_NGRAMS = ['...', '!!!', '?!!', '?1', '?..', '..']

SENTENCE_TERMINALS = [i for i in SENTENCE_TERMINAL_CHARS] + SENTENCE_TERMINAL_NGRAMS


def detect_sentence_boundaries(doc):
    for i, token in enumerate(doc[:-2]):
        if token.text == '\n\n':
            doc[i + 1].sent_start = True
        elif token.text in SENTENCE_TERMINALS:
            # define sentence start if known sentence terminal and title case token or digit after
            if doc[i + 1].is_title or doc[i + 1].is_upper or doc[i + 1].is_digit or doc[i + 1].text in {'"'}:
                doc[i + 1].sent_start = True
        elif token.text == '\n':
            # define sentence start if known sentence terminal before line break and title case token or digit after
            if doc[i - 1].text in SENTENCE_TERMINALS and (doc[i + 1].is_title or doc[i + 1].is_digit):
                doc[i + 1].sent_start = True
        elif token.text == '-':
            # define sentence start if known sentence terminal before line break and title case token or digit after
            if doc[i - 1].text in SENTENCE_TERMINALS and (doc[i + 1].is_title or doc[i + 1].is_digit):
                doc[i].sent_start = True

    else:
        # if no sentence boundaries were found - make entire document a single sentence
        doc[0].sent_start = True
    return doc
