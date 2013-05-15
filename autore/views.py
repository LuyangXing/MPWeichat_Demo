# Create your views here.
# coding=utf-8
from django.http import HttpResponse
import hashlib, time
from xml.etree import ElementTree as ET


def handle_request(request):
    if request.method == 'GET':
        response = HttpResponse(check_signature(request), content_type="text/plain")
        return response
    elif request.method == 'POST':
        response = HttpResponse(response_msg(request), content_type="application/xml")
        return response
    else:
        return HttpResponse("Invalid Request")


def check_signature(req):
    token = "wxtoken20130515"
    params = req.GET
    args = [token, params['timestamp'], params['nonce']]
    args.sort()
    if hashlib.sha1("".join(args)).hexdigest() == params['signature']:
        if params.has_key('echostr'):
            return HttpResponse(params['echostr'])
    else:
        return HttpResponse("Invalid Request")


def response_msg(req):
    if req.raw_post_data:
        xml = ET.fromstring(req.raw_post_data)
        msgtype = xml.find("Type").text
        if msgtype == "text":
            save_text(req)
            re_text(req)


def save_text(req):
    if req.raw_post_data:
        xml = ET.fromstring(req.raw_post_data)
        content = xml.find("Content").text
        fromUserName = xml.find("ToUserName").text
        toUserName = xml.find("FromUserName").text
        postTime = str(int(time.time()))

    else:
        return HttpResponse("Invalid Request")


def re_text(req):
    xml = ET.fromstring(req.raw_post_data)
    content = xml.find("Content").text
    fromUserName = xml.find("ToUserName").text
    toUserName = xml.find("FromUserName").text
    postTime = str(int(time.time()))
    reply = """<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    <FuncFlag>0</FuncFlag>
                </xml>"""
    if content == "Hello2BizUser":
        return HttpResponse(reply % (toUserName, fromUserName, postTime, "查询成绩,更多功能开发中..."))
    else:
        pass