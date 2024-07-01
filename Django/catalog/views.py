from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
import json
from .models import Catalog,Users,Labs,Pcs

# Create your views here.
"""
//genral post request (this is an example, it doesn't work in this app)
let data = {title:"ali",description:"wowwwwww",completed:true}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrfToken = getCookie('csrftoken');
fetch("http://127.0.0.1:8000/post",{
  method: 'POST',
  headers: {'X-CSRFToken': csrfToken},
  body: JSON.stringify(data),
}).then(data=>data.json()).then(data=>console.log(data))
"""

# fetch("http://127.0.0.1:8000/get/users").then(data=>data.json()).then(data=>console.log(data))
def getUsers(request):
    users = list(Users.objects.all().values("name","jobTitle","userName"))
    return HttpResponse(json.dumps(users))

# fetch("http://127.0.0.1:8000/get/user?searchTerm=Samy").then(data=>data.json()).then(data=>console.log(data))
def getUser(request):
    x = request.GET.get("searchTerm","NULL")
    users = list(Users.objects.filter(Q(name=x)|Q(email=x)|Q(jobTitle=x)|Q(userName=x)).values("name","jobTitle","userName","password"))
    return HttpResponse(json.dumps(users))


"""
let userData = {name:"Ahmed Ali",email:"ahmedahmed999@gmail.com",jobTitle:"tech lead",userName:"Abdo the ghost",password:"Elgamed"}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrfToken = getCookie('csrftoken');
fetch("http://127.0.0.1:8000/post/user",{
  method: 'POST',
  headers: {'X-CSRFToken': csrfToken},
  body: JSON.stringify(userData),
}).then(data=>data.json()).then(data=>console.log(data))
"""

def postUser(request):
    post_data = json.loads(request.body.decode("utf-8"))
    name = post_data.get("name", "NULL")
    email = post_data.get("email", "NULL")
    jobTitle = post_data.get("jobTitle", "NULle")
    userName = post_data.get("userName", "NULL")
    password = post_data.get("password", "NULL")

    Users.objects.create(name=name,email=email,jobTitle=jobTitle,userName=userName,password=password)
    return HttpResponse(json.dumps({"status": 200}))
















# fetch("http://127.0.0.1:8000/get/labs").then(data=>data.json()).then(data=>console.log(data))
def getLabs(request):
    labs = list(Labs.objects.all().values())
    return HttpResponse(json.dumps(labs))


#  fetch("http://127.0.0.1:8000/get/lab?pcId=20").then(data=>data.json()).then(data=>console.log(data))
#  fetch("http://127.0.0.1:8000/get/lab?labId=6").then(data=>data.json()).then(data=>console.log(data))
#  fetch("http://127.0.0.1:8000/get/lab").then(data=>data.json()).then(data=>console.log(data))
def getLabById(request):
    x = request.GET.get('labId',0)
    y = request.GET.get('pcId',0)
    labs =0
    if x != 0:
        labs = list(Labs.objects.filter(id=x).values())
    elif y != 0 :
        labs = list(Labs.objects.filter( id=list(Pcs.objects.filter(id=y).values())[0].get("labId") ).values())
    else:
        labs = list(Labs.objects.all().values())
    return HttpResponse(json.dumps(labs))

"""
let labData = {labName:"lab 9", labBuilding:"3",labFNumber:3,labPcsCount:40,labChairsCount:50,labStatus:"working"}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrfToken = getCookie('csrftoken');
fetch("http://127.0.0.1:8000/post/lab",{
  method: 'POST',
  headers: {'X-CSRFToken': csrfToken},
  body: JSON.stringify(labData),
}).then(data=>data.json()).then(data=>console.log(data))
"""
def postLab(request):
    post_data = json.loads(request.body.decode("utf-8"))
    labName = post_data.get("labName", "NULL")
    labBuilding = post_data.get("labBuilding", "NULL")
    labFNumber = post_data.get("labFNumber", 0)
    labPcsCount = post_data.get("labPcsCounts", 0)
    labChairsCount = post_data.get("labChairsCount", 0)
    labStatus = post_data.get("labStatus", "not working")
    Labs.objects.create(labName=labName,labBuilding=labBuilding,labFNumber=labFNumber,
    labPcsCount=labPcsCount,labChairsCount=labChairsCount,labStatus=labStatus)
    labs = list(Labs.objects.all().values())
    return HttpResponse(json.dumps(labs))


