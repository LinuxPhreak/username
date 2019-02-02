#!/usr/bin/env python3
import requests
import os
import time
from bs4 import BeautifulSoup

os.system("printf '\033c'");

def intro():
	print('\033[1;33;48m _______   ______   ___   ___ ___   ___ ')
	print('\033[1;33;48m|       \ /  __  \  \  \ /  / \  \ /  / ')
	print('\033[1;33;48m|  .--.  |  |  |  |  \  V  /   \  V  /  ')
	print('\033[1;33;48m|  |  |  |  |  |  |   >   <     >   <   ')
	print("\033[1;33;48m|  '--'  |  `--'  |  /  .  \   /  .  \  ")
	print('\033[1;33;48m|_______/ \______/  /__/ \__\ /__/ \__\   ') 
	time.sleep(2);
	os.system("printf '\033c'");                          

#This is a testing function
def tester():
	#function for testing
	check_github = requests.get('https://github.com/LinuxPhreak')
	github_soup = BeautifulSoup(check_github.content, 'html.parser')
	if (check_github.status_code == 200):
		print("Yes")
	else:
		print("wrong")

#Facebook		
def fb():
	#function for facebook
	check_fb = requests.get('https://www.facebook.com/' + username)
	fb_soup = BeautifulSoup(check_fb.content, 'html.parser')
	if (fb_soup.title.get_text() != 'Page Not Found | Facebook'):
		print('\033[0;32;48mFound User: https://www.facebook.com/' + username)
		print(fb_soup.h1.get_text())
	else:
		print('\033[0;31;48mNo User Found On Facebook')

#Instagram	
def instagram():
	check_ig = requests.get('https://www.instagram.com/' + username)
	if (check_ig.status_code == 200):
		print('Found User: https://www.instagram.com/' + username)
	else:
		print('\033[0;31;48mNo User Found On Instagran')

#Twitter
def twitter():
	check_twitter = requests.get('https://twitter.com/' + username)
	twitter_soup = BeautifulSoup(check_twitter.content, 'html.parser')
	if (twitter_soup.title.get_text() != 'Twitter / ?'):
		print('Found User: https://twitter.com/' + username)
	else:
		print('\033[0;31;48mNo User Found On Twitter')

#YouTube
def yt():
	check_yt = requests.get('https://www.youtube.com/user/' + username)
	yt_soup = BeautifulSoup(check_yt.content, 'html.parser')
	if (yt_soup.title.get_text() != 'YouTube'):
		print('Found User: https://www.youtube.com/user/' + username)
	else:
		print('\033[0;31;48mNo User Found On YouTube') 

#Blogger
def blogger():
	check_blogger = requests.get('https://' + username + '.blogspot.com/')
	blogger_soup = BeautifulSoup(check_blogger.content, 'html.parser')
	if (blogger_soup.title.get_text() != 'Blog not found'):
		print('Found Blog: https://' + username + '.blogspot.com')
	else:
		print('\033[0;31;48mNo Blog Found On Blogger') 

#GLOOGLE PLUS

def gplus():
	check_gplus = requests.get('https://plus.google.com/+' + username + '/posts')
	gplus_soup = BeautifulSoup(check_gplus.content, 'html.parser')
	if (check_gplus.status_code == 200):
		print('Found User: https://plus.google.com/+' + username)
	else:
		print('\033[0;31;48mNo user found on Google +')

#Reddit
def reddit():
	#Not working
	check_reddit = requests.get('https://www.reddit.com/user/' + username)
	reddit_soup = BeautifulSoup(check_reddit.content, 'html.parser')
	print(reddit_soup.title.get_text())

#Word Press
def wp():
	check_wp = requests.get('https://' + username + '.wordpress.com/')
	wp_soup = BeautifulSoup(check_wp.content, 'html.parser')
	if (wp_soup.title.get_text() != 'WordPress.com'):
		print("WP User Found https://" + username + ".wordpress.com/")
	else:
		print('\033[0;31;48mNo Word Press Blog by that name')

