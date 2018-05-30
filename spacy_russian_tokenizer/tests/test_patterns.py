import pytest
from spacy.util import get_lang_class
from spacy.matcher import Matcher

from spacy_russian_tokenizer.src.hyphen_patterns import FOREIGN_SURNAME_PATTERNS, PRONOUN_PATTERNS, PARTICLE_PATTERNS, \
    ADVERB_PATTERNS, COMPOUND_PREPOSITION_PATTERNS, PROPER_NAMES_WITH_DIGITS_PATTERNS, \
    COMPOUND_WORDS_WITH_DIGIT_PATTERNS, GEOGRAPHIC_NAMES_PATTERNS, ORG_NAMES_PATTERNS, CONJUNCT_WORDS_PATTERNS, \
    DIRECTION_PATTERNS, MISC_HYPHEN_FORM_PATTERNS, LOANWORDS_PATTERNS, SYNTAGRUS_RARE_CASES, COMPOUND_NOUNS, \
    COMPOUND_ADJECTIVE_PATTERNS
from spacy_russian_tokenizer.pipeline import pipeline


def test_foreign_surnames():
    nlp = pipeline(FOREIGN_SURNAME_PATTERNS)

    text = "Сан-Мартин, Сен-Симон, Сен-Жюст, Сент-Бёв, Мак-Магон, Мак-Кинли, аль-Кадир, Турсун-заде, Мамед-оглы, " \
           "Явер-кызы, Измаил-бей, Кемаль-паша, Мирза-хан, Ахмед-шах, Чингисхан"
    doc = nlp(text)

    assert [i.text for i in doc if not i.is_punct] == text.split(', ')


def test_pronouns():
    nlp = pipeline(PRONOUN_PATTERNS)
    text = "кто-либо, что-либо, какой-либо, чей-либо, когда-либо, где-либо, куда-либо, откуда-либо, кто-нибудь, " \
           "что-нибудь, какой-нибудь, чей-нибудь, когда-нибудь, где-нибудь, куда-нибудь, откуда-нибудь, как-нибудь, " \
           "сколько-нибудь, кто-то, что-то, какой-то, такой-то, чей-то, когда-то, тогда-то, где-то, там-то, куда-то, " \
           "туда-то, откуда-то, оттуда-то, как-то, так-то, сколько-то, столько-то"
    doc = nlp(text)
    assert [i.text for i in doc if not i.is_punct] == text.split(', ')


def test_particles():
    nlp = pipeline(PARTICLE_PATTERNS)
    text = "ничего-де, Ответь-ка, Вот-те, Чёрт-те, да-с, нет-с, довольно-таки, наконец-таки"
    doc = nlp(text)
    assert [i.text for i in doc if not i.is_punct] == text.split(', ')


def test_adverb_and_compound_prepositions():
    nlp = pipeline(COMPOUND_PREPOSITION_PATTERNS + ADVERB_PATTERNS)
    text = "во-первых, во-вторых, в-третьих, в-десятых, в-главных, в-последних, из-за, из-под, по-за, по-над, " \
           "по-под, с-под, для-ради, за-ради"
    doc = nlp(text)
    assert [i.text for i in doc if not i.is_punct] == text.split(', ')


def test_proper_names_with_digits():
    nlp = pipeline(PROPER_NAMES_WITH_DIGITS_PATTERNS)
    text = "МКБ-10 — Международная классификация болезней 10-го пересмотра."
    doc = nlp(text)
    assert doc[0].text == 'МКБ-10'


def test_compound_words_with_digits():
    nlp = pipeline(COMPOUND_WORDS_WITH_DIGIT_PATTERNS)
    text = "Лихие 90-е — журналистское клише, характеризующее период постсоветской России в 1990-х — 2000-х гг."
    doc = nlp(text)
    assert doc[1].text == '90-е'
    assert doc[11].text == '1990-х'


def test_geographic_names():
    nlp = pipeline(GEOGRAPHIC_NAMES_PATTERNS)
    text = "Усть-Абакан, Соль-Илецк, Верх-Ирмень, Ново-Вязники, Нижне-Гнилое, Австро-Венгрия, Эльзас-Лотарингия"
    doc = nlp(text)
    assert [i.text for i in doc if not i.is_punct] == text.split(', ')


def test_org_names():
    nlp = pipeline(ORG_NAMES_PATTERNS)
    text = "«Альфа-групп» контролирует почти все активы девелопера DVI Group, сообщили «Ведомостям» два " \
           "консультанта, работавших с ней."
    doc = nlp(text)
    assert doc[1].text == 'Альфа-групп'


def test_conjuct_words():
    nlp = pipeline(CONJUNCT_WORDS_PATTERNS)
    text = "Чемпионат мира 2018 в Ростове-на-Дону"
    doc = nlp(text)
    assert doc[-1].text == 'Ростове-на-Дону'


def test_directions():
    nlp = pipeline(DIRECTION_PATTERNS)
    text = "северо-запад, северо-восток, юго-запад, юго-восток"
    doc = nlp(text)
    assert [i.text for i in doc if not i.is_punct] == text.split(', ')


def test_loanwords():
    nlp = pipeline(LOANWORDS_PATTERNS)
    text = "обер-мастер, унтер-офицер, лейб-медик, штаб-квартира, вице-президент, экс-чемпион"
    doc = nlp(text)
    assert [i.text for i in doc if not i.is_punct] == text.split(', ')


def test_compound_words():
    nlp = pipeline(COMPOUND_NOUNS)
    text = "Социал-демократия — социальная политика и идейно-политическое течение"
    doc = nlp(text)
    assert doc[0].text == 'Социал-демократия'


def test_compound_adjectives():
    nlp = pipeline(COMPOUND_NOUNS + COMPOUND_ADJECTIVE_PATTERNS)
    text = "Социал-демократия — социальная политика и идейно-политическое течение"
    doc = nlp(text)
    # [i.text for i in doc]
    assert doc[0].text == 'Социал-демократия'
    assert doc[5].text == 'идейно-политическое'
