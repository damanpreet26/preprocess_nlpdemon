import re
import os
import sys

import pandas as pd
import numpy as np

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

