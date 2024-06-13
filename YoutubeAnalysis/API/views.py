from django.shortcuts import render,HttpResponse
import urllib.request
import json
# Create your views here.
def show(request):
    url=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCcxZNL3o00nZeKV4E16I-mA&key=AIzaSyBzadJbQgAbZck3R149IGymMQyu-gXDc1k").read()
    data_sub=json.loads(url)['items'][0]['statistics']["subscriberCount"]
    data_view = json.loads(url)['items'][0]['statistics']["viewCount"]
    data_video = json.loads(url)['items'][0]['statistics']["videoCount"]
    dict_data={"sub":data_sub,"view":data_view,"vdio":data_video}
    return render(request,'APItemplates/page.html',context=dict_data)

