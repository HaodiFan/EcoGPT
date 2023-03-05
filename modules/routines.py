from tokenization import remove_stop_words, stem_text, lemmatize_text, replace_abbreviations, expand_contractions, \
    chinese_text_segmentation

routines = [
    chinese_text_segmentation,
    # remove_stop_words,
    stem_text
]
