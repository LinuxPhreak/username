#!/usr/bin/env python3
import urllib.request
import urllib.error
username = input("Username: ")

#Facebook
try:
    fb = urllib.request.urlopen('https://www.facebook.com/'+username)
    print('\033[0;32;48mFound User: https://www.facebook.com/'+username)
except urllib.error.HTTPError as e:
	print('\033[0;31;48mUser '+ username + ' Not Found: on Facebook')

#Twitter
try:
    twitter = urllib.request.urlopen('https://twitter.com/' + username)
    print('\033[0;32;48mFound User: https://twitter.com/' + username)
except urllib.error.HTTPError as e:
	print('\033[0;31;48mUser '+ username + ' Not Found: on Twitter')

#Google +
try:
	gplus = urllib.request.urlopen('https://plus.google.com/+' + username + '/posts')
	print('\033[0;32;48mFound User: https://plus.google.com/+' + username + '/posts')
except urllib.error.HTTPError as e:
	print('\033[0;31;48mUser '+ username + ' Not Found: on Google +')

#YouTube
try:
	yt = urllib.request.urlopen('https://www.youtube.com/user/'+username)
	print('\033[0;32;48mFound User: https://www.youtube.com/user/'+username)
except urllib.error.HTTPError as e:
	print('\033[0;31;48mUser '+ username + ' Not Found: on YouTube')

#About.me
try:
	yt = urllib.request.urlopen('https://about.me/' + username)
	print('\033[0;32;48mFound User: https://about.me/' + username)
except urllib.error.HTTPError as e:
	print('\033[0;31;48mUser '+ username + ' Not Found: on About')

#Vimeo
try:
	yt = urllib.request.urlopen('https://vimeo.com/' + username)
	print('\033[0;32;48mFound User: https://vimeo.com/' + username)
except urllib.error.HTTPError as e:
	print('\033[0;31;48mUser '+ username + ' Not Found: on Vimeo')

