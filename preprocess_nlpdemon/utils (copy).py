import re
import os
import sys

import pandas as pd
import numpy as np
import spacy
import matplotlib.pyplot

from spacy.lang.en.stop_words import STOP_WORDS as stopwords


## word count
def _get_word_counts(x):
    count=len(str(x).split())
    return count

## character count
def _char_counts(x):
    count=len("".join(str(x).split()))
    return count

## average word length
def _average_word_count(x):
    val = _char_counts(x)/_get_word_counts(x)
    return val

## stopword handeling
def _get_stop_words_count(x):
    count = len([t for t in x.split() if t in stopwords])
    return count

## count hahtags #
def _count_hashtags(x):
    count = len([t for t in x.split() if t.startswith("#")])
    return count

## count mentions @
def _count_mentions(x):
    count =  len([t for t in x.split() if t.startswith("@")])
    return count

## count numeric digits in te string
def _count_digits(x):
    count = len([t for t in x.split() if t.isdigit()])
    return count

## count upper case words in the string
def _count_uppe_case(x):
    count = len([t for t in x.split() if t.isupper()])
    return count

## contraction to expansion
def _get_contraction_exp(x):
    contractions = {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "can't've": "cannot have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'd've": "he would have",
        "he'll": "he will",
        "he'll've": "he will have",
        "he's": "he is",
        "how'd": "how did",
        "how'd'y": "how do you",
        "how'll": "how will",
        "how's": "how does",
        "i'd": "i would",
        "i'd've": "i would have",
        "i'll": "i will",
        "i'll've": "i will have",
        "i'm": "i am",
        "i've": "i have",
        "isn't": "is not",
        "it'd": "it would",
        "it'd've": "it would have",
        "it'll": "it will",
        "it'll've": "it will have",
        "it's": "it is",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "mightn't've": "might not have",
        "must've": "must have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "needn't": "need not",
        "needn't've": "need not have",
        "o'clock": "of the clock",
        "oughtn't": "ought not",
        "oughtn't've": "ought not have",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "shan't've": "shall not have",
        "she'd": "she would",
        "she'd've": "she would have",
        "she'll": "she will",
        "she'll've": "she will have",
        "she's": "she is",
        "should've": "should have",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "so've": "so have",
        "so's": "so is",
        "that'd": "that would",
        "that'd've": "that would have",
        "that's": "that is",
        "there'd": "there would",
        "there'd've": "there would have",
        "there's": "there is",
        "they'd": "they would",
        "they'd've": "they would have",
        "they'll": "they will",
        "they'll've": "they will have",
        "they're": "they are",
        "they've": "they have",
        "to've": "to have",
        "wasn't": "was not",
        " u ": " you ",
        " ur ": " your ",
        " n ": " and ",
        "won't": "would not",
        'dis': 'this',
        'bak': 'back',
        'brng': 'bring'}

    if type(x) is str:
        for key in contractions:
            value=contractions[key]
            x=x.replace(key, value)
        return x
    else:
        return x

## count and email vals
def _count_emails(x):
    pattern=r"[0-9a-z.-_]+@[0-9a-z.-_]+\.[0-9a-z.-_]"
    val=re.findall(pattern, x)
    count=len(val)
    return  val, count

## remove found emails
def _remove_emails(x):
    pattern = r"[0-9a-z.-_]+@[0-9a-z.-_]+\.[0-9a-z.-_]"
    x=re.sub(pattern, "", x)
