import re

from spacy.tokens import Token
from spacy.matcher import Matcher

from spacy.util import get_lang_class

HYPHEN_SPICIAL_CASES = ['Сент-Женевьев-де-Буа', 'Гран-при', 'перпетуум-мобиле', 'давным-давно', 'па-де-труа',
                        'вот-вот', 'ГУ-ВШЭ', 'постольку-поскольку', 'туда-сюда', 'Та-да-дам', 'Точь-в-точь',
                        'та-да-дам', 'точь-в-точь', 'а-ля', 'йо-йо', 'кВт-ч', 'ТНК-BP', 'Н-да', 'ток-шоу', 'ИТАР-ТАСС',
                        'чуть-чуть', 'Чуть-чуть', 'ноу-хау', 'де-факто', 'тайм-аут', 'только-только', 'всего-навсего',
                        'плей-офф',
                        'просто-напросто', 'еле-еле', 'Солт-Лейк-Сити', 'Coca-Cola', 'on-line', 'ва-банк', 'тьфу-тьфу',
                        'крест-накрест', 'волей-неволей', 'self-made', 'Тянь-Шань', 'ски', 'Ей-богу', 'ей-богу',
                        'папье-маше', 'Тимофеева-Ресовского', 'Тимофеев-Ресовский', 'Рабин-Пелозофф',
                        'экса-электрон-вольт',
                        'онлайн', "наконец-то",
                        'трам-пам-пам',

                        'мно-ой', 'Петропавловска-Камчатского', 'Римских-Корсаковых', 'экса-электрон-вольт', '10^-24']

DOT_SPECIAL_CASES = ['е.',
                     # 'г.',
                     'см.',
                     'гг.',
                     '.',
                     'См.',
                     'им.',
                     'англ.',
                     'т.',
                     'др.',
                     'рис.',
                     'руб.',
                     'им.',
                     # 'тыс.',
                     # 'млн.',
                     'к.п.н.',
                     'др.',
                     'Дж.',
                     'кв.',
                     'пр.',
                     # 'млрд.',
                     'стр.',
                     'проц.']


# EXCLUSIONS = ['очень-то']


def adjective_ending(text):
    return bool(re.compile(r'^[а-яА-Я]{2,}(но|ко|во)$').match(text))


def match_adjective(doc):
    for token in doc:
        if token.is_alpha:
            if not token.is_ascii:
                if adjective_ending(token.text):
                    token._.is_adjective = True
    return doc


def pipeline(pattern):
    def rules_matcher(doc):
        spans = []
        for id, start, end in matcher(doc):
            spans.append(doc[start:end])
        if spans:
            for span in spans:
                # try:
                #     if span.text not in EXCLUSIONS:
                #         span.merge()
                # except IndexError as error:
                #     # print(doc)
                #     # error occurs when there are more than one hyphen within span, basically it can be ignored
                span.merge()
        return doc

    Language = get_lang_class('ru')
    # Token.set_extension('is_adjective', default=False, force=True)
    nlp = Language()
    matcher = Matcher(nlp.vocab)
    matcher.add('pattern', None, *pattern)
    # nlp.add_pipe(match_adjective, name='match_adjective', last=True)
    nlp.add_pipe(rules_matcher, name='rules_matcher', first=True)
    for case in HYPHEN_SPICIAL_CASES:
        nlp.tokenizer.add_special_case(case, [{'ORTH': case}])

    for case in DOT_SPECIAL_CASES:
        nlp.tokenizer.add_special_case(case, [{'ORTH': case}])
    return nlp
