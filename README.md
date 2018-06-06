## spacy_russian_tokenizer: Russian segmentation and tokenization rules for spaCy

Tokenization in Russian language is not that simple topic when it comes to compound words connected by hyphens. Some of 
them (i.e. "какой-то", "кое-что", "бизнес-ланч") should be treated as single unit, while other (i.e. "суп-харчо", 
"инженер-программист") treated as multiple tokens. Correct tokenization is especially important when training language
model, because in most training datasets (i.e. SynTagRus) tokens are split or merged correctly and wrong tokenization 
reduces model's quality.
Example of default behaviour:
```python
from spacy.lang.ru import Russian
text = "Не ветер, а какой-то ураган!"
nlp = Russian()
doc = nlp(text)
print([token.text for token in doc])
# ['Не', 'ветер', ',', 'а', 'какой', '-', 'то', 'ураган', '!']
# Notice that word "какой-то" is split into three tokens.
```

This package uses spaCy [Matcher API](https://spacy.io/api/matcher) to create rules for specific cases and exceptions in
 Russian language.

## Installation
```
pip install git+https://github.com/aatimofeev/spacy_russian_tokenizer.git
```

## Implementation
Basically, the package is just a collection of manually tunes Matcher patterns. Most patterns were acquired from 
SynTagRus vocabulary and [lemma dictionary](http://dict.ruslang.ru/freq.php) from National Russian Language Corpus 
(НКРЯ).

## Usage
Core patterns are collected in `MERGE_PATTERNS` variable.
```python
from spacy.lang.ru import Russian
from spacy_russian_tokenizer import RussianTokenizer, MERGE_PATTERNS
text = "Не ветер, а какой-то ураган!"
nlp = Russian()
doc = nlp(text)
russian_tokenizer = RussianTokenizer(nlp, MERGE_PATTERNS)
nlp.add_pipe(russian_tokenizer, name='russian_tokenizer')
doc = nlp(text)
print([token.text for token in doc])
# ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
# Notice that word "какой-то" remains a single token. 
```
One can also add patterns, found in SynTagRus but absent in National Russian Language Corpus
```python
from spacy.lang.ru import Russian
from spacy_russian_tokenizer import RussianTokenizer, MERGE_PATTERNS, SYNTAGRUS_RARE_CASES
text = "«Фобос-Грунт» — российская автоматическая межпланетная станция (АМС)."
nlp = Russian()
doc = nlp(text)
russian_tokenizer = RussianTokenizer(nlp, MERGE_PATTERNS + SYNTAGRUS_RARE_CASES)
nlp.add_pipe(russian_tokenizer, name='russian_tokenizer')
doc = nlp(text)
print([token.text for token in doc])
# ['«', 'Фобос-Грунт', '»', '—', 'российская', 'автоматическая', 'межпланетная', 'станция', '(', 'АМС', ')', '.']
```

