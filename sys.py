import platform,socket,getpass
from datetime import datetime

ost = platform.uname()
hst = socket.gethostname()
usr = getpass.getuser()
dtm = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

file = open("index.html", "w")
file.write("<html>\n<h1><font color='green'><center>THE LAST DANCE</center></font></h1>\nOperating system info:"+" "+str(ost)+"\n<br>"+"Hostname:"+" "+str(hst)+"\n<br>"+"Username: "+str(usr)+"\n<br>"+"Time on server: "+str(dtm)+"\n</html>")
file.close()
