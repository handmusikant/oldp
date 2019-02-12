from typing import Generator

from spacy.tokens import Doc

from oldp.apps.nlp.lemmatizer import lemmatize


def extract_relations(doc: Doc, entity_name: str, model_name: str, noun_phrases=False) -> Generator:
    merge_spans(doc.ents)
    if noun_phrases:
        merge_spans(doc.noun_chunks)

    for span in filter(lambda t: t.label_ == entity_name, doc.ents):
        token = span[0]
        if model_name == 'de_core_news_sm':
            relation = extract_relations_de(token)
            relation = lemmas(relation, 'de')
        elif model_name == 'en_core_web_sm':
            relation = extract_relations_en(token)
            relation = lemmas(relation, 'en')
        else:
            raise ValueError('Unsupported model {}!'.format(model_name))

        if relation:
            yield relation, (token.text, span.start_char, span.end_char - 1)


def lemmas(word_tuple, lang='de'):
    if word_tuple is None:
        return None

    lemmatized_words = ()
    for word in word_tuple:
        lemmatized_words += (lemmatize(word, lang=lang),)
    return lemmatized_words


def merge_spans(spans):
    for span in spans:
        span.merge()


def extract_relations_en(token):
    """https://spacy.io/api/annotation#dependency-parsing CLEAR Style"""
    if token.dep_ == 'dobj':
        # entity is attribute or direct object
        verb = token.head.text
        subject = None
        for t in token.head.lefts:
            if t.dep_ == 'nsubj':
                subject = t.text
        return subject, verb

    elif token.dep_ == 'pobj' and token.head.dep_ == 'prep':
        # entity is object of preposition
        verb = token.head.head.text
        subject = None
        for t in token.head.head.lefts:
            if t.dep_ == 'nsubj':
                subject = t.text
        return subject, verb


def extract_relations_de(token):
    """https://spacy.io/api/annotation#dependency-parsing TIGER Treebank"""
    if token.dep_ == 'oa':
        # entity is accusative object
        head = token.head
        while head.dep_ != 'ROOT':
            head = head.head
        verb = head.text
        subject = None
        for t in head.children:
            if t.dep_ == 'sb':
                subject = t.text
        return subject, verb

    elif token.dep_ == 'nk':
        # entity is noun kernel
        if token.head.dep_ == 'oa':
            # without noun chunking the nk may be part of the oa
            token.dep_ = 'oa'
            return extract_relations_de(token)

        prep = token.head.text

        subject = None
        head = token.head
        while head.dep_ != 'ROOT':
            head = head.head
        for t in head.children:
            if t.dep_ == 'sb':
                subject = t.text
        return subject, prep
