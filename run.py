# -*- coding: UTF-8 -*- 

from src import create_guirenagent_app
from src.agentconfig import *

app = create_guirenagent_app()

if __name__ == '__main__':
    app.debug = True
    app.run(host= HOST,port=PORT)