## PINTEREST
def pinterest():
	check_pinterest = requests.get('https://www.pinterest.com/' + username)
	pinterest_soup = BeautifulSoup(check_pinterest.content, 'html.parser')
	if (pinterest_soup.title.get_text() != 'Pinterest'):
		print('Found User: https://www.pinterest.com/' + username)
	else:
		print('\033[0;31;48mNo Pinterest User Found')

#GitHub
def github():
	check_github = requests.get('https://github.com/' + username)
	github_soup = BeautifulSoup(check_github.content, 'html.parser')
	if (check_github.status_code == 200):
		print('Found User: https://github.com/' + username)
	else:
		print('\033[0;31;48mNo User Found On GitHub')

#TUMBLR
def tumblr():
	check_tumblr = requests.get('http://' + username + '.tumblr.com/#_=_')
	tumblr_soup = BeautifulSoup(check_tumblr.content, 'html.parser')
	if (check_tumblr.status_code == 200):
		print('User found http://' + username + '.tumblr.com/')
	else:
		print('\033[0;31;48mUser Not Found On Tumblr')

#FLICKR
def flickr():
	check_flickr = requests.get('https://www.flickr.com/people/' + username)
	if (check_flickr.status_code == 200):
		print('User found https://www.flickr.com/people/' + username)
	else:
		print('\033[0;31;48mUser Not Found On Flickr')

#STEAM
def steam():
	check_steam = requests.get('https://steamcommunity.com/id/' + username)
	steam_soup = BeautifulSoup(check_steam.content, 'html.parser')
	if (steam_soup.title.get_text() != 'Steam Community :: Error'):
		print('User found https://steamcommunity.com/id/' + username)
	else:
		print("\033[0;31;48mNo Steam User Found")

#VIMEO
def vimeo():
	check_vimeo = requests.get('https://vimeo.com/' + username)
	vimeo_soup = BeautifulSoup(check_vimeo.content, 'html.parser')
	if (vimeo_soup.title.get_text() != 'VimeUhOh'):
		print('User found https://vimeo.com/' + username)
	else:
		print('\033[0;31;48mNo Vimeo user Found')
		
#SoundCloud
def sndcloud():
	check_sndcloud = requests.get('https://soundcloud.com/' + username)
	sndcloud_soup = BeautifulSoup(check_sndcloud.content, 'html.parser')
	if (check_sndcloud.status_code == 200):
		print('User found https://soundcloud.com/' + username)
	else:
		print('\033[0;31;48mUser not on Sound Cloud')

#DISQUS
def disqus():
	check_disqus = requests.get('https://disqus.com/' + username)
	disqus_soup = BeautifulSoup(check_disqus.content, 'html.parser')
	if (check_disqus.status_code == 200):
		print('User found https://disqus.com/' + username)
	else:
		print('\033[0;31;48mUser not on Disqus')

#MEDIUM
def medium():
	check_med = requests.get('https://medium.com/@' + username)
	med_soup = BeautifulSoup(check_med.content, 'html.parser')
	if (check_med.status_code == 200):
		print('User found https://medium.com/@' + username)
	else:
		print('\033[0;31;48mNo user on Medium')

#DEVIANTART
def deviantart():
	check_devart = requests.get('https://www.deviantart.com/' + username)
	devart_soup = BeautifulSoup(check_devart.content, 'html.parser')
	if (check_devart.status_code == 200):
		print('User found https://.deviantart.com/' + username)
	else:
		print('\033[0;31;48mNo user on Deviant Art')

#VK
def vk():
	check_vk = requests.get('https://vk.com/' + username)
	vk_soup = BeautifulSoup(check_vk.content, 'html.parser')
	if (check_vk.status_code == 200):
		print('User found https://vk.com/' + username)
	else:
		print('\033[0;31;48mNo user on VK')
		
