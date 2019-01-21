#!/usr/bin/env python3
import urllib.request
import urllib.error
username = input("Username: ")

#Facebook
try:
    fb = urllib.request.urlopen('https://www.facebook.com/'+username)
    print('\033[0;32;48mFound User: https://www.facebook.com/'+username)
except urllib.error.HTTPError as e:
	print('\033[0;31;48mUser Not Found:')

#YouTube
try:
	yt = urllib.request.urlopen('https://www.youtube.com/user/'+username)
	print('\033[0;32;48mFound User: https://www.youtube.com/user/'+username)
except urllib.error.HTTPError as e:
	print('\033[0;31;48mUser Not Found:')