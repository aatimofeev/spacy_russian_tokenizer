from spacy.lang.ru import Russian
from spacy.matcher import Matcher
from spacy.pipeline import Sentencizer

from spacy_russian_tokenizer.patterns import MERGE_PATTERNS, SYNTAGRUS_RARE_CASES, NO_TERMINAL_PATTERNS
from spacy_russian_tokenizer.patterns.sentence_segmentation import detect_sentence_boundaries
from spacy_russian_tokenizer.patterns.tokenizer_exceptions import SPECIAL_CASES, DOT_SPECIAL_CASES


class RussianTokenizer:
    name = 'russian_tokenizer'

    def __init__(self, nlp, merge_patterns=None):
        self.matcher = Matcher(nlp.vocab)
        self.token_merge = nlp.vocab.strings['pattern']

        if merge_patterns:
            self.matcher.add(self.token_merge, None, *merge_patterns)

    def __call__(self, doc):
        matches = self.matcher(doc)
        if matches:
            spans = self.merge_spans(init_spans=matches)
            with doc.retokenize() as retokenizer:
                if matches:
                    for span in spans:
                        try:
                            retokenizer.merge(doc[span[1]:span[2]])
                        except ValueError:
                            continue
        return doc

    @staticmethod
    def merge_spans(init_spans):
        merged_spans = []

        labels = set([i[0] for i in init_spans])

        for label in labels:

            span_intervals = [[i[1], i[2]] for i in init_spans if i[0] == label]

            span_intervals.sort(key=lambda x: x[0])
            merged = [span_intervals[0]]
            for current in span_intervals:
                previous = merged[-1]
                if current[0] <= previous[1]:
                    previous[1] = max(previous[1], current[1])
                else:
                    merged.append(current)

            merged_spans += [(label, i[0], i[1]) for i in merged]

        return merged_spans


def pipeline(merge_patterns=MERGE_PATTERNS):
    nlp = Russian()

    russian_tokenizer = RussianTokenizer(nlp, merge_patterns=merge_patterns)

    sentencizer = Sentencizer(punct_chars=['\u2026'])
    nlp.add_pipe(sentencizer, name='sentencizer', first=True)
    nlp.add_pipe(russian_tokenizer, name='russian_tokenizer', last=True)

    return nlp
