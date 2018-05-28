#######################################################################################################################
# Image Downloader
#
#This code is to get links to images from image boards and download it responsibly
#
# Input variables:
#-->Forum Thread number
#-->Thread Start Page Number
#-->Thread End Page number
#-->Paralell download count
#-->File Save Location
#-->File sequential numbering or from source
#-->File prefix
#-->File Min Size
#-> verbose mode
#
#To add: verbose mode, post download deletion of poor images.
#######################################################################################################################

########Import libraries
from bs4 import BeautifulSoup
import re
import requests
import threading
import time
from urllib.parse import urlparse
import urllib.parse
import os
import argparse
from slugify import slugify

#########Input Variables#########
xossipThread = 1487535 #1086810
startPage = 6
endPage =10
threadCount = 10
saveLocation = "C:/Images/thrd1487535/"
fileprefix = "parser_"
useOriginalName = True
minKB = 5
######## Argument parser for command line

parser = argparse.ArgumentParser(description='This is a program to download images from Xossip.com threads.')
parser.add_argument( "Thread", metavar='ThreadId',
                    type=int,help='The thread id can be found in the URL. https://xossip.com/showthread.php?t=>1234567<')
parser.add_argument('startPage',metavar="Start-Page",type=int,help="Start downloads from Page Number")
parser.add_argument('endPage',metavar="End-Page",type=int,help="Download till Page Number")
parser.add_argument("-f", "--file",type=str, dest="saveLocation",help="Write images to FOLDER", metavar="FOLDER",required=True)
args = parser.parse_args()

xossipThread = args.Thread
startPage = args.startPage
endPage = args.endPage
saveLocation = args.saveLocation


#########This bit of code looks at the webpage and gets all the image urls#########
imageURL = []

for pageno in range(startPage,endPage+1):
    print("\rScanning Page "+str(pageno)+"...",end=" ")
    ####Edit here for other websites
    source = requests.get('https://www.xossip.com/showthread.php?t='+str(xossipThread)+'&page='+str(pageno))
    soup = BeautifulSoup(source.text,'lxml')
    for divtag in soup.find_all("div",id = re.compile("post_message_*")):
        for imgtag in divtag.find_all('img',border ="0",alt="",src = re.compile("http*")):
            #print(imgtag['src'])
            imageURL.append(imgtag['src'])

######### This bit of code filters out non xossip URLs and downloads them#########
print("\nFound "+str(len(imageURL))+" images. Filtering...")
#print(imageURL)
imageURLfiltered = []
for domain in imageURL:
    #print(urlparse(domain).netloc)
    if "xossip" not in urlparse(domain).netloc:
        imageURLfiltered.append(domain)

del imageURL

print("Filtered "+str(len(imageURLfiltered))+" image. Starting download...")
#print(imageURLfiltered)

#########This code downloads multiple images paralelly#########
if not os.path.exists(saveLocation):
    os.makedirs(saveLocation)

def download(link, filelocation,minKB):
    minSize = minKB*1000 #min file size to download in Bytes 5000 = 5KB
    flag = True
    r = requests.get(link, stream=True)
    ######Checks before download
    #check for min file size if content length is reported by server
    if r.headers.get("content-length"):
        if int(r.headers.get("content-length"))<minSize:
            flag = False
    #Check for file datatype
    if "image" not in r.headers["content-type"]:
        flag = False
    #Check for http errors
    if r.status_code != requests.codes.ok:
        flag = False

    #If all above checks are ok the flag variable would be true
    if flag:
        #print(r.headers)
        with open(filelocation, 'wb') as f:
            for chunk in r.iter_content(1024):
                if chunk:
                    f.write(chunk)
    else:
        print("Error downloading "+link)


def createNewDownloadThread(link, filelocation,minKB):
    download_thread = threading.Thread(target=download, args=(link,filelocation,minKB))
    download_thread.start()

for i in range(0,len(imageURLfiltered)):
    if useOriginalName:
        filesplit = urllib.parse.unquote(imageURLfiltered[i].split("/")[-1])
        fileName = saveLocation + slugify(filesplit[:-4])+"."+slugify(filesplit[-3:])
    else:
        fileName = saveLocation +fileprefix+str(i)+"."+slugify(imageURLfiltered[i][-3:])
    while(threading.active_count()>threadCount):
        time.sleep(0.1)
    print("\rDownloading "+str(i+1)+" of "+str(len(imageURLfiltered))+": "+imageURLfiltered[i]+"...",end=" ")
    createNewDownloadThread(imageURLfiltered[i],fileName,minKB)


############Summary of download