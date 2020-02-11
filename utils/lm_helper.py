# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:51:10 2020

@author: Shreyans
"""
import random 
from nltk.corpus import mac_morpho, brown, gutenberg


    
def get_test_data(num_brown = 500, num_mac = 20):
    test_list = []
    for file in brown.fileids():
        test_list.append(list(brown.sents(file)))
    for file in mac_morpho.fileids():
        test_list.append(list(mac_morpho.sents(file)))
    random.shuffle(test_list)
    return test_list

def get_train_data():
    train_list = []
    for file in gutenberg.fileids():
        train_list.append(list(gutenberg.sents(file)))
    return train_list