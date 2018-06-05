## spacy_russian_tokenizer: russian segmentation and tokenization rules

Tokenization in Russian language is not that simple topic when it comes
to compound words connected by hyphens. Some of them (i.e. "какой-то",
"кое-что", "бизнес-ланч") should be treated as single unit, while other
(i.e. "суп-харчо", "инженер-программист") treated as multiple tokens.
Correct tokenization is especially important when training language
model, because in most training datasets (i.e. SynTagRus) tokens are
split or merged correctly and wrong tokenization reduces model's quality.


This package uses spaCy [Matcher API](https://spacy.io/api/matcher) to
create rules for specific cases and exceptions in Russian language.

## Installation


## Usage
```
from spacy.lang.ru import Russian
from spacy_russian_tokenizer import RussianTokenizer, MERGE_PATTERNS
text = "Не ветер, а какой-то ураган!"
nlp = Russian()
doc = nlp(text)
print([(token.text) for token in doc])
# Notice that word "какой-то" is split into three tokens.
# ['Не', 'ветер', ',', 'а', 'какой', '-', 'то', 'ураган', '!']

russian_tokenizer = RussianTokenizer(nlp, MERGE_PATTERNS)
nlp.add_pipe(russian_tokenizer, name='russian_tokenizer')
doc = nlp("Не ветер, а какой-то ураган!")
print([(token.text) for token in doc])
# ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
```


