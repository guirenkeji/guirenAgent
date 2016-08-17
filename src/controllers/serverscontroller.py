# -*- coding: UTF-8 -*-
from flask import Module,render_template,jsonify, redirect, request,session,g
from src.agentconfig import *
import logging
import fileinput
import linecache
logging.basicConfig(level =logging.DEBUG)
serversmanages = Module(__name__)

#创建marathon
def createMarathon(count,server_config):
    count = request.json['count']
    server_config = request.json['server_config']
    print  'marathon'
def deleteMarathon(count,id):
    print 'marathon'    
def createHaproxy():
    print 'ha'
def createZookeeper():
    print 'ha'    
#日志文件查找
@serversmanages.route('/guirenAgent/servers/logs/preview',methods = ['POST'])
def logFileView():
# 日志行数
    logs_con = 0
# 日志列表
    logs_content = []
    logpath = request.json['logpath']
    logfile = request.json['logfile']
# 读取多少行
    linecount = request.json['linecount']
    logging.info(linecount)
    logfileurl = '/'.join((str(logpath),str(logfile)))
#     count = len(open(logfileurl,'rU').readlines())
    f = open(logfileurl,'r').readlines()
# 统计文件总行数
    sumcount = -1
    for sumcount, line in enumerate(open(logfileurl, 'rU')):
        pass
    sumcount += 1
    count = sumcount-linecount
    for line in f[-linecount:]:
        logs_con += 1
        logs_content.append({logs_con:line.strip("\n")})
#         logging.info(logs_content)
        
#     for line in fileinput.input(logfileurl):
#         process(line)
#         filelineno=fileinput.filelineno()
#         num=fileinput.lineno()
#         if num >=count:
#             print line
#     print num 
    return jsonify(data=logs_content)
@serversmanages.route('/guirenAgent/servers/logs/download',methods = ['POST'])
def logFileDownload():
    
    print 'log'