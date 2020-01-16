from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['text']
    wordc=fulltext.split()
    worddict={}
    for i in wordc:
        if i in worddict:
            worddict[i]+=1
        else:
            worddict[i]=1
    sort=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'wordc':len(wordc),'worddict':sort})
