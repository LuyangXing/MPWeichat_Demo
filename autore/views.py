# Create your views here.
# coding=utf-8
from django.http import HttpResponse
import hashlib
import time
from xml.etree import ElementTree as ET

from weixin.autore.models import KeywordsList
from weixin.autore.models import MsgList


def handle_request(request):
    if request.method == 'GET':
        response = HttpResponse(check_signature(request), content_type="text/plain")
        return response
    elif request.method == 'POST':
        response = HttpResponse(response_msg(request), content_type="application/xml")
        return response
    else:
        return HttpResponse("Invalid Request")


def check_signature(request):
    token = "wxtoken20130515"
    params = request.GET
    args = [token, params['timestamp'], params['nonce']]
    args.sort()
    if hashlib.sha1("".join(args)).hexdigest() == params['signature']:
        if params.has_key('echostr'):
            return HttpResponse(params['echostr'])
    else:
        return HttpResponse("Invalid Request")


def response_msg(request):
    if request.raw_post_data:
        xml = ET.fromstring(request.raw_post_data)
        content = xml.find("Content").text
        fromUserName = xml.find("ToUserName").text
        toUserName = xml.find("FromUserName").text
        msgtype = xml.find("MsgType").text
        postTime = str(int(time.time()))
        data = MsgList(cToUserName=toUserName, cFromUserName=fromUserName, cCreateTimec=postTime, cMsgType = msgtype)
        data.save()
        reply = """<xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[%s]]></MsgType>
                        <Content><![CDATA[%s]]></Content>
                        <FuncFlag>0</FuncFlag>
                    </xml>"""
        if content == "H2":
            test = "%s,%s,%s,%s,%s" % (toUserName, fromUserName, postTime, msgtype, content)
            return HttpResponse(reply % (toUserName, fromUserName, postTime, msgtype, test))
        else:
            return HttpResponse(reply % (toUserName, fromUserName, postTime, msgtype, "Hello!"))
    else:
        return HttpResponse("Invalid Request")


# #  reference
#
# receive
# {event  subscribe(dy)、unsubscribe(qxdy)}
# <xml><ToUserName><![CDATA[toUser]]></ToUserName>
# <FromUserName><![CDATA[FromUser]]></FromUserName>
# <CreateTime>123456789</CreateTime>
# <MsgType><![CDATA[event]]></MsgType>
# <Event><![CDATA[EVENT]]></Event>
# <EventKey><![CDATA[EVENTKEY]]></EventKey>
# </xml>
# {text}
# <xml>
# <ToUserName><![CDATA[toUser]]></ToUserName>
# <FromUserName><![CDATA[fromUser]]></FromUserName>
# <CreateTime>1348831860</CreateTime>
# <MsgType><![CDATA[text]]></MsgType>
# <Content><![CDATA[this is a test]]></Content>
# <MsgId>1234567890123456</MsgId>
# </xml>
# {location}
# <xml>
# <ToUserName><![CDATA[toUser]]></ToUserName>
# <FromUserName><![CDATA[fromUser]]></FromUserName>
# <CreateTime>1351776360</CreateTime>
# <MsgType><![CDATA[location]]></MsgType>
# <Location_X>23.134521</Location_X>
# <Location_Y>113.358803</Location_Y>
# <Scale>20</Scale>
# <Label><![CDATA[wzxx]]></Label>
# <MsgId>1234567890123456</MsgId>
# </xml>
#
# delivery
# {text}
# <xml>
# <ToUserName><![CDATA[toUser]]></ToUserName>
# <FromUserName><![CDATA[fromUser]]></FromUserName>
# <CreateTime>12345678</CreateTime>
# <MsgType><![CDATA[text]]></MsgType>
# <Content><![CDATA[content]]></Content>
# <FuncFlag>0</FuncFlag>
# </xml>
# {music}
# <xml>
# <ToUserName><![CDATA[toUser]]></ToUserName>
# <FromUserName><![CDATA[fromUser]]></FromUserName>
# <CreateTime>12345678</CreateTime>
# <MsgType><![CDATA[music]]></MsgType>
# <Music>
# <Title><![CDATA[TITLE]]></Title>
# <Description><![CDATA[DESCRIPTION]]></Description>
# <MusicUrl><![CDATA[MUSIC_Url]]></MusicUrl>
# <HQMusicUrl><![CDATA[HQ_MUSIC_Url]]></HQMusicUrl>
# </Music>
# <FuncFlag>0</FuncFlag>
# </xml>
# {news}
# <xml>
# <ToUserName><![CDATA[toUser]]></ToUserName>
# <FromUserName><![CDATA[fromUser]]></FromUserName>
# <CreateTime>12345678</CreateTime>
# <MsgType><![CDATA[news]]></MsgType>
# <ArticleCount>2</ArticleCount>
# <Articles>
# <item>
# <Title><![CDATA[title1]]></Title>
# <Description><![CDATA[description1]]></Description>
# <PicUrl><![CDATA[picurl]]></PicUrl>
# <Url><![CDATA[url]]></Url>
# </item>
# <item>
# <Title><![CDATA[title]]></Title>
# <Description><![CDATA[description]]></Description>
# <PicUrl><![CDATA[picurl]]></PicUrl>
# <Url><![CDATA[url]]></Url>
# </item>
# </Articles>
# <FuncFlag>1</FuncFlag>
# </xml>
