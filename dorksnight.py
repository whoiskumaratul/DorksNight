#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from re import findall
import platform
import urllib, requests, os, time, sys
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
from urllib.parse import unquote



header = """

                                                         (www.hackingtruth.in) 
██████╗░░█████╗░██████╗░██╗░░██╗░██████╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝
██║░░██║██║░░██║██████╔╝█████═╝░╚█████╗░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░
██║░░██║██║░░██║██╔══██╗██╔═██╗░░╚═══██╗██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░
██████╔╝╚█████╔╝██║░░██║██║░╚██╗██████╔╝██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
(www.kumaratuljaiswal.in)
"""
desc = "Search deeply and gain result for bug bounty hunters and penetration tester - DorksNight"
deV_Info = """
Developed by: Kumar Atul Jaiswal 🤝 Aniket Mishra  
python3
Date: 2021 May 19 
Please report any incorrect results at kumaratuljaiswal222@gmail.com
Disclaimer: This is only for educationl purpose so, don't misuse N if you do, then it will be your responsibiliy.
Copyright ©️ 2021 Hacking Truth
"""



if(platform.system() == 'Windows'):
    os.system('cls')
if (platform.system() == 'Linux'):
    os.system('clear')   
    


print(header)
print(desc + deV_Info)
print("\033[1;33;40m" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +"\n" + "\033[0;0m")



def filter(link):
    link = link[7:]
    link = link.split('&')
    link = link[0]
    link = unquote(link)
    return link


def create_url(query):       #q=site:yahoo.com
    global url                         #python3 dork.py -key  yahoo.com site site -count 10
    url = "https://google.com/search?q="+urllib.parse.quote(keyword)+":"+urllib.parse.quote(query)
    print(url)

def do_keyword():
    create_url(query)
    print("[🇮🇳] findinG websitE oN googlE...")
    time.sleep(1)
    print("[🇮🇳] googlinG...")
    try:
       res = requests.get(url)
    except requests.ConnectionError:
       print("[--]can'T connecteD witH serveR. arE yoU connecteD witH interneT!...")
       exit()
    
    soup = BeautifulSoup(res.content, 'html.parser')
    print("[🇮🇳] listinG resulT...")
    time.sleep(0.5)
    print("[🇮🇳] congratS wE founD iT.")
    try:
        saver = input("[🇮🇳] Do yoU wanT tO savE thiS datA iN a filE? (Y/N) ".strip())
        l0g = ("")
    except KeyboardInterrupt:
        print("\n")
        print("[🇮🇳]useR interruptioN detectioN")
        time.sleep(0.4)

    def logger(saver):
        file = open((l0g) + ".txt", "a")
        file.write("\n")
        file.write(str(saver))
        file.close()      

    if saver.startswith("y" or "Y"):
        l0g = input("[🇮🇳] pleasE givE thE filE namE (only name): ")
        #print("\n")
        #logger(saver)
    else:
        print("[🇮🇳] SavinG is skippeD")
        time.sleep(0.4)
    
    for divs in soup.find_all('div', class_ = 'ZINbbc xpd O9g5cc uUPGi'):  
        try:
            aHref = divs.find('h3')
            link = divs.find('a')['href']

            if link[:7] == '/url?q=':
                star = (aHref.text)
                print(Fore.LIGHTYELLOW_EX ,'[🎭]', star, Fore.RED , end=' »»»» ')
                print(Fore.LIGHTGREEN_EX + filter(link))
                a = '[🎭]', filter(star)
                b = filter(link)
                data = (a ,b)
                logger(data)
                

        except:
            pass        
        

parser = argparse.ArgumentParser(description='Dorking is techniquie which is used to learn search techniques and for deeply search results and for all those who do bug hunting, penetration testing and involved with cyber security. .', prog='python3 dorknight.py -keyword intitle or "index of /" -query "TryHackMe Walkthrough by Hacking Truth" or  "admin password txt" ', usage='%(prog)s [options]' )

parser.add_argument('-query', action='store', dest='query', help='-query "admin password txt" use double or single quotes if it is more than one word') 
parser.add_argument('-key',action='store', dest='keyword', help='-key "index of /"')
parser.add_argument('-dorkinglist', action='store_true', dest='dorkinglist', help='See the dorking list')

given_args = parser.parse_args()

keyword = given_args.keyword
query = given_args.query

dorking = '''
[Keyword]         [Query]
site              yahoo.com
inurl             admin
"inurl exposing"    "inbody invisible"
intitle           engineering 
allintitle        "engineering books"
allinurl          admin login 
filetype or ext   pdf or ext:pdf
allintext         "software engineering"
intext            hacking 
"site gov"        "inurl adminlogin"
inurl             "view/index.shtml"
inurl.com         "/configuration.php-dist"
filetype:xls      “username | password”
"index.of / "     "admin password txt"
"intitle index of" "upload size parent directory
"intitle merak mail server web administration" "-hackstuff.com"
"index of /"       "admin password txt"
"exposing"         "feed:rss"
"filetype:xls"     "budget 
"filetype:xlsx"    "budget"
"filetype:csv"     "budget"
"filetype pdf"     "site nasa.gov"    

  updated...
'''

if given_args.dorkinglist:
   print(dorking)
   exit(0)

do_keyword()


    