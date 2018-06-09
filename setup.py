from distutils.core import setup

setup(
    name="spacy-russian-tokenizer",
    version='0.1.1',
    description="Custom Russian tokenizer for spaCy",
    long_description="This package uses spaCy Matcher API to create rules for specific cases and exceptions in Russian "
                     "language.",
    author="Anton Timofeev",
    author_email="aatimofeev@hse.ru",
    url="https://github.com/aatimofeev/spacy_russian_tokenizer/",
    keywords="natural language processing russian tokenizer tokeniser",
    packages=['spacy_russian_tokenizer', 'spacy_russian_tokenizer.patterns'],
    install_requires=['spacy'],
    tests_require=['pytest'],
)
