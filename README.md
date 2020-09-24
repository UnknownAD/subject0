# subject0

here's some tricks:


to run a process in the background: 
xterm -e "firefox & sleep 5s";echo done
note: you must add an echo text because it
 must return a text output

seek for priviliges escalation weak points:
find / -perm /4000 2>/dev/null

restore a lost session when you are stucking on a shell
bug

go to the main command line and type :

restore <sessid>

to list all the active sessions: list
