from django.shortcuts import render
from django.http import HttpResponse
import urllib
import http.client
import random
import minigameProject.settings as setting
import time
import json
from .models import Minigame73

# Create your views here.

def sendMsg(PhoneNumber, VerifyCode):
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    account = "C40979219"
    password = "d6bafda9489356b5c326fc490f89f362"
    text = "您的验证码是："+ VerifyCode +"。请不要把验证码泄露给其他人。"
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': PhoneNumber, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str.decode('utf-8')

def genNum():
    s = ""
    for i in range(6):
        s += str(random.randint(0,9))
    return s

def getVerifyCode(request):
    VerifyCode = genNum()
    param = ""
    try:
        param = request.POST.get("param")
    except:
        result = {"code":-1, "msg":"输入参数错误！"}
        return HttpResponse(json.dumps(result))
    param = json.loads(param)
    phoneNumber = param["phoneNumber"]
    if(phoneNumber == ""):
        result = {"code":-1, "msg":"输入号码为空"}
        return HttpResponse(json.dumps(result))
    setting.map_code[phoneNumber] = (VerifyCode,time.time()) #验证码，创建时间
    #result = sendMsg(phoneNumber, VerifyCode)
    #print(result)
    return HttpResponse(VerifyCode)
    #return HttpResponse(sendMsg(phoneNumber))

def login(request):
    param = ""
    try:
        print(request.POST)
        param = request.POST.get("param")
        print(">>>>>")
        print(param)
        print(">>>>>")
    except:
        result = {"code": -1, "msg": "输入参数错误！"}
        return HttpResponse(json.dumps(result))
    param = json.loads(param)
    print(param)
    if(param.get("deviceID", None) == None):
        phoneNumber = param["phoneNumber"]
        verifyCode = param["verifyCode"]
    else:
        deviceID = param["deviceID"]
        player = Minigame73.objects.filter(username=deviceID)
        if(len(player) == 0):
            Minigame73.objects.create(username=deviceID)
            result = {"code": 0, "msg": "登陆成功", "data": ""}
            return HttpResponse(json.dumps(result))
        else:
            data = player[0].data
            result = {"code": 0, "msg": "登陆成功","data":data}
            return HttpResponse(json.dumps(result))

    if setting.map_code.get(phoneNumber, None) == None:
        result = {"code": -1, "msg": "请先获取验证码"}
        return HttpResponse(json.dumps(result))
    codeGenTime = setting.map_code[phoneNumber][1]
    if(codeGenTime- time.time() > 60):
        result = {"code":-1, "msg":"验证码过期"}
        return HttpResponse(json.dumps(result))
    if(verifyCode == setting.map_code[phoneNumber][0]):
        player = Minigame73.objects.filter(username=phoneNumber)
        if (len(player) == 0):
            Minigame73.objects.create(username=phoneNumber)
            result = {"code": 0, "msg": "登陆成功", "data": ""}
            return HttpResponse(json.dumps(result))
        else:
            data = player[0].data
            result = {"code": 0, "msg": "登陆成功", "data": data}
            return HttpResponse(json.dumps(result))
    else:
        result = {"code":-1, "msg":"验证码不正确"}
        return HttpResponse(json.dumps(result))

def saveData(request):
    try:
        param = request.POST.get("param")
    except:
        result = {"code": -1, "msg": "输入参数错误！"}
        return HttpResponse(json.dumps(result))
    param = json.loads(param)
    username = param["useranme"]
    data = param["data"]
    player = Minigame73.objects.filter(username = username)[0]
    player.data = data
    player.save()
    result = {"code": 0, "msg": "存档成功"}
    return HttpResponse(json.dumps(result))


