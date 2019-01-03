# -*- coding:utf-8 *-
import re
from langdetect import detect

class MainFunc():
    def DetectFunc(words):
        return detect(words)

    def WordCounter(lang,words):
        if lang == "ja" or lang == "ko":
            words = re.sub(r'\.|,|"|\n|\s|\t'," ",words).strip()
            return len(words)
        else:
            return len(list(filter(lambda w: len(w) > 0, re.split(r'\s|"|,|\.', words))))
