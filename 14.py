import os
reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        os.system("exit")

try:
	import requests
	import uuid
	import random
	import os
	import time 
	from os import system
	import colorama
	from colorama import Fore
	colorama.init(autoreset=True)
	
except Exception as m:
	print("Something Went Wrong\n")
	print(m)
	input()
	exit()
	
print("loding")
time.sleep(0.3)
print("10%■□□□□□□□□□")
time.sleep(5)
print("20%■■□□□□□□□□")
time.sleep(5)
print("30%■■■□□□□□□□")
time.sleep(5)
print("40%■■■■□□□□□□")
time.sleep(5)
print("50%■■■■■□□□□□")
time.sleep(5)
print("60%■■■■■■□□□□")
time.sleep(5)
print("70%■■■■■■■□□□")
time.sleep(5)
print("80%■■■■■■■■□□")
time.sleep(5)
print("90%■■■■■■■■■□")
time.sleep(5)
print("100%■■■■■■■■■")
time.sleep(5)
os.system("clear")
print("""
⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
""")

rnd = "abcdefghijklmnopqrwstuvwxyz1234567890"

input("Click Enter To Start Checking")

ggg = open("users.txt", "r")

while 1:
	email = random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+"@gmail.com"
	password = random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)
	username = ggg.readline().split("\n")[0]
	if username == "":
		print("Done Checking\nClick Enter To Exit")
		input()
		exit()
	uid = str(uuid.uuid4())
	
	url = "https://i.instagram.com/api/v1/accounts/create_validated/"
	
	hd_login = {
		'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "en-US",
		"X-IG-Capabilities": "3brTvw==",
		"X-IG-Connection-Type": "WIFI",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		'Host': 'i.instagram.com'
}

	data = {
		"device_id": uid,
		"uuid": uid,
		"email": email,
		"password": password,
		"_csrftoken": "missing",
		"firt_name": "Soud",
		"username": username
}

	req = requests.post(url, data=data, headers=hd_login)
	
	if "username_held_by_others" in req.text:
		print(Fore.RED+f"14 Day >> @{username}")
		with open("14-Day.txt", "a") as dd:
			dd.write(f"{username}\n")
	
	elif "username_is_taken" in req.text:
		print(Fore.GREEN+f"Not 14 Day >> @{username}")
		with open("Not 14-Day.txt", "a") as dd:
			dd.write(f"{username}\n")
	
	else:
		print(Fore.RED+f"Error >>  @{username}")
		print(req.text)
