import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stop_words_english = set(stopwords.words('english'))
stop_words_chinese = set(stopwords.words('chinese'))

def remove_stop_words(text):
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words_english]
    filtered_tokens = [token for token in filtered_tokens if token.lower() not in stop_words_chinese]

    return ' '.join(filtered_tokens)


stemmer = PorterStemmer()


def stem_text(text):
    tokens = nltk.word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)


lemmatizer = WordNetLemmatizer()


def lemmatize_text(text):
    tokens = nltk.word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized_tokens)


def replace_abbreviations(text):
    replacements = {
        "I'm": "I am",
        "I'll": "I will",
        "can't": "cannot",
        # add more abbreviations and their replacements as needed
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def expand_contractions(text):
    replacements = {
        "I'm": "I am",
        "I'll": "I will",
        "can't": "cannot",
        # add more contractions and their expansions as needed
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


import jieba

def chinese_text_segmentation(text):
    # cut the text into words
    words = jieba.cut(text, cut_all=False)
    # join the words back into a string
    segmented_text = ' '.join(words)
    return segmented_text


if __name__ == "__main__":
    input = '我说了一句英语：The cats were chasing the mice'
    x = chinese_text_segmentation(input)
    x = remove_stop_words(x)
    x = stem_text(x)
    print(x)