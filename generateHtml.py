import time
import os
try:
	spec = input("Input:")
	print(spec)
	f = open(str(spec)+"email.html","w")
	print(spec)
	text = "<p>&nbsp;&nbsp;<img src=\"http://100.35.205.75:23653/"+str(spec)+"\" alt=\"http://100.35.205.75:23653/"+str(spec)+" width=\"1\" height=\"1\" /></p>"
	print(text)
	f.write(text)
	f.close()
	file = str(spec)+"email.html"
	base = os.path.splittext(file)[0]
	os.rename(file, base+'.html')
	time.sleep(2)
except:
	time.sleep(1)
