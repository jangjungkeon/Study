import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myajax.models import Jikwon


def MainFunc(request):
    return render(request, 'main.html')


def jikwonFunc(request):
    # print('request.jik : ', request.GET.get('jik'))
    # test = Jikwon.objects.all()
    # request.GET.get('jik')
    sdata = Jikwon.objects.filter(jikwon_jik=request.GET.get('jik'))
    datas = []
    for i in sdata:
        dic = {'jikwon_no': i.jikwon_no, 'jikwon_name': i.jikwon_name, 'buser_num': i.buser_num}
        datas.append(dic)
    # print(datas)
    return HttpResponse(json.dumps(datas), content_type="application/json")
