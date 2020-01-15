import requests
import hashlib
import sys

def returnResponse(passwordChar):
	url='https://api.pwnedpasswords.com/range/' + passwordChar
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError("Problem with API")
	return res

def passwordCount(response,last):
	response = (lines.split(":") for lines in response.text.splitlines())
	for passw,count in response:
		if passw == last:
			return count
	return 0

def converter(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5, last= sha1password[:5], sha1password[5:]
	response = returnResponse(first5)
	return passwordCount(response, last)

def main(*args):
	for password in args:
		count = converter(password)
		if count:
			print(f'{password} was found {count} times. Think of a New one.' )
		else:
			print(f'{password} was Not found. Carry on.!')
	return 'done'


#Remove 'hello' and Pass your password in main function as string
main('hello')