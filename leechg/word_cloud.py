# --*-- coding:utf-8 --*--
__author__ = 'licha'

from django.http import HttpResponse
from django.shortcuts import render
import  helper.wordCloudHelper as word
import time
import os,sys

reload(sys)
sys.setdefaultencoding('utf8')
path = os.path.dirname(os.path.realpath(__file__))
def get(request):
    text = ""
    try:
        text1 = request.POST['text']
        text = text1
    except Exception,e:
        print "not POST"
    try:
        text2 = request.GET['text']
        text = text2
    except Exception,e:
        print "not GET"
    print text
    if text == "":
        context = {}
        response = HttpResponse("{'cuccess':false,'msg':'必须输入参数!'}", content_type="application/json; charset=utf-8"  )
        return render(request, 'index.html', context)

    img = word.getWordCloud(text)
    #image_data = img.read()
    rand = str(time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time())))
    filename = path + "/temp/pic"+ rand +".png"
    img.save(filename)
    image_data = open(filename,"rb").read()
    return HttpResponse(image_data,content_type="image/png")

