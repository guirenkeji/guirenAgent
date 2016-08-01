import socket
from flask import Flask,request,url_for,jsonify
import httplib
import json
import logging

register = Flask(__name__)
def getHostName():
    hostName = socket.gethostname() 
    hostIp = socket.gethostbyname(hostName) 
    data = hostName+':'+hostIp
    return data
# server注册
def toServerRegister():
    data =getHostName()
    data = {'data':data}
    httpregisterpost(data)
    print "服务注册成功"
httpClient = httplib.HTTPConnection("127.0.0.1",5013, timeout=30)    
def httpregisterpost (params):
#     httpClient = None
    try:
        data = json.dumps(params)
        
        httpClient.request("POST",'/v2/serverclient/register',data,{'Content-Type': 'application/json'})
        response = httpClient.getresponse()
        print response
    
    except Exception, e:
        print e 
#获取server服务下载war文件信息        
@register.route('/v2/client/download',methods=['POST'])  
def clientDownloadFile():
    url = request.json['url']
    appName = request.json['appname']
    
#     clientcontroller.upAppPackage(url,appName)
    print 'd'
