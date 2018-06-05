NO_TERMINAL_PATTERNS = [
    # general pattern, including forms like "г. Москва", "д. Старые Выселки", "р. Нева"
    [{'SHAPE': "x"}, {'ORTH': "."}, {"IS_TITLE": True}],
    # organisation name patters
    [{'LOWER': "им"}, {'ORTH': "."}, {"IS_TITLE": True}],
    # address pattern, street component
    [{'LOWER': "ул"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "пр"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "просп"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "пер"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "наб"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "бул"}, {'ORTH': "."}, {"IS_TITLE": True}],
    # geographic patterns
    [{'LOWER': "оз"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "хр"}, {'ORTH': "."}, {"IS_TITLE": True}],

    # address pattern, building number component
    # [{'LOWER': "д"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "корп"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "кор"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "стр"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    # address pattern, unit number component
    [{'LOWER': "оф"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "кв"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    # legal pattern
    [{'LOWER': "ч"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    # [{'LOWER': "п"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "ст"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    # numbers patters
    [{'LOWER': "тыс"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "млн"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "млрд"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "трл"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "ок"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    # time patterns
    [{'LOWER': "час"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "мин"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    [{'LOWER': "сек"}, {'ORTH': "."}, {"IS_DIGIT": True}],
    # language patterns (i.e. in Wikipedia abstracts)
    [{'LOWER': "лат"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "англ"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "нем"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "фр"}, {'ORTH': "."}, {"IS_TITLE": True}],
    [{'LOWER': "итал"}, {'ORTH': "."}, {"IS_TITLE": True}],

    [{'SHAPE': 'X'}, {'ORTH': "."}, {'SHAPE': 'X'}],

]
