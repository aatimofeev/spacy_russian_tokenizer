from lxml import html

from spacy.tokens import Doc
from spacy.gold import GoldParse

from spacy_russian_tokenizer.src.hyphen_patterns import FOREIGN_SURNAME_PATTERNS, PRONOUN_PATTERNS, PARTICLE_PATTERNS, \
    ADVERB_PATTERNS, COMPOUND_PREPOSITION_PATTERNS, PROPER_NAMES_WITH_DIGITS_PATTERNS, \
    COMPOUND_WORDS_WITH_DIGIT_PATTERNS, GEOGRAPHIC_NAMES_PATTERNS, ORG_NAMES_PATTERNS, CONJUNCT_WORDS_PATTERNS, \
    DIRECTION_PATTERNS, MISC_HYPHEN_FORM_PATTERNS, LOANWORDS_PATTERNS, SYNTAGRUS_RARE_CASES, COMPOUND_NOUNS, \
    COMPOUND_ADJECTIVE_PATTERNS
from spacy_russian_tokenizer.src.bigram_patterns import PERCENTAGE_PATTERNS
from spacy_russian_tokenizer.pipeline import pipeline
from spacy_russian_tokenizer.evaluation.evaluation_utils import find_unaligned_sentences, find_problem_tokens


def extract_docs_and_golds_from_opencorpora(nlp, opencorpora_file):
    parsed_sentences = []
    gold_sentences = []

    with open(opencorpora_file, "r") as f:
        opencorpora = f.read().encode('utf-8')

    page_tree = html.fromstring(opencorpora)

    for text in page_tree.xpath('//text'):
        for paragraphs in text.xpath('./paragraphs'):
            for paragraph in paragraphs.xpath('./paragraph'):
                for sentence in paragraph.xpath('./sentence'):
                    text = sentence.xpath('./source')[0].text
                    parsed_sentences.append(nlp(text))
                    sent_words = [token.attrib['text'] for token in sentence.xpath('./tokens/token')]
                    gold = GoldParse(Doc(nlp.vocab, words=sent_words), words=sent_words,  # heads=sent_heads,
                                     # tags=sent_tags, deps=sent_deps,
                                     entities=['-'] * len(sent_words))
                    gold_sentences.append(gold)
    return parsed_sentences, gold_sentences


opencorpora_file = '/home/user/Downloads/annot.opcorpora.no_ambig.xml'

RULES = FOREIGN_SURNAME_PATTERNS + PRONOUN_PATTERNS + PARTICLE_PATTERNS + ADVERB_PATTERNS + \
        COMPOUND_PREPOSITION_PATTERNS + PROPER_NAMES_WITH_DIGITS_PATTERNS + COMPOUND_WORDS_WITH_DIGIT_PATTERNS + \
        GEOGRAPHIC_NAMES_PATTERNS + ORG_NAMES_PATTERNS + CONJUNCT_WORDS_PATTERNS + DIRECTION_PATTERNS + \
        MISC_HYPHEN_FORM_PATTERNS + LOANWORDS_PATTERNS + SYNTAGRUS_RARE_CASES + COMPOUND_NOUNS + \
        COMPOUND_ADJECTIVE_PATTERNS + PERCENTAGE_PATTERNS
nlp = pipeline(RULES)

parsed_sentences, gold_sentences = extract_docs_and_golds_from_opencorpora(nlp, opencorpora_file)

unaligned = find_unaligned_sentences(parsed_sentences, gold_sentences)

print(len(unaligned) / len(gold_sentences))
# 0.08563324133701318


problem_tokens, wrong_tokenization_examples = find_problem_tokens(unaligned)
#
# # nlp.evaluate(zip(parsed_sentences, gold_sentences)).scores
#
[print(i[1]) for i in problem_tokens if i[1].find('-') > -1 and problem_tokens[i] > 0]
#
for id, example in enumerate(unaligned):
    if example[0][-1].text != '..':
        print(id, '\n', [i.text for i in example[0]], '\n', example[1].words)
