import sys

w = "Hostname"
file = open("./index.html","r")
text = file.read()
if w in text:
  print("Good")
  sys.exit(0)
else:
  print("Bad")
  sys.exit(1)
