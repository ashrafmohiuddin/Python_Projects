import requests
from bs4 import BeautifulSoup
import smtplib
import time
from files import url,headers,your_price,from_mail,to_mail,password
# files.py contains UserAgent in headers, url of amazon product, from and to mail addresses , password of from_mail and Price you wanna track.

def checkPrice(url,headers,your_price,from_mail,to_mail,password):

	page = requests.get(url,headers = headers)

	soup = BeautifulSoup(page.content,"html.parser")

	ans = soup.find(id="priceblock_ourprice").get_text()

	list(ans)
	lst = []
	int_str = ["0","1","2","3","4","5","6","7","8","9"]
	for i in ans:
		if i in int_str:
			lst.append(i)

	ans = float("".join(lst))
	
	ans = ans/100

	if ans < your_price :
		send_mail(from_mail,to_mail,password,url)

def send_mail(from_mail,to_mail,password,url):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login(from_mail,password)

	subject = "Price is less than your price!!"

	body = f"The product is priced lower than your price.Click the link to access the product {url}"

	message = f"Subject: {subject} \n\n {body}"

	server.sendmail(from_mail,to_mail,message)

	print("Mail is sent successfully")

	server.quit()

while True:
	checkPrice(url,headers,your_price,from_mail,to_mail,password)
	time.sleep(30)
