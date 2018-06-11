import time
from datetime import datetime as dt


hosts_temp=r"C:\rename\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts";
redirect="127.0.0.1";
websit_list=["www.google.com","www.facebook.com"];
while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,14)<dt.now()<dt(dt.now().year,dtnow().month,dt.now().day):
 		print("Working hours")
		with open(hosts_temp,\r+\) as file:
			content =file.read()
				for website in website_list:
					if website in content:
						pass
					else:
						file.write(redirect+""+website+"\n")	
	else:
		with open(hosts_temp,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website inline forwebsite in website_list):
					file.write(line)
			file.truncate()
		print("fun  hours")
	time.sleep(5)


