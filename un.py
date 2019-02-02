#!/usr/bin/env python3
import urllib.request
import urllib.error
import os

os.system("printf '\033c'");

#Facebook
def facebook():
	try:
		fb = urllib.request.urlopen('https://www.facebook.com/'+username)
		print('\033[0;32;48mFound User: https://www.facebook.com/'+username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Facebook')

#Twitter
def twitter():
	try:
		twitter = urllib.request.urlopen('https://twitter.com/' + username)
		print('\033[0;32;48mFound User: https://twitter.com/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Twitter')

#Google +
def googleplus():
	try:
		gplus = urllib.request.urlopen('https://plus.google.com/+' + username + '/posts')
		print('\033[0;32;48mFound User: https://plus.google.com/+' + username + '/posts')
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Google +')

#Blogger
def blogger():
	try:
		blogspot = urllib.request.urlopen('https://' + username + '.blogspot.com/')
		print('\033[0;32;48mFound User: https://' + username + '.blogspot.com/')
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Blogger')

#YouTube
def youtube():
	try:
		yt = urllib.request.urlopen('https://www.youtube.com/user/'+username)
		print('\033[0;32;48mFound User: https://www.youtube.com/user/'+username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on YouTube')

#About.me
def about():
	try:
		aboutme = urllib.request.urlopen('https://about.me/' + username)
		print('\033[0;32;48mFound User: https://about.me/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on About')

#Vimeo
def vimeo():
	try:
		vim = urllib.request.urlopen('https://vimeo.com/' + username)
		print('\033[0;32;48mFound User: https://vimeo.com/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Vimeo')

#Word Press
def wordpress():
	try:
		wp = urllib.request.urlopen('https://' + username + '.wordpress.com/')
		print('\033[0;32;48mFound User: https://' + username + '.wordpress.com/')
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on WordPresss')

#Tumblr
def tumblr():
	try:
		tmb = urllib.request.urlopen('http://' + username + '.tumblr.com/#_=_')
		print('\033[0;32;48mFound User: http://' + username + '.tumblr.com/#_=_')
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Tumblr')

#GitHub
def github():
	try:
		git = urllib.request.urlopen('https://github.com/' + username)
		print('\033[0;32;48mFound User: https://github.com/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on GitHub')

#Instagram
def instagram():
	try:
		instg = urllib.request.urlopen('https://www.instagram.com/' + username)
		print('\033[0;32;48mFound User: https://www.instagram.com/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Instagram')

#FLICKR
def flickr():
	try:
		flick = urllib.request.urlopen('https://www.flickr.com/people/' + username)
		print('\033[0;32;48mFound User: https://www.flickr.com/people/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Flickr')

#Pinterist
def pinterest():
	try:
		pint = urllib.request.urlopen('https://www.pinterest.com/' + username)
		print('\033[0;32;48mFound User: https://www.pinterest.com/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Pinterist')

#SoundCloud
def sndcloud():
	try:
		sc = urllib.request.urlopen('https://soundcloud.com/' + username)
		print('\033[0;32;48mFound User: https://soundcloud.com/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on SoundCloud')

#Spotify
def spotify():
	try:
		spot = urllib.request.urlopen('https://open.spotify.com/user/' + username)
		print('\033[0;32;48mFound User: https://open.spotify.com/user/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Spotify')

#MixCloud
def mixcloud():
	try:
		mc = urllib.request.urlopen('https://www.mixcloud.com/' + username)
		print('\033[0;32;48mFound User: https://www.mixcloud.com/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Mixcloud')

#Ello
def ello():
	try:
		el = urllib.request.urlopen('https://ello.co/' + username)
		print('\033[0;32;48mFound User: https://ello.co/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Ello')
		print(e)

#Patreon
def patreon():
	try:
		pat = urllib.request.urlopen('https://www.patreon.com/' + username)
		print('\033[0;32;48mFound User: https://www.patreon.com/' + username)
	except urllib.error.HTTPError as e:
		print('\033[0;31;48mUser '+ username + ' Not Found: on Patreon')


print('Enter a number to get the user name on a specific site. \nEntering the number 1 will search for the \nsame username on all sites in the list. \n')
print('1: All                   2: Facebook      	  3: Twitter')
print('4: Google +              5: Youtube       	  6: Blogger')
print('7: WordPress             8: Tumblr        	  9: GitHub')
print('10: Instagram            11: Flickr       	  12: Pinterest')
print('13: Sound Cloud          14: Spotify      	  15: Mixcloud')
print('16: Ello                 17: Patreon      	  18: Deviantart')
print('19: Slideshare           20: VK           	  21: About')
print('22: Flip Board           23: eBay         	  24: Vimeo')
print('25: Wikipedia            26: Etsy         	  27: Hacker News')
print('28: Imgur                29: Medium       	  30: Pastebin')
print('31: Creative Mmarket     32: Cash.me           33: Live Journal')
print('34: Steam                35: Trip Advisor      36: Buzz Feed')
print('37: Daily Motion         38: Colour Lovers     39: Trakt')
print('40: Disqus               41: Codecademy        42: Instructables')
print('43: Foursquare           44: Bitbucket         45: Trip')
print('46: News Ground          47: Quora             48: Help')

number = input("Enter Number: ")
if (number == "1"):
	username = input("Username: ")
	facebook()
	twitter()
	googleplus()
	youtube()
	about()
	vimeo()
	wordpress()
	blogger()
	tumblr()
	github()
	instagram()
	flickr()
	pinterest()
	sndcloud()
	spotify()
	mixcloud()
elif (number == "2"):
	username = input("Username: ")
	facebook()
elif (number == "3"):
	username = input("Username: ")
	twitter()
elif (number == "4"):
	username = input("Username: ")
	googleplus()
elif (number == "5"):
	username = input("Username: ")
	youtube()
elif (number == "6"):
	username = input("Username: ")
	blogger()
elif (number == "7"):
	username = input("Username: ")
	wordpress()
elif (number == "8"):
	username = input("Username: ")
	tumblr()
elif (number == "9"):
	username = input("Username: ")
	github()
elif (number == "10"):
	username = input("Username: ")
	instagram()
elif (number == "11"):
	username = input("Username: ")
	flickr()
elif (number == "12"):
	username = input("Username: ")
	pinterest()
elif (number == "13"):
	username = input("Username: ")
	sndcloud()
elif (number == "14"):
	username = input("Username: ")
	spotify()
elif (number == "15"):
	username = input("Username: ")
	mixcloud()
elif (number == "16"):
	username = input("Username: ")
	ello()
elif (number == "17"):
	username = input("Username: ")
	patreon()
elif (number == "21"):
	username = input("Username: ")
	about()
elif (number == "24"):
	username = input("Username: ")
	vimeo()