#About.me
def about():
	check_about = requests.get('https://about.me/' + username)
	about_soup = BeautifulSoup(check_about.content, 'html.parser')
	if (check_about.status_code == 200):
		print('User found https://about.me/' + username)
	else:
		print('\033[0;31;48mNo user on About.me')

#Imgur
def imgur():
	check_imgur = requests.get('https://imgur.com/user/' + username)
	imgur_soup = BeautifulSoup(check_imgur.content, 'html.parser')
	if (check_imgur.status_code == 200):
		print('User found https://imgur.com/user/' + username)
	else:
		print('\033[0;31;48mNo user on imgur')

#FlipBoard
def flipboard():
	check_flipboard = requests.get('https://flipboard.com/@' + username)
	flipboard_soup = BeautifulSoup(check_flipboard.content, 'html.parser')
	if (check_flipboard.status_code == 200):
		print('User found https://flipboard.com/@' + username)
	else:
		print('\033[0;31;48mUser not on Flipboard')

#SlideShare
def slideshare():
	check_slideshare = requests.get('https://slideshare.net/' + username)
	slideshare_soup = BeautifulSoup(check_slideshare.content, 'html.parser')
	if (check_slideshare.status_code == 200):
		print('User found https://slideshare.net/' + username)
	else:
		print('\033[0;31;48mNo user on SlideShare')

#Patreon
def patreon():
	check_patreon = requests.get('https://www.patreon.com/' + username)
	patreon_soup = BeautifulSoup(check_patreon.content, 'html.parser')
	if (check_patreon.status_code == 200):
		print('User found https://www.patreon.com/' + username)
	else:
		print('\033[0;31;48mNo user on Patreon')
		
#Ebay
def ebay():
	check_ebay = requests.get('https://www.ebay.com/usr/' + username)
	ebay_soup = BeautifulSoup(check_ebay.content, 'html.parser')
	if (ebay_soup.title.get_text() != 'eBay Profile - error'):
		print('User found https://www.ebay.com/usr/' + username)
	else:
		print('\033[0;31;48mUser not on eBay')
		
#CashMe
def cashme():
	check_cashme = requests.get('https://cash.me/$' + username)
	cashme_soup = BeautifulSoup(check_cashme.content, 'html.parser')
	if (check_cashme.status_code == 200):
		print('User found https://cash.me/$' + username)
	else:
		print('\033[0;31;48mUser not on CashMe')
		
#Wikipedia
def wikipedia():
	check_wikipedia = requests.get('https://www.wikipedia.org/wiki/User:' + username)
	wikipedia_soup = BeautifulSoup(check_wikipedia.content, 'html.parser')
	if (check_wikipedia.status_code == 200):
		print('User found https://www.wikipedia.org/wiki/User:' + username)
	else:
		print('\033[0;31;48mUser not on Wikipedia')

#Pastebin
def pastebin():
	check_pastebin = requests.get('https://pastebin.com/u/' + username)
	pastebin_soup = BeautifulSoup(check_pastebin.content, 'html.parser')
	if (pastebin_soup.title.get_text() != 'Pastebin.com - #1 paste tool since 2002!'):
		print('User found https://pastebin.com/u/' + username)
	else:
		print('\033[0;31;48mUser not on Pastebin')
		
#Etsy
def etsy():
	check_etsy = requests.get('https://www.etsy.com/people/' + username)
	etsy_soup = BeautifulSoup(check_etsy.content, 'html.parser')
	if (check_etsy.status_code == 200):
		print('User found https://www.etsy.com/people/' + username)
	else:
		print('\033[0;31;48mUser not on Etsy')
		
#Spotify
def spotify():
	check_spotify = requests.get('https://open.spotify.com/user/' + username)
	spotify_soup = BeautifulSoup(check_spotify.content, 'html.parser')
	if (check_spotify.status_code == 200):
		print('User found https://open.spotify.com/user/' + username)
	else:
		print('\033[0;31;48mUser not on Spotify')
		
