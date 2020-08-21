from collections import defaultdict


def get_mean_actual(lst):
    return sum(lst)/len(lst)


def get_range_actual(lst):
    return max(lst) - min(lst) 



def count_words(string):
    string = string.replace("\n", " ").replace("\t", " ")
    return len(string.split(" "))


def create_first_letter_dict(string):
    string = string.replace("\n", " ").replace("\t", " ")
    words = string.split(" ")
    d = defaultdict(list)
    for word in words:
        key = word.lower()[0]
        d[key].append(word)
    return d