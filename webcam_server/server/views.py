import os

from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from pybase64 import b64decode
import time


@csrf_exempt
def save_image(request):
    print("HELLO!!!")
    if request.method == 'POST':
        # print(request.POST.get('image', ""))
        with open(
                f"D:/WhitespaceVoid/Projects/PycharmProjects/New_Bitch/webcam_server/server/static/images/temp/{time.strftime('%Y%m%d-%H%M%S')}.png",
                'wb') as f:
            img_data = request.POST['image']
            format, imgstr = img_data.split(';base64,')
            f.write(b64decode(imgstr))
    if len(os.listdir('D:/WhitespaceVoid/' +
                      'Projects/PycharmProjects/' +
                      'New_Bitch/webcam_server/server/static/images/temp/')) == 5:

    return HttpResponse("uploaded")


def index(request):
    # print("BOBO")
    return render(request, 'index.html')
