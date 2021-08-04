w = "Hostname"
file = open("./index.html","r")
text = file.read()
if w in text:
  print("Good")
else:
  print("Bad")
