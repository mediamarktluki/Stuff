import time
import RPi.GPIO as GPIO
import MFRC522
import MyRead
import requests
headers = {
    'Content-Type': 'text/plain',
    'Accept': 'application/json',}
data = 'ON'
while True:
 try:
  id1 = ["<id1>","<id2>","<id3>"]
  master = "master"
  run = MyRead.MyRead()
  text = run.read()
  if text in id1:
   print("Success" + text)
   print("")
   response = requests.post('http://<YourIP>:8080/rest/items/<yourItem>', headers=headers, data=data)
   time.sleep(5)
  else:
   if text == master:
    print("new Card")
    print("wait 10 Sec")
    time.sleep(10)
    text1 = run.read()
    print(text1)
    id1.append(text1)
   print(id1)
 except (KeyboardInterrupt):
	raise
 except:
	print("")
