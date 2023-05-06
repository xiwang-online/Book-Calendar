from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import BookSubmit
import json
def booksubmit(request):
    request.params = json.loads(request.body)
    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_submit':
        return listsubmit(request)
    elif action == 'add_submit':
        return addsubmit(request)
    elif action == 'del_submit':
        return delsubmit(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


"""
{
"action":"list_submit"
}
"""
def listsubmit(request):
    if 'usertype' not in request.session:     #判断是否登录
        return JsonResponse({
            'ret': 302,
           })
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = BookSubmit.objects.values()   #获取表记录
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})





"""
{
"action":"add_submit",
"data":{
"date":"2023.2.19.10.05",
"bookname":"弃长安",
"author":"忘了",
"introduction":"有关安史之乱的一本书",
"information":"2292896976",
"remark":"备注",
"spare1":"备用1",
"spare2":"备用2"
}
}
"""
def addsubmit(request):
    """
    if 'usertype' not in request.session:     #判断是否登录
        return JsonResponse({
            'ret': 302,
           })
    """
    info = request.params['data']             #获取数据
    record = BookSubmit.objects.create(
        date = info['date'],
        bookname = info['bookname'],
        author = info['author'],
        introduction = info['introduction'],
        information = info['information'],
        remark = info['remark'],
        spare1 = info['spare1'],
        spare2 = info['spare2'])
    return JsonResponse({'ret': 0, 'id': record.id})


def delsubmit(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['id']
    try:
        todo = BookSubmit.objects.get(id=info)
    except BookSubmit.DoesNotExist:
        return JsonResponse({
            'ret': 1,
        })
    todo.delete()
    return JsonResponse({'ret': 0})


"""
    date = 
    bookname = 
    author = 
    introduction = 
    information = 
    remark = 
    spare1 = 
    spare2 = 
"""
