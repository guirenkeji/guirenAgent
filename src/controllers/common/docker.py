from docker import Client
from io import BytesIO
def dockerHandle():
    cli = Client(base_url='unix://var/run/docker.sock')
                                           
#     f = BytesIO(dockerFile.dockerfile.encode('utf-8'))        
#     response = [line for line in cli.build(        
#         fileobj=f, rm=True, tag='yourname/volume'  
#     )]                                             
#     response  
#     
    print cli.info()
def dockerFile():
    dockerfile = '''                               
    # Shared Volume                                
    FROM busybox:buildroot-2014.02                 
    MAINTAINER first last, first.last@yourdomain.co
    VOLUME /data                                   
    CMD ["/bin/sh"]                                
    '''                                          

if __name__ == '__main__' :
    dockerHandle()    