# coding=utf-8
from django.db import models

# Create your models here.
from django.contrib import admin
#引用admin界面
from tinymce.models import HTMLField
#引用tinymce模块,
#需要是用 manage.py syncdb 生成目录


class KeywordsList(models.Model):
    cKeywords = models.CharField(max_length=20,  verbose_name=u'自动回复关键词')
    cKeywordsDesc = models.CharField(max_length=50, verbose_name=u'关键词描述', blank=True)

    lMsgType = (('text',  u'文本内容'), ('news',  u'图文内容'), ('music', u'音乐内容'), )
    cMsgType = models.CharField(max_length=10,  verbose_name=u'消息类型', choices=lMsgType)
    #该部分使用模式为参考输入项目,先以元组形式赋值，以choices形式调用，保存值为前者，后者为显示值

    lEventType = (('subscribe', u'关注'), ('unsubscribe', u'取消关注'), )
    cEventType = models.CharField(max_length=20, verbose_name=u'事件类型', blank=True, choices=lEventType)

    cContent = models.TextField(null=True, blank=True, verbose_name=u'文本内容')

    lArticleCount = (('1',  u'1条'), ('2', u'2条'), ('3', u'3条'), ('4', u'4条'), )
    cArticleCount = models.CharField(max_length=1,  blank=True, verbose_name=u'图文条数',
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
        verbose_name = '关键词'
        verbose_name_plural = '关键词'
        #此部分为汉化上级菜单中的文字显示


class KeywordsListAdmin(admin.ModelAdmin):
    list_display = ('cKeywords', 'cKeywordsDesc', 'cMsgType', 'cContent', )
    #此处为上级列表显示哪些字段
    search_fields = ('cKeywords', 'cKeywordsDesc', )
    #此处为搜索框中可以搜索到哪些内容
    list_filter = ('cKeywordsDesc', )
    #此处为右侧列表搜索框中列表形式显示筛选项目
    ordering = ('cKeywords', )
    #此处为排序规则，加-则为倒叙排列

    #fields = ('title', 'authors', 'publisher', 'publication_date')
    fieldsets = [(None, {'fields': ['cKeywords', 'cKeywordsDesc', 'cMsgType', 'cEventType']}),
                 (u'文本内容', {'fields': ['cContent'], 'classes': ['collapse']}),
                 (u'图文内容', {'fields': ['cArticleCount',
                                'cTitle1', 'cDescription1', 'cPicUrl1', 'cUrl1',
                                'cTitle2', 'cDescription2', 'cPicUrl2', 'cUrl2',
                                'cTitle3', 'cDescription3', 'cPicUrl3', 'cUrl3',
                                'cTitle4', 'cDescription4', 'cPicUrl4', 'cUrl4', ],
                                'classes': ['collapse']}),
                 (u'音乐内容', {'fields': ['cTitle', 'cDescription', 'cMusicUrl', 'cHQMusicUrl'],
                                'classes': ['collapse']}), ]
    #此处为填表页字段显示方式规范化，None行为主值相关字段，下面部分为其他值，classes部分为隐藏


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


class ResourceList(models.Model):
    cID = models.AutoField(primary_key=True, verbose_name=u'资源ID')
    lFileClass = (('Pic', u'图片'), ('Mp3', u'音频'),)
    cFileClass = models.CharField(max_length=10, verbose_name=u'类别', choices=lFileClass)
    cFilename = models.CharField(max_length=150, verbose_name=u'文件名')
    cFile_img = models.ImageField(upload_to='update/%Y/%m/%d', null=True,  blank=True, verbose_name=u'图片上传')
    cFile_mp3 = models.FileField(upload_to='update/%Y/%m/%d', null=True,  blank=True, verbose_name=u'音频上传')
    #文件上传字段，需要制定上传目录，默认以media目录为准，可以通过时间戳格式化存储目录
    cFullUrl = models.CharField(max_length=50, verbose_name=u'文件链接',
                                default='http://123.196.123.20/media/', help_text='帮助信息')
    #这里为默认值，可以免去频繁输入的问题； 帮助信息部分是显示在字段之下的帮助说明

    class Meta:
        verbose_name = '资源'
        verbose_name_plural = '资源'


class ResourceListAdmin(admin.ModelAdmin):
    list_display = ('cID', 'cFilename', 'cFileClass', 'cFullUrl', 'cFile_img', )
    search_fields = ('cFilename', )
    list_filter = ('cFileClass', )
    ordering = ('-cID', )


class NewsList(models.Model):
    nID = models.AutoField(primary_key=True, verbose_name=u'新闻ID')
    nTitle = models.CharField(max_length=50, verbose_name=u'新闻标题')
    nDesc = models.CharField(max_length=100, verbose_name=u'描述', blank=True)
    nTime = models.DateTimeField(verbose_name=u'创建时间')
    nCon = HTMLField(verbose_name=u'正文')
    #调用了tinymce模块的自定义段
    nFullUrl = models.CharField(max_length=50, verbose_name=u'文件链接',
                                default='http://123.196.123.20/news?cid=',
                                help_text='帮助信息')

    class Meta:
        verbose_name = '新闻文章'
        verbose_name_plural = '新闻文章'


class NewsListAdmin(admin.ModelAdmin):
    list_display = ('nFullUrl', 'nID', 'nTitle', 'nTime', 'nFullUrl', )
    search_fields = ('nTitle', 'nDesc', )
    list_filter = ('nTime', )
    ordering = ('-nID', )


admin.site.register(MsgList, MsgListAdmin)
admin.site.register(KeywordsList, KeywordsListAdmin)
admin.site.register(ResourceList, ResourceListAdmin)
admin.site.register(NewsList, NewsListAdmin)
#此处为注册admin模块，需要模块和模块规范化两个部分一起注册才能生效