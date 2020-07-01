# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 00:10:08 2020

@author: Farhan Basheer
"""
import operator

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increae
            worddictionary[word] += 1
        else:
            #add to dictionay
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')