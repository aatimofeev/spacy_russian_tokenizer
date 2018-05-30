FOREIGN_SURNAME_PATTERNS = [
    # prefixes, i.e Сен-Жермен, Мак-Кинли, Тер-Петросян
    [{'ORTH': "Сан"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Сен"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Сент"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Мак"}, {'ORTH': "-"}, {}],
    [{'LOWER': "аль"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Тер"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Бен"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Ибн"}, {'ORTH': "-"}, {}],
    # postfixes, i.e. Бендер-бей, Ахмет-паша
    [{}, {'ORTH': "-"}, {'LOWER': "оглы"}],
    [{}, {'ORTH': "-"}, {'LOWER': "заде"}],
    [{}, {'ORTH': "-"}, {'LOWER': "зуль"}],
    [{}, {'ORTH': "-"}, {'LOWER': "хан"}],
    [{}, {'ORTH': "-"}, {'LOWER': "шах"}],
    [{}, {'ORTH': "-"}, {'LOWER': "кызы"}],
    [{}, {'ORTH': "-"}, {'LOWER': "бей"}],
    [{}, {'ORTH': "-"}, {'LOWER': "бек"}],
    [{}, {'ORTH': "-"}, {'LOWER': "паша"}],
    [{}, {'ORTH': "-"}, {'LOWER': "хан"}],
    [{}, {'ORTH': "-"}, {'LOWER': "ага"}],
]

PRONOUN_PATTERNS = [
    # postfixes, i.e
    [{}, {'ORTH': "-"}, {'ORTH': "либо"}],
    [{}, {'ORTH': "-"}, {'ORTH': "нибудь"}],
    [{}, {'ORTH': "-"}, {'ORTH': "то"}],
    [{}, {'ORTH': "-"}, {'ORTH': "нито"}],
    # prefixes
    [{'LOWER': "кое"}, {'ORTH': "-"}, {}],
    [{'LOWER': "кой"}, {'ORTH': "-"}, {}],
    [{'LOWER': "как"}, {'ORTH': "-"}, {}],
]

PARTICLE_PATTERNS = [
    # i.e Ничего-то ты не знаешь, Джон Сноу.
    [{}, {'ORTH': "-"}, {'ORTH': "де"}],
    [{}, {'ORTH': "-"}, {'ORTH': "ка"}],
    [{}, {'ORTH': "-"}, {'ORTH': "те"}],
    # [{}, {'ORTH': "-"}, {'ORTH': "то"}],
    # [{}, {'ORTH': "-"}, {'ORTH': "с"}],
    [{}, {'ORTH': "-"}, {'ORTH': "таки"}],
]

ADVERB_PATTERNS = [
    [{'LOWER': "по"}, {'ORTH': "-"}, {}],
    [{'LOWER': "во"}, {'ORTH': "-"}, {}],
    [{'LOWER': "в"}, {'ORTH': "-"}, {}],

]

COMPOUND_PREPOSITION_PATTERNS = [
    [{'LOWER': "из"}, {'ORTH': "-"}, {}],
    [{'LOWER': "с"}, {'ORTH': "-"}, {'LOWER': "под"}],
    [{'LOWER': "для"}, {'ORTH': "-"}, {}],
    [{'LOWER': "за"}, {'ORTH': "-"}, {}],
]

PROPER_NAMES_WITH_DIGITS_PATTERNS = [
    # i.e ИЛ-2, T-34
    [{"IS_UPPER": True}, {'ORTH': "-"}, {"IS_DIGIT": True}],

]

COMPOUND_WORDS_WITH_DIGIT_PATTERNS = [
    [{"IS_DIGIT": True}, {'ORTH': "-"}, {'LOWER': "е"}],  # 1990-е
    [{"IS_DIGIT": True}, {'ORTH': "-"}, {'LOWER': "х"}],  # 2000-х
    [{"IS_DIGIT": True}, {'ORTH': "-"}, {'LOWER': "м"}],  # 2007-м
    [{"IS_DIGIT": True}, {'ORTH': "-"}, {'LOWER': "ти"}],  # 15-ти
    [{"IS_DIGIT": True}, {'ORTH': "-"}, {'LOWER': "го"}],  # 10-го

]

GEOGRAPHIC_NAMES_PATTERNS = [
    # Following PATTERNS will match both nouns (i.e "Австро-Венгрия" and "Австро-венгерский")
    # prefixes
    # russian compound names
    [{'LOWER': "усть"}, {'ORTH': "-"}, {}],
    [{'LOWER': "соль"}, {'ORTH': "-"}, {}],
    [{'LOWER': "верх"}, {'ORTH': "-"}, {}],
    [{'LOWER': "старо"}, {'ORTH': "-"}, {}],
    [{'LOWER': "верхне"}, {'ORTH': "-"}, {}],
    [{'LOWER': "нижне"}, {'ORTH': "-"}, {}],
    [{'LOWER': "ново"}, {'ORTH': "-"}, {}],
    [{'LOWER': "свято"}, {'ORTH': "-"}, {}],
    # region names
    [{'LOWER': "австро"}, {'ORTH': "-"}, {}],
    [{'LOWER': "эльзас"}, {'ORTH': "-"}, {}],
    # foreign articles
    [{'LOWER': "эль"}, {'ORTH': "-"}, {}],
    [{'LOWER': "аль"}, {'ORTH': "-"}, {}],
    [{'LOWER': "ле"}, {'ORTH': "-"}, {}],
    [{'LOWER': "ла"}, {'ORTH': "-"}, {}],
    [{'LOWER': "де"}, {'ORTH': "-"}, {}],
    [{'LOWER': "порт"}, {'ORTH': "-"}, {}],
    [{'LOWER': "санкт"}, {'ORTH': "-"}, {}],
    [{'LOWER': "нью"}, {'ORTH': "-"}, {}],
    [{'LOWER': "лос"}, {'ORTH': "-"}, {}],
    [{'LOWER': "вест"}, {'ORTH': "-"}, {}],
    [{'LOWER': "ханты"}, {'ORTH': "-"}, {}],
    [{'LOWER': "кабардино"}, {'ORTH': "-"}, {}],
    [{'LOWER': "алма"}, {'ORTH': "-"}, {}],
    [{'LOWER': "лас"}, {'ORTH': "-"}, {}],
    [{'LOWER': "шри"}, {'ORTH': "-"}, {}],
    [{'LOWER': "урус"}, {'ORTH': "-"}, {}],
    [{'LOWER': "мазари"}, {'ORTH': "-"}, {}],
    [{'LOWER': "коста"}, {'ORTH': "-"}, {}],
    # postfixes
    [{}, {'ORTH': "-"}, {'ORTH': "оол"}],
    [{}, {'ORTH': "-"}, {'ORTH': "Сити"}],
]

ORG_NAMES_PATTERNS = [
    [{}, {'ORTH': "-"}, {'LOWER': "групп"}],
    [{}, {'ORTH': "-"}, {'LOWER': "груп"}],
]

CONJUNCT_WORDS_PATTERNS = [
    # i.e. Ростов-на-Дону, Ортега-и-Гассет, Иван-да-Марья
    [{}, {'ORTH': "-"}, {'LOWER': "на"}, {'ORTH': "-"}, {}],
    [{}, {'ORTH': "-"}, {'LOWER': "да"}, {'ORTH': "-"}, {}],
    [{}, {'ORTH': "-"}, {'ORTH': "и"}, {'ORTH': "-"}, {}],
]

DIRECTION_PATTERNS = [
    # part of world
    [{'LOWER': "северо"}, {'ORTH': "-"}, {}],
    [{'LOWER': "юго"}, {'ORTH': "-"}, {}],
    [{'LOWER': "южно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "восточно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "западно"}, {'ORTH': "-"}, {}],
]

MISC_HYPHEN_FORM_PATTERNS = [
    [{'LOWER': "б"}, {'ORTH': "-"}, {"IS_ALPHA": True}],  # i.e "слава б-гу" - used in web corpus by jewish
    [{'LOWER': "г"}, {'ORTH': "-"}, {"IS_ALPHA": True}],  # i.e "г-ну Иванову"
    [{'LOWER': "д"}, {'ORTH': "-"}, {"IS_ALPHA": True}],  # i.e "д-ру Иванову"
    [{'LOWER': "е"}, {'ORTH': "-"}, {"IS_ALPHA": True}],  # i.e "е-майл"
    [{}, {'ORTH': "-"}, {'LOWER': "кво"}],

]

LOANWORDS_PATTERNS = [
    # latin-, german- and greek-based prefixes (more traditional prefixes)
    [{'LOWER': "вице"}, {'ORTH': "-"}, {}],
    [{'LOWER': "обер"}, {'ORTH': "-"}, {}],
    [{'LOWER': "унтер"}, {'ORTH': "-"}, {}],
    [{'LOWER': "лейб"}, {'ORTH': "-"}, {}],
    [{'LOWER': "штаб"}, {'ORTH': "-"}, {}],
    [{'LOWER': "экс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "контр"}, {'ORTH': "-"}, {}],
    [{'LOWER': "архи"}, {'ORTH': "-"}, {}],
    [{'LOWER': "альтер"}, {'ORTH': "-"}, {}],
    [{'LOWER': "форс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "статс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "микро"}, {'ORTH': "-"}, {}],
    [{'LOWER': "макро"}, {'ORTH': "-"}, {}],
    [{'LOWER': "кило"}, {'ORTH': "-"}, {}],
    [{'LOWER': "мега"}, {'ORTH': "-"}, {}],
    [{'LOWER': "гига"}, {'ORTH': "-"}, {}],
    [{'LOWER': "анти"}, {'ORTH': "-"}, {}],
    [{'LOWER': "квази"}, {'ORTH': "-"}, {}],
    [{'LOWER': "шеф"}, {'ORTH': "-"}, {}],
    [{'LOWER': "камер"}, {'ORTH': "-"}, {}],
    [{'LOWER': "альма"}, {'ORTH': "-"}, {}],
    [{'LOWER': "прима"}, {'ORTH': "-"}, {}],
    [{'LOWER': "ски"}, {'ORTH': "-"}, {}],
    [{'LOWER': "блиц"}, {'ORTH': "-"}, {}],

    # greek letters
    [{'LOWER': "альфа"}, {'ORTH': "-"}, {}],
    [{'LOWER': "бета"}, {'ORTH': "-"}, {}],
    [{'LOWER': "гамма"}, {'ORTH': "-"}, {}],
    [{'LOWER': "дельта"}, {'ORTH': "-"}, {}],
    [{'LOWER': "каппа"}, {'ORTH': "-"}, {}],
    [{'LOWER': "лямбда"}, {'ORTH': "-"}, {}],
    [{'LOWER': "сигма"}, {'ORTH': "-"}, {}],
    [{'LOWER': "тета"}, {'ORTH': "-"}, {}],
    [{'LOWER': "омега"}, {'ORTH': "-"}, {}],

    # english-based prefixes (more modern prefixes)
    [{'LOWER': "пресс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "мини"}, {'ORTH': "-"}, {}],
    [{'LOWER': "макси"}, {'ORTH': "-"}, {}],
    [{'LOWER': "миди"}, {'ORTH': "-"}, {}],
    [{'LOWER': "vip"}, {'ORTH': "-"}, {}],
    [{'LOWER': "вип"}, {'ORTH': "-"}, {}],
    [{'LOWER': "it"}, {'ORTH': "-"}, {}],
    [{'LOWER': "ит"}, {'ORTH': "-"}, {}],
    [{'LOWER': "премьер"}, {'ORTH': "-"}, {}],
    [{'LOWER': "эконом"}, {'ORTH': "-"}, {}],
    [{'LOWER': "бизнес"}, {'ORTH': "-"}, {}],
    [{'LOWER': "пит"}, {'ORTH': "-"}, {}],
    [{'LOWER': "кросс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "тест"}, {'ORTH': "-"}, {}],
    [{'LOWER': "секс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "стрип"}, {'ORTH': "-"}, {}],
    [{'LOWER': "хэдж"}, {'ORTH': "-"}, {}],
    [{'LOWER': "фокус"}, {'ORTH': "-"}, {}],
    [{'LOWER': "медиа"}, {'ORTH': "-"}, {}],
    [{'LOWER': "интернет"}, {'ORTH': "-"}, {}],
    [{'LOWER': "веб"}, {'ORTH': "-"}, {}],
    [{'LOWER': "арт"}, {'ORTH': "-"}, {}],
    [{'LOWER': "дот"}, {'ORTH': "-"}, {}],
    [{'LOWER': "топ"}, {'ORTH': "-"}, {}],
    [{'LOWER': "дресс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "пин"}, {'ORTH': "-"}, {}],
    [{'LOWER': "шорт"}, {'ORTH': "-"}, {}],
    [{'LOWER': "лонг"}, {'ORTH': "-"}, {}],
    [{'LOWER': "продакт"}, {'ORTH': "-"}, {}],
    [{'LOWER': "супер"}, {'ORTH': "-"}, {}],
    [{'LOWER': "гипер"}, {'ORTH': "-"}, {}],
    [{'LOWER': "аудио"}, {'ORTH': "-"}, {}],
    [{'LOWER': "видео"}, {'ORTH': "-"}, {}],
    [{'LOWER': "поп"}, {'ORTH': "-"}, {}],
    [{'LOWER': "рок"}, {'ORTH': "-"}, {}],
    [{'LOWER': "панк"}, {'ORTH': "-"}, {}],
    [{'LOWER': "рэп"}, {'ORTH': "-"}, {}],
    [{'LOWER': "рэп"}, {'ORTH': "-"}, {}],
    [{'LOWER': "экспресс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "блок"}, {'ORTH': "-"}, {}],
    [{'LOWER': "масс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "шоу"}, {'ORTH': "-"}, {}],
    [{'LOWER': "офф"}, {'ORTH': "-"}, {}],
    [{'LOWER': "пиар"}, {'ORTH': "-"}, {}],

]

COMPOUND_NOUNS = [

    [{'LOWER': "генерал"}, {'ORTH': "-"}, {}],
    [{'LOWER': "социал"}, {'ORTH': "-"}, {}],
    [{'LOWER': "национал"}, {'ORTH': "-"}, {}],
    [{'LOWER': "серо"}, {'ORTH': "-"}, {}],
    [{'LOWER': "англо"}, {'ORTH': "-"}, {}],
    [{'ORTH': "узи"}, {'ORTH': "-"}, {}],
    [{'LOWER': "матч"}, {'ORTH': "-"}, {}],
    [{'LOWER': "член"}, {'ORTH': "-"}, {}],
    [{'LOWER': "сверх"}, {'ORTH': "-"}, {}],
    [{'LOWER': "перво"}, {'ORTH': "-"}, {}],
    [{'LOWER': "псевдо"}, {'ORTH': "-"}, {}],
]

COMPOUND_ADJECTIVE_PATTERNS = [
    # [{"is_adjective": True}, {'ORTH': "-"}, {}],
    [{'LOWER': "черно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "научно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "военно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "физико"}, {'ORTH': "-"}, {}],
    [{'LOWER': "общественно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "торгово"}, {'ORTH': "-"}, {}],
    [{'LOWER': "темно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "взаимно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "горно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "ярко"}, {'ORTH': "-"}, {}],
    [{'LOWER': "нормативно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "сердечно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "воздушно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "желудочно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "мрачно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "химико"}, {'ORTH': "-"}, {}],
    [{'LOWER': "административно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "организационно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "жилищно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "дорожно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "планово"}, {'ORTH': "-"}, {}],
    [{'LOWER': "взлетно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "судебно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "социально"}, {'ORTH': "-"}, {}],
    [{'LOWER': "духовно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "патрульно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "инженерно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "финансово"}, {'ORTH': "-"}, {}],
    [{'LOWER': "либерально"}, {'ORTH': "-"}, {}],
    [{'LOWER': "медико"}, {'ORTH': "-"}, {}],
    [{'LOWER': "природно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "программно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "светло"}, {'ORTH': "-"}, {}],
    [{'LOWER': "целлюлозно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "санитарно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "опытно"}, {'ORTH': "-"}, {}],
    [{'LOWER': "природно"}, {'ORTH': "-"}, {}],

]

PUNCTUATION_PATTERNS = [
    [{'ORTH': "."}, {'ORTH': ".", 'OP': "+"}]
]

SYNTAGRUS_RARE_CASES = [
    # rare cases added here to improve SynTagRus evaluation
    [{'LOWER': "уик"}, {'ORTH': "-"}, {}],
    [{'LOWER': "айс"}, {'ORTH': "-"}, {}],
    [{'LOWER': "уль"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Фобос"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Улан"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Маньчжоу"}, {'ORTH': "-"}, {}],
    [{'ORTH': "X"}, {'ORTH': "-"}, {}],
    [{'ORTH': "T"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Ак"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Рублево"}, {'ORTH': "-"}, {}],
    [{'ORTH': "10^"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Кара"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Норд"}, {'ORTH': "-"}, {}],
    [{'ORTH': "членов"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Буэнос"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Карачаево"}, {'ORTH': "-"}, {}],
    [{'ORTH': "ра"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Коба"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Ну"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Орехово"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Al"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Азяш"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Та"}, {'ORTH': "-"}, {}],
    [{'ORTH': "ни"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Кенин"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Джалал"}, {'ORTH': "-"}, {}],
    [{'ORTH': "Алхан"}, {'ORTH': "-"}, {}],
    [{'ORTH': "экс"}, {'ORTH': "-"}, {}],
]