"""
let labData = {labId:2,labName:"lab Maged", labBuilding:"5",labFNumber:1,labPcsCount:44,labChairsCount:25,labStatus:"working"}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrfToken = getCookie('csrftoken');
fetch("http://127.0.0.1:8000/update/lab",{
  method: 'POST',
  headers: {'X-CSRFToken': csrfToken},
  body: JSON.stringify(labData),
}).then(data=>data.json()).then(data=>console.log(data))
"""
def updateLab(request):
    post_data = json.loads(request.body.decode("utf-8"))
    labId = post_data.get("labId",0)
    labName = post_data.get("labName","null")
    labBuilding = post_data.get("labBuilding","null")
    labFNumber = post_data.get("labFNumber",0)
    labPcsCount = post_data.get("labPcsCount",0)
    labChairsCount = post_data.get("labChairsCount",0)
    labStatus = post_data.get("labStatus","working")

    Labs.objects.filter(id=labId).update(labName=labName,labBuilding=labBuilding,labFNumber=labFNumber,labPcsCount=labPcsCount,
    labChairsCount=labChairsCount,labStatus=labStatus)

    lab = list(Labs.objects.filter(id=labId).values())
    return HttpResponse(json.dumps(lab))

# fetch("http://127.0.0.1:8000/delete/lab?labId=8").then(data=>data.json()).then(data=>console.log(data))
def deleteLab(request):
    x = request.GET.get('labId',0)
    Labs.objects.filter(id=x).delete()
    return HttpResponse(json.dumps({"status": 200}))












# fetch("http://127.0.0.1:8000/get/pcs?labId=6").then(data=>data.json()).then(data=>console.log(data))
def getPcs(request):
    x = request.GET.get('labId',0)
    pcs = list(Pcs.objects.filter(labId=x).values())
    return HttpResponse(json.dumps(pcs))

# fetch("http://127.0.0.1:8000/get/pc?pcId=20").then(data=>data.json()).then(data=>console.log(data))
def getPc(request):
    x = request.GET.get('pcId',0)
    pcs =0
    if x!=0:
        pcs = list(Pcs.objects.filter(id=x).values())
    else:
        pcs = list(Pcs.objects.all().values())
    return HttpResponse(json.dumps(pcs))

"""
let pcData = {labId:4,pcStatus:"working",comment:"Wubba labba dub dub!"}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrfToken = getCookie('csrftoken');
fetch("http://127.0.0.1:8000/post/pc",{
  method: 'POST',
  headers: {'X-CSRFToken': csrfToken},
  body: JSON.stringify(pcData),
}).then(data=>data.json()).then(data=>console.log(data))
"""
def postPc(request):
    post_data = json.loads(request.body.decode("utf-8"))
    labId = post_data.get("labId", 0)
    pcStatus = post_data.get("pcStatus", "Working")
    comment = post_data.get("comment", "")
    Pcs.objects.create(labId=labId,pcStatus=pcStatus,comment=comment)

    pcs = list(Pcs.objects.filter(labId=labId).values())
    return HttpResponse(json.dumps(pcs))


"""
let pcData = {pcId:18,pcStatus:"working",comment:"the mouse is now fixed!"}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrfToken = getCookie('csrftoken');
fetch("http://127.0.0.1:8000/update/pc",{
  method: 'POST',
  headers: {'X-CSRFToken': csrfToken},
  body: JSON.stringify(pcData),
}).then(data=>data.json()).then(data=>console.log(data))
"""

def updatePc(request):
    post_data = json.loads(request.body.decode("utf-8"))
    pcId = post_data.get("pcId",0)
    labId = post_data.get("labId",list(Pcs.objects.filter(id=pcId).values("labId"))[0].get("labId"))
    newComment = post_data.get("comment","")
    newStatus = post_data.get("pcStatus","working")


    Pcs.objects.filter(id=pcId).update(comment=newComment,pcStatus=newStatus,labId=labId)
    pcs = list(Pcs.objects.filter(id=pcId).values())
    return HttpResponse(json.dumps(pcs))

# fetch("http://127.0.0.1:8000/delete/pc?pcId=36").then(data=>data.json()).then(data=>console.log(data))
def deletePc(request):
    x = request.GET.get('pcId',0)
    Pcs.objects.filter(id=x).delete()
    return HttpResponse(json.dumps({"status": 200}))



