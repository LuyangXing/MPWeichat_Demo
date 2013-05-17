# coding=utf-8
from django.db import models

# Create your models here.
## coding=utf-8
from django.contrib import admin


class KeywordsList(models.Model):
    cKeywords = models.CharField(max_length=20,  verbose_name=u'自动回复关键词')

    lMsgType = ((u'文本内容',  'text'), (u'音乐内容', 'music'), (u'新闻内容',  'news'), )
    cMsgType = models.CharField(max_length=10,  verbose_name=u'消息类型', choices=lMsgType)

    cContent = models.CharField(max_length=300, blank=True, verbose_name=u'文本内容')

    cTitle = models.CharField(max_length=50, blank=True, verbose_name=u'音乐标题')
    cDescription = models.CharField(max_length=100, blank=True, verbose_name=u'音乐描述')
    cMusicUrl = models.CharField(max_length=200, blank=True, verbose_name=u'音乐链接')
    cHQMusicUrl = models.CharField(max_length=200, blank=True, verbose_name=u'音乐高品质链接')

    lArticleCount = ((u'1条',  1), (u'2条', 2), (u'3条',  3), (u'4条',  4), )
    cArticleCount = models.IntegerField(max_length=1, null=True,  blank=True, verbose_name=u'新闻条数' , choices=lArticleCount)
    cTitle1 = models.CharField(max_length=50, blank=True, verbose_name=u'新闻1标题')
    cDescription1 = models.CharField(max_length=100, blank=True, verbose_name=u'新闻1描述')
    cPicUrl1 = models.CharField(max_length=200, blank=True, verbose_name=u'新闻1图片')
    cUrl1 = models.CharField(max_length=200, blank=True, verbose_name=u'新闻1链接')
    cTitle2 = models.CharField(max_length=50, blank=True, verbose_name=u'新闻2标题')
    cDescription2 = models.CharField(max_length=100, blank=True, verbose_name=u'新闻2描述')
    cPicUrl2 = models.CharField(max_length=200, blank=True, verbose_name=u'新闻2图片')
    cUrl2 = models.CharField(max_length=200, blank=True, verbose_name=u'新闻2链接')
    cTitle3 = models.CharField(max_length=50, blank=True, verbose_name=u'新闻3标题')
    cDescription3 = models.CharField(max_length=100, blank=True, verbose_name=u'新闻3描述')
    cPicUrl3 = models.CharField(max_length=200, blank=True, verbose_name=u'新闻3图片')
    cUrl3 = models.CharField(max_length=200, blank=True, verbose_name=u'新闻3链接')
    cTitle4 = models.CharField(max_length=50, blank=True, verbose_name=u'新闻4标题')
    cDescription4 = models.CharField(max_length=100, blank=True, verbose_name=u'新闻4描述')
    cPicUrl4 = models.CharField(max_length=200, blank=True, verbose_name=u'新闻4图片')
    cUrl4 = models.CharField(max_length=200, blank=True, verbose_name=u'新闻4链接')


class MsgList(models.Model):
    cToUserName = models.CharField(max_length=50, verbose_name=u'公司ID')
    cFromUserName = models.CharField(max_length=50, verbose_name=u'用户ID')
    cCreateTime = models.DateTimeField(verbose_name=u'消息日期')
    cMsgType = models.CharField(max_length=20, verbose_name=u'消息类型')

    cEvent = models.CharField(max_length=10, blank=True, verbose_name=u'事件类别')

    cContent = models.CharField(max_length=300, blank=True, verbose_name=u'文本内容')

    cLocation_X = models.CharField(max_length=10, blank=True, verbose_name=u'坐标纬度')
    cLocation_Y = models.CharField(max_length=10, blank=True, verbose_name=u'坐标经度')
    cScale = models.CharField(max_length=10, blank=True, verbose_name=u'缩放级别')
    cLabel = models.CharField(max_length=50, blank=True, verbose_name=u'位置信息')


class KeywordsListAdmin(admin.ModelAdmin):
    list_display = ('cKeywords', 'cMsgType', )
    search_fields = ('cKeywords', )
    #list_filter = ('publication_date',)
    ordering = ('cKeywords', )

    #fields = ('title', 'authors', 'publisher', 'publication_date')
    #fieldsets = [(None,{'fields': ['question']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})]


class MsgListAdmin(admin.ModelAdmin):
    list_display = ('cToUserName', 'cCreateTime', 'cContent', )
    search_fields = ('cKeywords', 'cContent', )
    ordering = ('-cCreateTime', )


admin.site.register(KeywordsList, KeywordsListAdmin)
admin.site.register(MsgList, MsgListAdmin)