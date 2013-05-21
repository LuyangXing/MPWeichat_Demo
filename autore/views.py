# Create your views here.
# coding=utf-8
from django.http import HttpResponse
import hashlib
import time
import datetime
from xml.etree import ElementTree as ET
#微信嗲用处理部分

from weixin.autore.models import MsgList
from weixin.autore.models import KeywordsList
from weixin.autore.models import NewsList
#引用数据层模块

from django.template import loader, Context
#调用模版层


def handle_request(request):
    if request.method == 'GET':
        response = HttpResponse(check_signature(request), content_type="text/plain")
        return response
    elif request.method == 'POST':
        response = HttpResponse(response_msg(request), content_type="application/xml")
        return response
    else:
        return HttpResponse("Invalid Request")
    #微信模块的第一部分，判断并解析检查签名和回复信息部分


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
    #微信模块的第二部分，签名分析，通过加密对比，返回验证信息


def response_msg(request):
    #微信模块的第三部分，提取服务器传来的信息
    if request.raw_post_data:
        xml = ET.fromstring(request.raw_post_data)
        fromUserName = xml.find("ToUserName").text
        toUserName = xml.find("FromUserName").text
        msgtype = xml.find("MsgType").text
        postTime = str(int(time.time()))
        #提取部分公用信息
        reply_text = """<xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[%s]]></MsgType>
                        <Content><![CDATA[%s]]></Content>
                        <FuncFlag>0</FuncFlag>
                    </xml>"""

        reply_news = """<xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
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
        #声明各种返回信息模版
        if msgtype == 'text':
            content = xml.find("Content").text
            data = MsgList(cToUserName=toUserName, cFromUserName=fromUserName,
                           cCreateTime=datetime.datetime.now(), cMsgType=msgtype, cContent=content)
            data.save()
            #数据层 存储一条新数据
            try:
                #验证数据层回复部分
                kwlobjs = KeywordsList.objects.filter(cKeywords=content)
                #数据层 提取筛选信息
                for kwlobj in kwlobjs:
                    #数据层 循环提取单条信息
                    if kwlobj.cMsgType == 'text':
                        return HttpResponse(reply_text % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                          kwlobj.cContent))
                    elif kwlobj.cMsgType == 'news':
                        return HttpResponse(reply_news % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                          kwlobj.cArticleCount,
                                                          kwlobj.cTitle1, kwlobj.cDescription1,
                                                          kwlobj.cPicUrl1, kwlobj.cUrl1,
                                                          kwlobj.cTitle2, kwlobj.cDescription2,
                                                          kwlobj.cPicUrl2, kwlobj.cUrl2,
                                                          kwlobj.cTitle3, kwlobj.cDescription3,
                                                          kwlobj.cPicUrl3, kwlobj.cUrl3,
                                                          kwlobj.cTitle4, kwlobj.cDescription4,
                                                          kwlobj.cPicUrl4, kwlobj.cUrl4))
                    elif kwlobj.cMsgType == 'music':
                        return HttpResponse(reply_music % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                           kwlobj.cTitle, kwlobj.cDescription, kwlobj.cMusicUrl,
                                                           kwlobj.cHQMusicUrl))
                    else:
                        pass
            except KeywordsList.DoesNotExist:
                pass

        elif msgtype == 'event':
            event = xml.find("Event").text
            if event == 'subscribe':
                try:
                    kwlobjs = KeywordsList.objects.filter(cEventType='subscribe')
                    for kwlobj in kwlobjs:
                        if kwlobj.cMsgType == 'text':
                            return HttpResponse(reply_text % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                              kwlobj.cContent))
                        elif kwlobj.cMsgType == 'news':
                            return HttpResponse(reply_news % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                              kwlobj.cArticleCount,
                                                              kwlobj.cTitle1, kwlobj.cDescription1,
                                                              kwlobj.cPicUrl1, kwlobj.cUrl1,
                                                              kwlobj.cTitle2, kwlobj.cDescription2,
                                                              kwlobj.cPicUrl2, kwlobj.cUrl2,
                                                              kwlobj.cTitle3, kwlobj.cDescription3,
                                                              kwlobj.cPicUrl3, kwlobj.cUrl3,
                                                              kwlobj.cTitle4, kwlobj.cDescription4,
                                                              kwlobj.cPicUrl4, kwlobj.cUrl4))
                        elif kwlobj.cMsgType == 'music':
                            return HttpResponse(reply_music % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                               kwlobj.cTitle, kwlobj.cDescription, kwlobj.cMusicUrl,
                                                               kwlobj.cHQMusicUrl))
                        else:
                            pass
                except KeywordsList.DoesNotExist:
                    pass
            elif event == 'unsubscribe':
                try:
                    kwlobjs = KeywordsList.objects.filter(cEventType='unsubscribe')
                    for kwlobj in kwlobjs:
                        if kwlobj.cMsgType == 'text':
                            return HttpResponse(reply_text % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                              kwlobj.cContent))
                        elif kwlobj.cMsgType == 'news':
                            return HttpResponse(reply_news % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                              kwlobj.cArticleCount,
                                                              kwlobj.cTitle1, kwlobj.cDescription1,
                                                              kwlobj.cPicUrl1, kwlobj.cUrl1,
                                                              kwlobj.cTitle2, kwlobj.cDescription2,
                                                              kwlobj.cPicUrl2, kwlobj.cUrl2,
                                                              kwlobj.cTitle3, kwlobj.cDescription3,
                                                              kwlobj.cPicUrl3, kwlobj.cUrl3,
                                                              kwlobj.cTitle4, kwlobj.cDescription4,
                                                              kwlobj.cPicUrl4, kwlobj.cUrl4))
                        elif kwlobj.cMsgType == 'music':
                            return HttpResponse(reply_music % (toUserName, fromUserName, postTime, kwlobj.cMsgType,
                                                               kwlobj.cTitle, kwlobj.cDescription, kwlobj.cMusicUrl,
                                                               kwlobj.cHQMusicUrl))
                        else:
                            pass
                except KeywordsList.DoesNotExist:
                    pass
            else:
                return HttpResponse("Invalid Request")

        else:
            return HttpResponse("Invalid Request")

    else:
        return HttpResponse("Invalid Request")


def news_list(request):
    #显示新闻内容信息
    cid = request.GET.get('cid')
    anews = NewsList.objects.get(nID=cid)
    #数据层 提取单条信息
    t = loader.get_template("news.html")
    c = Context({'anews': anews})
    return HttpResponse(t.render(c))
    #这个部分需要配合 urls templates 实现代码使用
    #以 www.xxx.com/news?nid=1& 形式传参，以request.GET.get形式接收参数


# #  reference
