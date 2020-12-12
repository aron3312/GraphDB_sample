import jieba.posseg as pseg
import re


def pos_cut(text):
    cut_words = pseg.cut(text)
    return [(word, pos) for word, pos in cut_words]


def regexp_match(text, pattern, filter):
    if filter:
        return [re.search(pattern, p).group(1) if re.search(pattern, p) else '' for p in text.split('。')
         if filter in p and re.search(pattern, p)]
    else:
        return re.search(pattern , text).group(1) if re.search(pattern, text) else ''


def extract_feature(result):
    return [(result[i][0], result[i + 1][0]) for i, p in enumerate(result) if
     i < len(result) - 1 and p[1] == 'n' and result[i + 1][1] == 'nr']

