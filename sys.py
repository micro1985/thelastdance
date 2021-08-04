import platform,socket,getpass

ost = platform.uname()
hst = socket.gethostname()
usr = getpass.getuser()

file = open("index.html", "w")
file.write("<html>\nOperating system info:"+" "+str(ost)+"\n<br>"+"Hostname:"+" "+str(hst)+"\n<br>"+"Username: "+str(usr)+"\n</html>")
file.close()
