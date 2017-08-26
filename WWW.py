import urllib.request
from tqdm import tqdm
from optparse  import *
import os , sys
from platform import system

if system() == 'Windows':
    os.system('cls')
    os.system('color a')

    
z = OptionParser('''
---------<>---------::
    PRO :: AMR REFAT
    PRO :: MIDO MOSTAFA
   
                                            ,--,                                   
          ,'  , `.   ,---,     ,--,     ,--,  
     ,-+-,.' _ |  '  .' \    |'. \   / .`|  
  ,-+-. ;   , || /  ;    '.  ; \ `\ /' / ;  
 ,--.'|'   |  ;|:  :       \ `. \  /  / .'  
|   |  ,', |  '::  |   /\   \ \  \/  / ./   
|   | /  | |  |||  :  ' ;.   : \  \.'  /    
'   | :  | :  |,|  |  ;/  \   \ \  ;  ;     
;   . |  ; |--' '  :  | \  \ ,'/ \  \  \    
|   : |  | ,    |  |  '  '--' ;  /\  \  \   
|   : '  |/     |  :  :     ./__;  \  ;  \  
;   | |`-'      |  | ,'     |   : / \  \  ; 
|   ;/          `--''       ;   |/   \  ' | 
'---'                       `---'     `--`  


-u /--url  :: link

ex:>>
script.py -u 'https://www.kau.edu.sa/files/830/files/60761_Linux.pdf'

''')
z.add_option ('-u','--url',dest = 'url',type = 'string')

(options,arga)= z.parse_args()

if options.url == None:
    print (z.usage)
    exit(0)
else:
    url= str(input('enter the link ::'))
    x = urllib.request.urlopen(url)
    print (x.info())
    name = url.split('/')[-1]
    file_size = int(x.headers['content-length'])
    block = 500
    amr = open(name,'wb')
    for i in tqdm (range(file_size)):
        i=i+block
        d=x.read(block)
        amr.write(d)
    x.close()









'''
https://www.isecur1ty.org/%D8%A5%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-python-%D9%84%D9%84%D8%AA%D8%B4%D9%88%D9%8A%D8%B4-%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D8%B4%D8%A8%D9%83%D8%A7%D8%AA/
import random
for i in range (1,15000):
    i = i*10
    x = ''.join ((random.choice('amrwqe{0}kop'.format (str(i))) for i in range (16)))
    print (x)
from bs4 import BeautifulSoup
import urllib.request
x = urllib.request.urlopen ('https://www.facebook.com')
y = (x.read(1000))

ss = BeautifulSoup(y,'html.parser')
#print (ss.prettify())
#print (ss.html.head.title.text)
#print (ss.find(‘link’)) 
for i in ss.findAll('link'):
    print (i.get('href'))
#print (ss.findAll('link'))'''











    
