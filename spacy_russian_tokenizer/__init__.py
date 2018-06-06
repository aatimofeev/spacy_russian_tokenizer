from spacy.matcher import Matcher
from spacy.util import get_lang_class

from spacy_russian_tokenizer.patterns import MERGE_PATTERNS, SYNTAGRUS_RARE_CASES, NO_TERMINAL_PATTERNS
from spacy_russian_tokenizer.patterns.sentence_segmentation import detect_sentence_boundaries
from spacy_russian_tokenizer.patterns.tokenizer_exceptions import SPECIAL_CASES, DOT_SPECIAL_CASES


class RussianTokenizer(object):
    name = 'russian_tokenizer'

    def __init__(self, nlp, merge_patterns=None, terminal_patterns=None):
        self.matcher = Matcher(nlp.vocab)
        self.token_merge = nlp.vocab.strings['pattern']
        self.sentence_terminal = nlp.vocab.strings['sentence_terminal']
        if merge_patterns:
            self.matcher.add(self.token_merge, None, *merge_patterns)
        if terminal_patterns:
            self.matcher.add(self.sentence_terminal, None, *terminal_patterns)

    def __call__(self, doc):
        spans = []
        for id, start, end in self.matcher(doc):
            if id == self.token_merge:
                spans.append(doc[start:end])
            elif id == self.sentence_terminal:
                # remove all sentence start marks from span that match pattern
                for token in doc[start:end]:
                    if token.sent_start:
                        token.sent_start = False
        if spans:
            for span in spans:
                span.merge()
        return doc


def pipeline(merge_patterns=None, terminal_patterns=None):
    CYRILLIC_UPPER = r'[\p{Lu}&&\p{Cyrillic}]'
    r'(?<=[{au}])\.(?=\w+)'.format(au=CYRILLIC_UPPER)

    Language = get_lang_class('ru')
    Language.Defaults.infixes += ('«»',)
    Language.Defaults.infixes += ('-',)
    Language.Defaults.infixes += ('"\/',)
    Language.Defaults.infixes += ('/',)
    Language.Defaults.infixes += (r'(?<=[{au}])\.(?=\w+)'.format(au=CYRILLIC_UPPER),)

    # Token.set_extension('is_adjective', default=False, force=True)
    nlp = Language()
    russian_tokenizer = RussianTokenizer(nlp, merge_patterns=merge_patterns, terminal_patterns=terminal_patterns)

    nlp.add_pipe(detect_sentence_boundaries, name='detect_sentence_boundaries', first=True)
    # nlp.add_pipe(match_adjective, name='match_adjective', after='detect_sentence_boundaries')
    nlp.add_pipe(russian_tokenizer, name='russian_tokenizer', after='detect_sentence_boundaries')

    for case in SPECIAL_CASES:
        nlp.tokenizer.add_special_case(case, [{'ORTH': case}])

    for case in DOT_SPECIAL_CASES:
        nlp.tokenizer.add_special_case(case, [{'ORTH': case}])

    nlp.tokenizer.add_special_case('--', [{'ORTH': '—'}])
    nlp.tokenizer.add_special_case('  ', [{'ORTH': ' '}])

    return nlp