#Ello
def ello():
	check_ello = requests.get('https://ello.co/' + username)
	ello_soup = BeautifulSoup(check_ello.content, 'html.parser')
	if (check_ello.status_code == 200):
		print('User found https://ello.co/' + username)
	else:
		print('\033[0;31;48mUser not on Ello')

## OKCupid
# not working yet
def okc():
	check_okc = requests.get('https://www.okcupid.com/profile/' + username)
	okc_soup = BeautifulSoup(check_okc.content, 'html.parser')
	if (check_okc.status_code != 404):
		print('User found https://www.okcupid.com/profile/' + username)
	else:
		print('\033[0;31;48mUser not on OKCupid')

#HackerNews
def hackernews():
	check_hnews = requests.get('https://news.ycombinator.com/user?id=' + username)
	hnews_soup = BeautifulSoup(check_hnews.content, 'html.parser')
	if (check_hnews.text != 'No such user.'):
		print('User found https://news.ycombinator.com/user?id=' + username)
	else:
		print('\033[0;31;48mUser not on Hacker News')

#Foursquare
def foursquare():
	check_foursquare = requests.get('https://foursquare.com/' + username)
	foursquare_soup = BeautifulSoup(check_foursquare.content, 'html.parser')
	if (check_foursquare.status_code == 200):
		print('User found https://foursquare.com/' + username)
	else:
		print('\033[0;31;48mUser not found on Four Square')

#BitBucket
def bitbucket():
	check_bitbucket = requests.get('https://bitbucket.org/' + username)
	bitbucket_soup = BeautifulSoup(check_bitbucket.content, 'html.parser')
	if (check_bitbucket.status_code == 200):
		print('User found https://bitbucket.org/' + username)
	else:
		print('\033[0;31;48mUser not on BitBucket')
		
#MixCloud
def mixcloud():
	check_mixcloud = requests.get('https://www.mixcloud.com/' + username)
	mixcloud_soup = BeautifulSoup(check_mixcloud.content, 'html.parser')
	if (mixcloud_soup.title.get_text() != 'Page Not Found | Mixcloud'):
		print('User found https://www.mixcloud.com/' + username)
	else:
		print('\033[0;31;48mUser not on MixCloud')
		
#DailyMotion
def dmotion():
	check_dmotion = requests.get('https://www.dailymotion.com/' + username)
	dmotion_soup = BeautifulSoup(check_dmotion.content, 'html.parser')
	if (check_dmotion.status_code == 200):
		print('User found https://www.dailymotion.com/' + username)
	else:
		print('\033[0;31;48mUser not on Daily Motion')
		
#Instructables
def instructables():
	check_instructables = requests.get('https://www.instructables.com/member/' + username)
	instructables_soup = BeautifulSoup(check_instructables.content, 'html.parser')
	if (check_instructables.status_code == 200):
		print('User found https://www.instructables.com/member/' + username)
	else: 
		print('\033[0;31;48mUser not on Instructables')
		
#Buzzfeed
def buzzfeed():
	check_buzzfeed = requests.get('https://buzzfeed.com/' + username)
	buzzfeed_soup = BeautifulSoup(check_buzzfeed.content, 'html.parser')
	if (check_buzzfeed.status_code == 200):
		print('User found https://buzzfeed.com/' + username)
	else:
		print('\033[0;31;48mUser not on BuzzFeed')
		
#TripAdvisor
def tripadviser():
	check_tripadviser = requests.get('https://www.tripadvisor.com/members/' + username)
	tripadviser_soup = BeautifulSoup(check_tripadviser.content, 'html.parser')
	if (check_tripadviser.status_code == 200):
		print('Found user https://www.tripadvisor.com/members/' + username)
	else:
		print('\033[0;31;48mUser not on Trip Adviser')

#Trip
def trip():
	check_trip = requests.get('https://www.trip.skyscanner.com/user/' + username)
	trip_soup = BeautifulSoup(check_trip.content, 'html.parser')
	if (check_trip.status_code == 200):
		print('Found user https://www.trip.skyscanner.com/user/' + username)
	else:
		print('\033[0;31;48mUser not on Trip SkyScanner')

