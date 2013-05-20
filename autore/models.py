# coding=utf-8
from django.db import models

# Create your models here.
## coding=utf-8
from django.contrib import admin

class KeywordsList(models.Model):
    cKeywords = models.CharField(max_length=20,  verbose_name=u'自动回复关键词')

    lMsgType = (('text',  u'文本内容'), ('news',  u'图文内容'), ('music', u'音乐内容'), )
    cMsgType = models.CharField(max_length=10,  verbose_name=u'消息类型', choices=lMsgType)

    lEventType = (('subscribe', u'关注'), ('unsubscribe', u'取消关注'), )
    cEventType = models.CharField(max_length=10, verbose_name=u'', blank=True, choices=lEventType)

    cContent = models.TextField(null=True, blank=True, verbose_name=u'文本内容')

    lArticleCount = ((u'1条',  1), (u'2条', 2), (u'3条',  3), (u'4条',  4), )
    cArticleCount = models.IntegerField(max_length=1, null=True,  blank=True, verbose_name=u'图文条数',
                                        choices=lArticleCount)
    cTitle1 = models.CharField(max_length=50, blank=True, verbose_name=u'图文1标题')
    cDescription1 = models.CharField(max_length=100, blank=True, verbose_name=u'图文1描述')
    cPicUrl1 = models.CharField(max_length=200, blank=True, verbose_name=u'图文1图片')
    cUrl1 = models.CharField(max_length=200, blank=True, verbose_name=u'图文1链接')
    cTitle2 = models.CharField(max_length=50, blank=True, verbose_name=u'图文2标题')
    cDescription2 = models.CharField(max_length=100, blank=True, verbose_name=u'图文2描述')
    cPicUrl2 = models.CharField(max_length=200, blank=True, verbose_name=u'图文2图片')
    cUrl2 = models.CharField(max_length=200, blank=True, verbose_name=u'图文2链接')
    cTitle3 = models.CharField(max_length=50, blank=True, verbose_name=u'图文3标题')
    cDescription3 = models.CharField(max_length=100, blank=True, verbose_name=u'图文3描述')
    cPicUrl3 = models.CharField(max_length=200, blank=True, verbose_name=u'图文3图片')
    cUrl3 = models.CharField(max_length=200, blank=True, verbose_name=u'图文3链接')
    cTitle4 = models.CharField(max_length=50, blank=True, verbose_name=u'图文4标题')
    cDescription4 = models.CharField(max_length=100, blank=True, verbose_name=u'图文4描述')
    cPicUrl4 = models.CharField(max_length=200, blank=True, verbose_name=u'图文4图片')
    cUrl4 = models.CharField(max_length=200, blank=True, verbose_name=u'图文4链接')

    cTitle = models.CharField(max_length=50, blank=True, verbose_name=u'音乐标题')
    cDescription = models.CharField(max_length=100, blank=True, verbose_name=u'音乐描述')
    cMusicUrl = models.CharField(max_length=200, blank=True, verbose_name=u'音乐链接')
    cHQMusicUrl = models.CharField(max_length=200, blank=True, verbose_name=u'音乐高品质链接')

    class Meta:
        verbose_name = '关键词管理'
        verbose_name_plural = '关键词管理'


class KeywordsListAdmin(admin.ModelAdmin):
    list_display = ('cKeywords', 'cMsgType', 'cContent')
    search_fields = ('cKeywords', )
    list_filter = ('cMsgType',)
    ordering = ('cKeywords', )

    #fields = ('title', 'authors', 'publisher', 'publication_date')
    fieldsets = [(None, {'fields': ['cKeywords', 'cMsgType']}),
                 (u'文本内容', {'fields': ['cContent'], 'classes': ['collapse']}),
                 (u'图文内容', {'fields': ['cArticleCount',
                                'cTitle1', 'cDescription1', 'cPicUrl1', 'cUrl1',
                                'cTitle2', 'cDescription2', 'cPicUrl2', 'cUrl2',
                                'cTitle3', 'cDescription3', 'cPicUrl3', 'cUrl3',
                                'cTitle4', 'cDescription4', 'cPicUrl4', 'cUrl4', ],
                                'classes': ['collapse']}),
                 (u'音乐内容', {'fields': ['cTitle', 'cDescription', 'cMusicUrl', 'cHQMusicUrl'],
                                'classes': ['collapse']}), ]


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

    class Meta:
        verbose_name = '消息查询'
        verbose_name_plural = '消息查询'


class MsgListAdmin(admin.ModelAdmin):
    list_display = ('cFromUserName', 'cCreateTime', 'cContent', )
    search_fields = ('cContent', 'cFromUserName', )
    list_filter = ('cCreateTime', )
    ordering = ('-cCreateTime', )


class KeywordsListResource(models.Model):
    lFileClass = (('Pic', u'图片'), ('Mp3', u'音频'),)
    cFileClass = models.CharField(max_length=10, verbose_name=u'类别', choices=lFileClass)
    cFilename = models.CharField(max_length=150, verbose_name=u'文件名')
    cFile_img = models.ImageField(upload_to='update/%Y/%m/%d', null=True,  blank=True, verbose_name=u'图片上传')
    cFile_mp3 = models.FileField(upload_to='update/%Y/%m/%d', null=True,  blank=True, verbose_name=u'音频上传')
    cCreateTime = models.DateTimeField(verbose_name=u'上传时间')

    class Meta:
        verbose_name = '资源管理'
        verbose_name_plural = '资源管理'


class KeywordsListResourceAdmin(admin.ModelAdmin):
    list_display = ('cFilename', 'cCreateTime', 'cFileClass', )
    search_fields = ('cFilename', 'cFileClass')
    list_filter = ('cCreateTime', )
    ordering = ('-cCreateTime', )


admin.site.register(MsgList, MsgListAdmin)
admin.site.register(KeywordsList, KeywordsListAdmin)
admin.site.register(KeywordsListResource, KeywordsListResourceAdmin)