from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyse(request):
    text= request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','default')
    fullcap = request.POST.get('fullcap','default')
    newline = request.POST.get('newline','default')
    spaceRemover = request.POST.get('spaceRemover','default')

    if removepunc == "on":
        analysed = ""
        punc_list = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in text:
            if char not in punc_list:
                analysed = analysed + char

        params = {"analyzed_text":analysed, "purpose":"Remove Puncuations"}
        text = analysed

    if fullcap == "on":
        analysed = ""
        for char in text:
            analysed = analysed + char.upper()
        
        params = {"analyzed_text":analysed, "purpose":"capitalize text"}
        text = analysed

    if newline == "on":
        analysed = ""
        for char in text:
            if char !="\n" and char!="\r":
                analysed = analysed + char
                
        params = {"analyzed_text":analysed, "purpose":"NewLine remover"}
        text = analysed 

    if spaceRemover == "on":
        analysed = ""
        for index,char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                analysed =analysed + char
        
        params = {"analyzed_text":analysed, "purpose":"Space remover"}

    if(spaceRemover != "on" and newline != "on" and fullcap != "on" and removepunc != "on"):
            return HttpResponse('please select a operation')
    
    return render(request,"analyze.html",params)
    
def navi(request):
    return render (request,"navi.html")
