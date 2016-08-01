# -*- coding: UTF-8 -*-
# from flask import Flask,request,url_for
from flask import Module,render_template,jsonify, redirect, request,session,g
 
from time import sleep
import httplib
import json
from src.agentconfig import *
import requests
import urllib2
import logging

# logging.basicConfig(level =logging.DEBUG)
appmanages = Module(__name__)
# 查看应用日志
@appmanages.route('/guirenAgent/appLogs/preview',methods = ['POST'])
def appLogs():
    app_filename = request.json['app_filename']
    log_path = request.json['log_path']
    log_file = request.json['log_file']
    status = request.json['status']
    logs = ioFile(status, log_path, app_filename, log_file)
    print logs
    return jsonify(data = logs)
# 下载应用日志
def upAppLogs():
    return 'upApplogs'
#下载应用包
def upAppPackage(url,appname):
    local_filename = url.split('=')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(fileDownloadPath+'/'+appname+'/'+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return 'upAppPackage'
#读取文件流
def filestream(status,filepath,appfilename,logfile):
    i=0
    linecount=0
    while linecount-i==0:
        sleep(5)
        try:
            files = open(filepath+'/'+appfilename+'/'+logfile)
            f = files.readlines()
            linecount=len(f)
            c = linecount-i
            i = linecount
            print logfile
            if not c==0:
                for line in f[(linecount-c):len(f)]:
                     print line
                     yield line
# status为1退出文件流         
            if status==1:
                f.close()
                return 
        except StopIteration, e:
            f.close()
            return       
def ioFile(status,filepath,appfilename,logfile):
    for i in filestream(status,filepath,appfilename,logfile):
# 数据传参
#         urllib2.urlopen('http://127.0.0.1/iCloud/icloudAjax/accepteMsg.dox?msg=%s' %(i)).read()
#         print i
        print type(i)

if __name__ == '__main__':
    
    print 'appcontroller'