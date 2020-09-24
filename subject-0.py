#!/usr/bin/python3
print ('''
             lol ty googl
             0000000000000
          0000000000000000000   00
       00000000000000000000000000000
      0000000000000000000000000000000
    000000000             0000000000
   00000000               0000000000                           
  0000000                000000000000                     * The God damn shell manager -_-
 0000000               000000000000000                                                    
 000000              000000000  000000
0000000            000000000     000000
000000            000000000      000000
000000          000000000        000000
000000         00000000          000000
000000       000000000           000000
0000000    000000000            0000000
 000000   000000000             000000
 0000000000000000              0000000
  0000000000000               0000000
   00000000000              00000000
   00000000000            000000000
  0000000000000000000000000000000
   00000000000000000000000000000
     000  0000000000000000000
             0000000000000
              @0x00string
         https:github.com/unknownad
''')
import socket
import subprocess
import threading
req=('localhost',9999)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(req)
sock.listen(3)
socks=[]
addrs=[]
threads=[]
allowed_ports=20000
def handle(c):
    global addrs,socks,allowed_ports
    allowed_ports=allowed_ports-1
    target_peer=socks[int(c)]
    print("[-] Starting a new thread .. ")
    title=f"{addrs[int(c)][0]}:{addrs[int(c)]}"
    subprocess.Popen(['xterm','-hold','-T',title,'-e','./demo.sh',str(allowed_ports)])
    __import__('time').sleep(1)
    proxy=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    proxy.connect(('localhost',allowed_ports))
    while True:
        query=proxy.recv(2048)
        if len(query)>0:
            try:
                target_peer.send(query)
                proxy.send(target_peer.recv(2048))
            except Exception as error:
                print(error)
def accept():
    global sock,socks,allowed_ports
    while True:
        
        conn,addr=sock.accept()
        socks.append(conn)
        addrs.append(addr)
        print(f"! New Connection has been established From {addr[0]}:{addr[1]}")
        for en,sock_obj in enumerate(socks):
            if conn==sock_obj:break
        sub_thread=threading.Thread(target=handle,args=str(en))
        sub_thread.start()
        print("$ A new Thread has been started")
        pass
def restore_session(sessid):
    print(f'[+] restore session : {sessid}')
    backup=threading.Thread(target=handle,args=str(sessid))
    backup.start()
def cmd_prompt():
    main_thread=threading.Thread(target=accept)
    main_thread.start()
    while True:
        cmd=input('$ ')
        if cmd=='list':
            sessions=''
            for n,s in enumerate(socks):
                try:
                    s.send(b'hi')
                    sessions=f"{sessions}+${n} {addrs[n][0]} : {addrs[n][1]} \n"
                except:
                    del socks[n]
                    del addrs[n]
            print(sessions)
        if 'restore' in cmd:
            sessid=cmd.replace('restore ','')
            restore_session(sessid)
cmd_prompt()
