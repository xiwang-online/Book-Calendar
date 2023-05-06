from django.db import models

# Create your models here.

class Book(models.Model):
    #日期、书名、作者、出版日期、一言、简介、作者简介、下载链接、封面、标签、宜

    #日期
    date = models.CharField(max_length=200)

    # 书名称
    bookname = models.CharField(max_length=200)

    # 作者
    author = models.CharField(max_length=200)

    # 出版日期
    bookdate = models.CharField(max_length=200)

    # 一言
    word = models.TextField(null=True)

    #简介
    introduction = models.TextField(null=True)

    #作者简介
    authorintroduction = models.TextField(null=True)

    #下载链接
    downloadlink = models.TextField(null=True)

    #封面链接
    imagelink = models.TextField(null=True)

    #宜
    yi = models.TextField(null=True)

    #标签
    label = models.TextField(null=True)

    #备注
    remark = models.TextField(null=True)

    #备用1
    spare1 = models.TextField(null=True)#这个里面放对应日期的时间戳用于比较，单位：s

    #备用2
    spare2 = models.TextField(null=True)


