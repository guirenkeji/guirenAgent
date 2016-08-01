# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, redirect, request,session,g
from src.agentconfig import *

home = Module(__name__)


@home.route('/')
def index():
    return 'hello guirenAgent '
@home.route('/dashboard')
def login():
    if 'username' in session and not session['username'] == None:
        return redirect('/fitnessmanages')
    return render_template('Login.html',
                           title = u'登陆'
                           )
    return redirect('/fitnessmanages')

