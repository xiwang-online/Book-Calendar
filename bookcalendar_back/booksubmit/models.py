from django.db import models

# Create your models here.
class BookSubmit(models.Model):
    

    #提交时间
    date = models.CharField(max_length=200)

    #书名称
    bookname = models.CharField(max_length=200)

    #作者
    author = models.CharField(max_length=200)

    #推荐理由
    introduction = models.TextField(null=True)

    #联系方式
    information = models.TextField(null=True)

    #备注
    remark = models.TextField(null=True)

    #备用1
    spare1 = models.TextField(null=True)

    #备用2
    spare2 = models.TextField(null=True)

