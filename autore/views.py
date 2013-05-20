# Create your views here.
# coding=utf-8
from django.http import HttpResponse
import hashlib
import time
import datetime
from xml.etree import ElementTree as ET

from weixin.autore.models import MsgList
from weixin.autore.models import KeywordsList


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
        fromUserName = xml.find("ToUserName").text
        toUserName = xml.find("FromUserName").text
        msgtype = xml.find("MsgType").text
        postTime = str(int(time.time()))

        reply_text = """<xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[%s]]></MsgType>
                        <Content><![CDATA[%s]]></Content>
                        <FuncFlag>0</FuncFlag>
                    </xml>"""

        reply_news = """<xml>
                        <ToUserName><![CDATA[%s]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[%s]]></MsgType>
                        <ArticleCount>%s</ArticleCount>
                        <Articles>
                            <item>
                                <Title><![CDATA[%s]]></Title>
                                <Description><![CDATA[%s]]></Description>
                                <PicUrl><![CDATA[%s]]></PicUrl>
                                <Url><![CDATA[%s]]></Url>
                            </item>
                            <item>
                                <Title><![CDATA[%s]]></Title>
                                <Description><![CDATA[%s]]></Description>
                                <PicUrl><![CDATA[%s]]></PicUrl>
                                <Url><![CDATA[%s]]></Url>
                            </item>
                            <item>
                                <Title><![CDATA[%s]]></Title>
                                <Description><![CDATA[%s]]></Description>
                                <PicUrl><![CDATA[%s]]></PicUrl>
                                <Url><![CDATA[%s]]></Url>
                            </item>
                            <item>
                                <Title><![CDATA[%s]]></Title>
                                <Description><![CDATA[%s]]></Description>
                                <PicUrl><![CDATA[%s]]></PicUrl>
                                <Url><![CDATA[%s]]></Url>
                            </item>
                        </Articles>
                        <FuncFlag>1</FuncFlag>
                    </xml>"""

        reply_music = """<xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[%s]]></MsgType>
                        <Music>
                            <Title><![CDATA[%s]]></Title>
                            <Description><![CDATA[%s]]></Description>
                            <MusicUrl><![CDATA[%s]]></MusicUrl>
                            <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
                        </Music>
                        <FuncFlag>0</FuncFlag>
                    </xml>"""

        if msgtype == 'text':
            content = xml.find("Content").text
            data = MsgList(cToUserName=toUserName, cFromUserName=fromUserName,
                           cCreateTime=datetime.datetime.now(), cMsgType=msgtype, cContent=content)
            data.save()

            kwlobjs = KeywordsList.objects.filter(cKeywords=content)
            return HttpResponse(reply_text % (toUserName, fromUserName, postTime, 'text', kwlobjs))
            # try:
            #     kwlobjs = KeywordsList.objects.filter(cKeywords=content)
            # except KeywordsList.DoesNotExist:
            #     pass
            # else:
            #     for kwlobj in kwlobjs:
            #         if kwlobj.cMsgType == 'text':
            #             return HttpResponse(reply_text % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
            #                                               kwlobj.cContent))
            #         elif kwlobj.cMsgType == 'news':
            #             return HttpResponse(reply_news % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
            #                                               kwlobj.cArticleCount,
            #                                               kwlobj.cTitle1, kwlobj.cDescription1, kwlobj.cPicUrl1, kwlobj.cUrl1,
            #                                               kwlobj.cTitle2, kwlobj.cDescription2, kwlobj.cPicUrl2, kwlobj.cUrl2,
            #                                               kwlobj.cTitle3, kwlobj.cDescription3, kwlobj.cPicUrl3, kwlobj.cUrl3,
            #                                               kwlobj.cTitle4, kwlobj.cDescription4, kwlobj.cPicUrl4, kwlobj.cUrl4))
            #         elif kwlobj.cMsgType == 'music':
            #             return HttpResponse(reply_music % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
            #                                                kwlobj.cTitle, kwlobj.cDescription, kwlobj.cMusicUrl, kwlobj.cHQMusicUrl))
            #         else:
            #             return HttpResponse("Invalid Request")

        elif msgtype == 'event':
            event = xml.find("Event").text
            if event == 'subscribe':
                try:
                    kwlobjs = KeywordsList.objects.filter(cEvent='subscribe')
                except KeywordsList.DoesNotExist:
                    pass
                else:
                    for kwlobj in kwlobjs:
                        if kwlobj.cMsgType == 'text':
                            return HttpResponse(reply_text % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                              kwlobj.cContent))
                        elif kwlobj.cMsgType == 'news':
                            return HttpResponse(reply_news % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                              kwlobj.cArticleCount,
                                                              kwlobj.cTitle1, kwlobj.cDescription1, kwlobj.cPicUrl1, kwlobj.cUrl1,
                                                              kwlobj.cTitle2, kwlobj.cDescription2, kwlobj.cPicUrl2, kwlobj.cUrl2,
                                                              kwlobj.cTitle3, kwlobj.cDescription3, kwlobj.cPicUrl3, kwlobj.cUrl3,
                                                              kwlobj.cTitle4, kwlobj.cDescription4, kwlobj.cPicUrl4, kwlobj.cUrl4))
                        elif kwlobj.cMsgType == 'music':
                            return HttpResponse(reply_music % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                               kwlobj.cTitle, kwlobj.cDescription, kwlobj.cMusicUrl, kwlobj.cHQMusicUrl))
                        else:
                            return HttpResponse("Invalid Request")

            elif event == 'unsubscribe':
                try:
                    kwlobjs = KeywordsList.objects.filter(cEvent='unsubscribe')
                except KeywordsList.DoesNotExist:
                    pass
                else:
                    for kwlobj in kwlobjs:
                        if kwlobj.cMsgType == 'text':
                            return HttpResponse(reply_text % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                              kwlobj.cContent))
                        elif kwlobj.cMsgType == 'news':
                            return HttpResponse(reply_news % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                              kwlobj.cArticleCount,
                                                              kwlobj.cTitle1, kwlobj.cDescription1, kwlobj.cPicUrl1, kwlobj.cUrl1,
                                                              kwlobj.cTitle2, kwlobj.cDescription2, kwlobj.cPicUrl2, kwlobj.cUrl2,
                                                              kwlobj.cTitle3, kwlobj.cDescription3, kwlobj.cPicUrl3, kwlobj.cUrl3,
                                                              kwlobj.cTitle4, kwlobj.cDescription4, kwlobj.cPicUrl4, kwlobj.cUrl4))
                        elif kwlobj.cMsgType == 'music':
                            return HttpResponse(reply_music % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                               kwlobj.cTitle, kwlobj.cDescription, kwlobj.cMusicUrl, kwlobj.cHQMusicUrl))
                        else:
                            return HttpResponse("Invalid Request")

            else:
                return HttpResponse("Invalid Request")

        # elif msgtype == 'location':
        #     data = MsgList(cToUserName=toUserName, cFromUserName=fromUserName,
        #                    cCreateTime=datetime.datetime.now(), cMsgType=msgtype, cContent=content)
        #     data.save()

        else:
            return HttpResponse("Invalid Request")

    else:
        return HttpResponse("Invalid Request")


# #  reference