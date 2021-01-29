import re
import os
import sys

import pandas as pd
import numpy as np


## word count
def _get_word_counts(x):
    count=len(str(x).split())
    return count

