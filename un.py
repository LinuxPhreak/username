#!/usr/bin/env python3
import urllib.request
import urllib.error
import os
#

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
		print('\033[0;31;48mUser '+ username + ' Not Found: on Vimeo')

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
elif (number == "7"):
	username = input("Username: ")
	wordpress()
elif (number == "21"):
	username = input("Username: ")
	about()
elif (number == "24"):
	username = input("Username: ")
	vimeo()