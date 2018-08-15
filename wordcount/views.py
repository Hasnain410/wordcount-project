from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',)

worddictionary = {}

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1
        else:
            # add to dictionary
            worddictionary[word] = 1

    sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sorted_words': sorted_words, })


def about(request):
    return render(request,'about.html',)




#the home function was defined here, but we are pulling information from the
# home.html files. The html files can also work with some python code inside.
