#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if (n/2).is_integer() == True ]
    return evens


def make_exclamation(sentence_list):
    exclaimed = [n + '!' for n in sentence_list]
    return exclaimed