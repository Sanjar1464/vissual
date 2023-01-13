from django.shortcuts import render
from django.http import HttpResponse

def korish(request):
    return HttpResponse("yangilik;lar")


def ozgartirish(request):
    return HttpResponse("")

def yangilik(request, id):
    if id > 0 and id < 4:
        yangilik_ = [
            "yangilik 1"
            "yangilik 2"
            "yangilik 3"
        ]
        return HttpResponse(yangilik_[id-1])
    else:
        return HttpResponse("bunday yangilik mavjud emas")