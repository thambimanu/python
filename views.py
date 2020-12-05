from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request,'home.html')
def about(request):
	return render(request,'about.html')

def count(request):
	fulltext=request.GET['fulltext']
	wordlist=fulltext.split()
	wddict ={}
	for word in wordlist:
		if word in wddict:
			wddict[word] += 1	
		else:
			wddict[word]=1
		
	#print(fulltext)
	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'wddict':wddict.items()})
