from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book
import json
import time
def bookdate(request):
    request.params = json.loads(request.body)
    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_book':
        return listbook(request)
    elif action == 'add_book':
        return addbook(request)
    elif action == 'del_book':
        return delbook(request)
    elif action =='modify_book':
        return modifybook(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


"""
请求示例，规定了时间time后就写时间，没规定time后就写0
{
"action":"list_book",
"time":0
}
"""
def listbook(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Book.objects.values()   #获取表记录

    """
    先判断ph的值，为0的话发筛选时间后的数据，为日期的话从筛选后的数据中找到对应日期发送，为-1的话判断是否登录，登录了就发，没登陆就不发
    """
    ph = request.params['time']
    if ph!=(-1):
        t = time.time()  #获取当前时间时间戳
        qs = qs.filter(spare1__lte=t)
        if ph:
            qs = qs.filter(date=ph)
        retlist = list(qs)
        return JsonResponse({'ret': 0, 'retlist': retlist})
    else:
        if 'usertype' in request.session:
            retlist = list(qs)
            return JsonResponse({'ret': 0, 'retlist': retlist})
        else:
            return JsonResponse({'ret': 302,})





"""
请求示例：
{
"action":"add_book",
"data":{
        "date" : "2023.5.15",
        "bookname" : "尘埃落定",
        "author" : "阿来",
        "bookdate" : "1998",
        "word" : "任何腐烂的地方都会有新的东西长出。",
        "introduction" : "简介",
        "authorintroduction" : "作者简介",
        "downloadlink" : "下载链接",
        "imagelink" : "封面链接",
        "yi" : "宜",
        "label" : "标签",
        "remark" : "评论",
        "spare1" : "备用1",
        "spare2" : "备用2"
        }
}
"""
def addbook(request):
    
    if 'usertype' not in request.session:     #判断是否登录
        return JsonResponse({
            'ret': 302,
           })
    
    info = request.params['data']             #获取数据
    record = Book.objects.create(
        date = info['date'],
        bookname = info['bookname'],
        author = info['author'],
        bookdate = info['bookdate'],
        word = info['word'],
        introduction = info['introduction'],
        authorintroduction = info['authorintroduction'],
        downloadlink = info['downloadlink'],
        imagelink = info['imagelink'],
        yi = info['yi'],
        label = info['label'],
        remark = info['remark'],
        spare1 = info['spare1'],
        spare2 = info['spare2'])
    return JsonResponse({'ret': 0, 'id': record.id})


def delbook(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['id']
    try:
        todo = Book.objects.get(id=info)
    except Book.DoesNotExist:
        return JsonResponse({
            'ret': 1,
        })
    todo.delete()
    return JsonResponse({'ret': 0})




def modifybook(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    bookid = request.params['id']
    newdata = request.params['newdata']
    print("在")

    try:
        # 根据 id 从数据库中找到相应的客户记录
        book = Book.objects.get(id=bookid)
    except Book.DoesNotExist:
        return {
            'ret': 1,
        }
    if 'date' in newdata:
        book.date = newdata['date']
    if 'bookname' in newdata:
        book.bookname = newdata['bookname']
    if 'author' in newdata:
        book.author = newdata['author']
    if 'bookdate' in newdata:
        book.bookdate = newdata['bookdate']
    if 'word' in newdata:
        book.word = newdata['word']
    if 'introduction' in newdata:
        book.introduction = newdata['introduction']
    if 'authorintroduction' in newdata:
        book.authorintroduction = newdata['authorintroduction']
    if 'downloadlink' in newdata:
        book.downloadlink = newdata['downloadlink']
    if 'imagelink' in newdata:
        book.imagelink = newdata['imagelink']
    if 'yi' in newdata:
        book.yi = newdata['yi']
    if 'label' in newdata:
        book.label = newdata['label']
    if 'remark' in newdata:
        book.remark = newdata['remark']
    if 'spare1' in newdata:
        book.spare1 = newdata['spare1']
    if 'spare2' in newdata:
        book.spare2 = newdata['spare2']

    # 注意，一定要执行save才能将修改信息保存到数据库
    book.save()
    return JsonResponse({'ret': 0})


"""
        date
        bookname
        author
        bookdate
        word
        introduction
        authorintroduction
        downloadlink
        imagelink
        yi
        label
        remark
        spare1
        spare2
"""
