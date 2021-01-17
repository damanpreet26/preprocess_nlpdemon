from preprocess_nlpdemon import utils

__version__="1.0"

def get_word_counts(x):
	return utils._get_word_counts(x)
	

def char_counts(x):
	return utils._char_counts(x)


def average_word_count(x):
	return utils._average_word_count(x)