## Tripit
def tripit():
	check_tripit = requests.get('https://www.tripit.com/people/' + username + '#/profile/basic-info')
	trip_soup = BeautifulSoup(check_tripit.content, 'html.parser')
	if (check_tripit.status_code == 200):
		print('User found https://www.tripit.com/people/' + username + '#/profile/basic-info')
	else:
		print('\033[0;31;48mUser not on Trip It')

#Newgrounds
def newsground():
	check_newsground = requests.get('https://' + username + '.newgrounds.com')
	newsground_soup = BeautifulSoup(check_newsground.content, 'html.parser')
	if (check_newsground.status_code == 200):
		print('Found user https://' + username + '.newgrounds.com')
	else:
		print('\033[0;31;48mUser not on News Ground')	

#CreativeMarket
def creativemarket():
	check_cmarket = requests.get('https://creativemarket.com/' + username)
	cmarket_soup = BeautifulSoup(check_cmarket.content, 'html.parser')
	if (cmarket_soup.title.get_text() != 'Fonts, Graphics, Themes and More ~ Creative Market'):
		print('Found user https://creativemarket.com/' + username)
	else:
		print('\033[0;31;48mUser not on Creative Market')
		
#Codecademy
def codecademy():
	check_codecademy = requests.get('https://www.codecademy.com/' + username)
	codecademy_soup = BeautifulSoup(check_codecademy.content, 'html.parser')
	if (check_codecademy.status_code == 200):
		print('User found https://www.codecademy.com/' + username)
	else:
		print('\033[0;31;48mUser not on Codecademy')

#ColourLovers
def colourLuv():
	check_colourLuv = requests.get('https://www.colourlovers.com/lover/' + username)
	colourLuv_soup = BeautifulSoup(check_colourLuv.content, 'html.parser')
	if (check_colourLuv.status_code == 200):
		print('User found https://www.colourlovers.com/lover/' + username)
	else:
		print('\033[0;31;48mUser not on Colour Lovers')
		
#Trakt
def trakt():
	check_trakt = requests.get('https://trakt.tv/users/' + username)
	trakt_soup = BeautifulSoup(check_trakt.content, 'html.parser')
	if (check_trakt.status_code == 200):
		print('User found https://trakt.tv/users/' + username)
	else:
		print('\033[0;31;48mUser not on Trakt')
		
#Livejournal
def livejournal():
	check_livejournal = requests.get('https://' + username + '.livejournal.com')
	livejournal_soup = BeautifulSoup(check_livejournal.content, 'html.parser')
	if (check_livejournal.status_code == 200):
		print('User found https://' + username + '.livejournal.com')
	else:
		print('\033[0;31;48mUser not on Live Journal')

## Tracky
def tracky():
	check_tracky = requests.get('https://tracky.com/~' + username)
	tracky_soup = BeautifulSoup(check_tracky.content, 'html.parser')
	if (tracky_soup.title.get_text() != 'Home &mdash; Tracky'):
		print('User found https://tracky.com/user/' + username)
	else:
		print('\033[0;31;48mUser not on Tracky')

## Pay Pal
def paypal():
	check_paypal = requests.get('https://www.paypal.me/' + username)
	paypal_soup = BeautifulSoup(check_paypal.content, 'html.parser')
	if (check_paypal.status_code == 200):
		print('User found https://www.paypal.me/' + username)
	else:
		print('\033[0;31;48mUser not on Pay Pal')
		
#Quora
def quora():
	check_quora = requests.get('https://www.quora.com/profile/' + username)
	quora_soup = BeautifulSoup(check_quora.content, 'html.parser')
	if (check_quora.status_code == 200):
		print('User found https://www.quora.com/profile/' + username)
	else:
		print('\033[0;31;48mUser not on Quora')

intro()

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

