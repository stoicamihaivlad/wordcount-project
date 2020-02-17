from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'hithere':'Vlad'})

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    numberofwords = len(wordlist)
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increase count
             worddictionary[word]+=1
        else:
            #add it to the dictionary
            worddictionary[word]=1
    sortedWords = sorted (worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html', {'fulltext':fulltext,'count':numberofwords,'sortedWords':sortedWords})


