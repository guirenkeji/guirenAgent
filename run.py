# -*- coding: UTF-8 -*- 

from src import create_guirenagent_app
from src.agentconfig import *
import logging
import logging.handlers

app = create_guirenagent_app()

if __name__ == '__main__':
#     formatter = logging.basicConfig(level = logging.DEBUG,
#                         filename = 'guirenAgent.log',
#     
#                           )
#     Rthandler =logging.handlers.RotatingFileHandler('guirenAgent.log',maxBytes=10,backupCount= 2)
#     Rthandler.setFormatter(formatter)
#     app.debug = True
#     app.logger.setLevel(logging.INFO)
    app.run(host= HOST,port=PORT)