if (number == '1'):
	username = input("Username: ")
	fb()
	instagram()
	twitter()
	yt()
	blogger()
	github()
	wp()
	gplus()
	pinterest()
	tumblr()
	flickr()
	steam()
	vimeo()
	sndcloud()
	disqus()
	medium()
	deviantart()
	vk()
	about()
	imgur()
	flipboard()
	slideshare()
	patreon()
	ebay()
	cashme()
	wikipedia()
	pastebin()
	etsy()
	spotify()
	ello()
	hackernews()
	foursquare()
	bitbucket()
	mixcloud()
	dmotion()
	instructables()
	buzzfeed()
	tripadviser()
	trip()
	newsground()
	creativemarket()
	codecademy()
	colourLuv()
	trakt()
	livejournal()
	quora()
elif (number == '2'):
	username = input("Username: ")
	fb()
elif (number == '3'):
	username = input("Username: ")
	twitter()
elif (number == '4'):
	username = input("Username: ")
	gplus()
elif (number == '5'):
	username = input("Username: ")
	yt()
elif (number == '6'):
	username = input("Username: ")
	blogger()
elif (number == '7'):
	username = input("Username: ")
	wp()
elif (number == '8'):
	username = input("Username: ")
	tumblr()
elif (number == '9'):
	username = input("Username: ")
	github()
elif (number == '10'):
	username = input("Username: ")
	instagram()
elif (number == '11'):
	username = input("Username: ")
	flickr()
elif (number == '12'):
	username = input("Username: ")
	pinterest()
elif (number == '13'):
	username = input("Username: ")
	sndcloud()
elif (number == '14'):
	username = input("Username: ")
	spotify()
elif (number == '15'):
	username = input("Username: ")
	mixcloud()
elif (number == '16'):
	username = input("Username: ")
	ello()
elif (number == '17'):
	username = input("Username: ")
	patreon()
elif (number == '18'):
	username = input("Username: ")
	deviantart()
elif (number == '19'):
	username = input("Username: ")
	slideshare()
elif (number == '20'):
	username = input("Username: ")
	vk()
elif (number == '21'):
	username = input("Username: ")
	about()
elif (number == '22'):
	username = input("Username: ")
	flipboard()
elif (number == '23'):
	username = input("Username: ")
	ebay()
elif (number == '24'):
	username = input("Username: ")
	vimeo()
elif (number == '25'):
	username = input("Username: ")
	wikipedia()
elif (number == '26'):
	username = input("Username: ")
	etsy()
elif (number == '27'):
	username = input("Username: ")
	hackernews()
elif (number == '28'):
	username = input("Username: ")
	imgur()
elif (number == '29'):
	username = input("Username: ")
	medium()
elif (number == '30'):
	username = input("Username: ")
	pastebin()
elif (number == '31'):
	username = input("Username: ")
	creativemarket()
elif (number == '32'):
	username = input("Username: ")
	cashme()
elif (number == '33'):
	username = input("Username: ")
	livejournal()
elif (number == '34'):
	username = input("Username: ")
	steam()
elif (number == '35'):
	username = input("Username: ")
	tripadviser()
elif (number == '36'):
	username = input("Username: ")
	buzzfeed()
elif (number == '37'):
	username = input("Username: ")
	dmotion()
elif (number == '38'):
	username = input("Username: ")
	colourLuv()
elif (number == '39'):
	username = input("Username: ")
	trakt()
elif (number == '40'):
	username = input("Username: ")
	disqus()
elif (number == '41'):
	username = input("Username: ")
	codecademy()
elif (number == '42'):
	username = input("Username: ")
	instructables()
elif (number == '43'):
	username = input("Username: ")
	foursquare()
elif (number == '44'):
	username = input("Username: ")
	bitbucket()
elif (number == '45'):
	username = input("Username: ")
	trip()
elif (number == '46'):
	username = input("Username: ")
	newsground()
elif (number == '47'):
	username = input("Username: ")
	quora()
