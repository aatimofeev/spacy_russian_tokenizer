from collections import defaultdict
import re

from spacy.tokens import Doc
from spacy.gold import GoldParse
from spacy.syntax.nonproj import projectivize

from spacy_russian_tokenizer.src import MERGE_PATTERNS
from spacy_russian_tokenizer.src import NO_TERMINAL_PATTERNS
from spacy_russian_tokenizer.pipeline import pipeline
from spacy_russian_tokenizer.evaluation.evaluation_utils import find_unaligned_sentences, find_problem_tokens, \
    calculate_f1, count_partially_aligned_tokens, evaluate_sentences


def extract_docs_and_golds(nlp, conllu_file):
    parsed_sentences = []
    gold_sentences = []
    documents = defaultdict(list)
    documents_gold_sentences = defaultdict(list)
    gold_segmentation = defaultdict(list)

    with open(conllu_file, "r", encoding="utf8") as conllu:
        for chunk in conllu.read().split('\n\n')[:-1]:
            lines = chunk.split('\n')
            if lines[0].startswith('# newdoc'):
                docid, sentid = lines[1].split(' ')[-2:]
                lines = lines[1:]
            elif lines[0].startswith('# source'):
                docid, sentid = 0, 0
            elif lines[0].startswith('# text'):
                docid, sentid = lines[0].split(' ')[-2:]
                lines = [''] + lines
            else:
                docid, sentid = lines[0].split(' ')[-1].rsplit('_', 1)
            text = lines[1].split('=')[-1].strip()
            if lines[2].startswith('# sent_id'):
                lines = lines[1:]
            sent_words = []
            sent_tags = []
            sent_heads = []
            sent_deps = []
            for line in lines[2:]:
                id_, word, lemma, pos, tag, morph, head, dep, _1, _2 = line.split('\t')
                if '.' in id_:
                    continue
                if '-' in id_:
                    continue
                id_ = int(id_) - 1
                try:
                    head = int(head) - 1 if head != '0' else id_
                except ValueError:
                    head = id_
                sent_words.append(word)
                sent_tags.append(tag)
                sent_heads.append(head)
                sent_deps.append('ROOT' if dep == 'root' else dep)
            sent_heads, sent_deps = projectivize(sent_heads, sent_deps)
            # text should be cleaned, because removing trailing spaces is not point of spaCy at all
            # and should not be evaluated
            text = re.sub('\s+', ' ', text).strip().strip()
            parsed_sentences.append(nlp(text))
            gold = GoldParse(Doc(nlp.vocab, words=sent_words), words=sent_words, heads=sent_heads,
                             tags=sent_tags, deps=sent_deps,
                             entities=['-'] * len(sent_words))
            gold_sentences.append(gold)
            documents[docid].append(text)
            documents_gold_sentences[docid].append(gold)
            gold_segmentation[docid].append([1] + [0] * (len(sent_words) - 1))
    return parsed_sentences, gold_sentences, gold_segmentation, documents, documents_gold_sentences


if __name__ == "__main__":
    import argparse
    import time

    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument('--conllu_file', help='Syntagrus CoNLL file', required=True, type=str)
    args = parser.parse_args()

    nlp = pipeline(MERGE_PATTERNS, NO_TERMINAL_PATTERNS)
    parsed_sentences, gold_sentences, gold_segmentation, documents, documents_gold_sentences = extract_docs_and_golds(
        nlp,
        args.conllu_file)
    unaligned, aligned = find_unaligned_sentences(parsed_sentences, gold_sentences)

    golden_count = sum([len(sent.words) for sent in gold_sentences])
    fully_correct_parsed_count = sum([len(sent) for sent in aligned])
    parsed_count = sum([len(sent) for sent in parsed_sentences])
    partially_correct_parsed_count = count_partially_aligned_tokens(unaligned)

    strict_tokenization_evaluation = calculate_f1(correct_count=fully_correct_parsed_count, golden_count=golden_count,
                                                  produced_count=parsed_count)
    loose_tokenization_evaluation = calculate_f1(
        correct_count=fully_correct_parsed_count + partially_correct_parsed_count,
        golden_count=golden_count,
        produced_count=parsed_count)

    correct_sentences, golden_sentences, parsed_sentences, fails = evaluate_sentences(nlp, documents,
                                                                                      documents_gold_sentences)

    segmentation_evaluation = calculate_f1(correct_count=correct_sentences, golden_count=golden_sentences,
                                           produced_count=parsed_sentences)

    end_time = time.time() - start_time
    for fail in fails:
        print('\n\n',
              ' '.join([i.text for i in fail[0]]),
              '\n',
              ' '.join(fail[1].words))
    print("Evaluation took {end_time:.2f} seconds, {improvement:.2f} improvement".format(end_time=end_time,
                                                                                         improvement=(
                                                                                                         end_time / 58.40) - 1))
    print("Strict tokenization evaluation: F1: {f1:.3f}, precision: {precision:.2f}, recall: {recall:.2f}".format(
        precision=strict_tokenization_evaluation[0],
        recall=strict_tokenization_evaluation[1],
        f1=strict_tokenization_evaluation[1]))
    print("Strict tokenization results improvement: {x:.3f}".format(
        x=strict_tokenization_evaluation[0] / 0.946 - 1))
    print("{x} more correct tokens achieved (total: {y})".format(x=fully_correct_parsed_count - 823261,
                                                                 y=fully_correct_parsed_count))

    print("Loose tokenization evaluation: F1: {f1:.3f}, precision: {precision:.2f}, recall: {recall:.2f}".format(
        precision=loose_tokenization_evaluation[0],
        recall=loose_tokenization_evaluation[1],
        f1=loose_tokenization_evaluation[1]))
    print("Loose tokenization results improvement: {x:.3f}".format(
        x=loose_tokenization_evaluation[0] / 0.971 - 1))

    print("Sentence segmentation evaluation: F1: {f1:.3f}, precision: {precision:.2f}, recall: {recall:.2f}".format(
        precision=segmentation_evaluation[0],
        recall=segmentation_evaluation[1],
        f1=segmentation_evaluation[1]))
    print(
        "Sentence segmentation results improvement: {x:.3f}".format(
            x=segmentation_evaluation[0] / 0.214 - 1))
    print("{x} more correct sentences achieved (total:{y})".format(x=correct_sentences - 0,
                                                                   y=correct_sentences))
