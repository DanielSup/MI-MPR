import os
from django.http import HttpResponse
from django.shortcuts import render

from forms import MyForm
from speedcheck import loadInputAndProcess
from django.conf import settings


import datetime

def home_view(request, *args, **kwargs):
    today = datetime.datetime.now().date()

    if request.method=='POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            title = str(request.FILES['field'])
            content = request.FILES['field'].read()
            f = open(str(settings.MEDIA_ROOT)+title, "wb")
            f.write(content)
            f.close()
            print(settings.MEDIA_ROOT)
            loadInputAndProcess('media/'+title)
            return render(request, "myaction.html", {'value': "output.avi"})

    form = MyForm()
    return render(request, "home.html", {"today" : today, 'form': form })