from collections import defaultdict


def find_unaligned_sentences(parsed_sentences, gold_sentences):
    unaligned = []
    aligned = []
    for parse, gold in zip(parsed_sentences, gold_sentences):
        if [i.text for i in parse] != gold.words:
            unaligned.append((parse, gold))
        else:
            aligned.append(parse)
    return unaligned, aligned


def count_partially_aligned_tokens(unaligned):
    correct = 0
    for doc, gold in unaligned:
        for token, word in zip(doc, gold.words):
            if token.text == word:
                correct += 1
            else:
                break
    return correct


def find_problem_tokens(unaligned):
    problem_tokens = defaultdict(int)
    wrong_tokenization_examples = []
    for example in unaligned:
        for a, b in zip([i.text for i in example[0]], example[1].words):
            if a != b:
                problem_tokens[a, b] += 1
                wrong_tokenization_examples.append(example)
                break
    return problem_tokens, wrong_tokenization_examples


def find_examples_in_gold_parse(gold_sentences, query):
    results = []
    for gold in gold_sentences:
        for token in gold.words:
            if token.lower() == query.lower() or token.lower().startswith(query.lower()):
                results.append(gold)
    return results


def evaluate_sentences(nlp, documents, documents_gold_sentences):
    correct_sentences = 0
    golden_sentences = 0
    parsed_sentences = 0
    fails = []
    for docid in documents.keys():
        if docid != 0:
            doc = nlp(' '.join(documents[docid]))
            golden_sentences += len(documents_gold_sentences[docid])
            parsed_sentences += len(list(doc.sents))
            for parsed_sent, golden_sent in zip(doc.sents, documents_gold_sentences[docid]):
                if [i.text for i in parsed_sent] == golden_sent.words:
                    correct_sentences += 1
                else:
                    fails.append((parsed_sent, golden_sent))
                    # print('\n', ' '.join([i.text for i in parsed_sent]), '\n', ' '.join(golden_sent.words), '\n', '\n')
                    break
    return correct_sentences, golden_sentences, parsed_sentences, fails


def calculate_f1(correct_count, golden_count, produced_count):
    recall = correct_count / golden_count
    precision = correct_count / produced_count
    return precision, recall, 2 * recall * precision / (recall + precision)
