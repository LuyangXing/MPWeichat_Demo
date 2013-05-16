from django.db import models

# Create your models here.
from django.contrib import admin


class KeywordsList(models.Model):
    cKeywords = models.CharField(max_length=20)

    cCreateTime = models.DateTimeField()
    #cMsgType = (('F', 'Female'), ('M', 'Male'),)

    #cContent = models.CharField(max_length=300, blank=True, verbose_name='e-mail')

    cTitle = models.CharField(max_length=50)
    cDescription = models.CharField(max_length=100)
    cMusicUrl = models.CharField(max_length=200)
    cHQMusicUrl = models.CharField(max_length=200)

    cArticleCount = models.IntegerField(max_length=1)
    cTitle1 = models.CharField(max_length=50)
    cDescription1 = models.CharField(max_length=100)
    cPicUrl1 = models.CharField(max_length=200)
    cUrl1 = models.CharField(max_length=200)
    cTitle2 = models.CharField(max_length=50)
    cDescription2 = models.CharField(max_length=100)
    cPicUrl2 = models.CharField(max_length=200)
    cUrl2 = models.CharField(max_length=200)
    cTitle3 = models.CharField(max_length=50)
    cDescription3 = models.CharField(max_length=100)
    cPicUrl3 = models.CharField(max_length=200)
    cUrl3 = models.CharField(max_length=200)


class MsgList(models.Model):
    cToUserName = models.CharField(max_length=50)
    cFromUserName = models.CharField(max_length=50)
    cCreateTime = models.DateTimeField()
    cMsgType = models.CharField(max_length=20)

    cEvent = models.CharField(max_length=10)

    cContent = models.CharField(max_length=300)

    cLocation_X = models.CharField(max_length=10)
    cLocation_Y = models.CharField(max_length=10)
    cScale = models.CharField(max_length=10)
    cLabel = models.CharField(max_length=50)


class KeywordsListAdmin(admin.ModelAdmin):
    list_display = ('cKeywords', 'cMsgType')
    #search_fields = ('first_name', 'last_name')
    #list_filter = ('publication_date',)
    #ordering = ('-publication_date',)

    #fields = ('title', 'authors', 'publisher', 'publication_date')
    #fieldsets = [(None,{'fields': ['question']}),
    # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})]


class MsgListAdmin(admin.ModelAdmin):
    list_display = ('cToUserName', 'cCreateTime', 'cContent')


admin.site.register(KeywordsList, KeywordsListAdmin)
#admin.site.register(MsgList, MsgListAdmin)