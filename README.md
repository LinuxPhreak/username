# Username
Username was originally inspired by the [userrecon](http://go.techmeout.org/2L) shell script. I saw much potential and felt it can do much more if written in python. This is just the beginning of a detailed project. 

Currently right now it simply tells you if a username exists and where it exists. With the exception of finding a username on [Facebook](http://go.techmeout.org/2M). Then it will tell you the persons name as well by using web scraping.

## Requirements

* [Python3.6 or higher](http://go.techmeout.org/27)
* [Beautiful Soup 4 or higher](http://go.techmeout.org/2K)

## Installation
First install Git and Python3 from your Linux distro
### Ubuntu/Debian/LinuxMint
`sudo apt install git python3 python3-bs4`

### Fedora 28 or higher
`sudo dnf install git python3 python3-beautifulsoup4`

### Fedora 27 or older, CentOS, RedHat
`sudo yum install git python3 python3-beautifulsoup4`

### Arch Linux
`pacman -S git python3 python-beautifulsoup4`

I have an Arch Linux Repository For Username. You can install using pacman by doing the following.
Add the following lines to your `/etc/pacman.conf` file. 

`[bigben-repo]`

`SigLevel = Optional TrustAll`

`Server = http://bennix.net/bigben-repo/`

Then update the repo list.

`pacman -Syy`

Then you can install by simply typing in the following.

`pacman -S username`

### Gentoo
`emerge --ask dev-lang/python:3.7`

Next you clone the username repo. 
`git clone https://github.com/LinuxPhreak/username.git`

>Be sure to configure your git correctly. [Git Tutorial](https://techmeout.org/git-tutorial/)

## Usuage
Navigate to the username directory on your computer in your terminal and type the following. 

`python3 username.py`

![Program Running](include/program.png)
