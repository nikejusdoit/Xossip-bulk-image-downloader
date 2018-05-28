# Xossip-bulk-image-downloader
This is python code to bulk download images from a xossip thread. (as of 28th May 2018 formatting)
The code can be slightly modified to download images from other famous image boards. Learn Beautiful soup if you wish to DIY or drop me a message on which website you would like next.

##Inputs

- Forum Thread number: find this in the URL. For "https://www.xossip.com/showthread.php?t=**1527778**" the thread number is 1527778.

- Thread Start Page Number: Starting Page from which you want to download the images.

- Thread End Page number: Last Page till which you want to download the images.

- Paralell download count: number of paralell image downloads. Higher = faster but irresponsible.(Recommended 5)

- File Save Location: Specify the folder location. Folder must exist.

- File Name - sequential or original: Sequential renames the images in the order of download. Original retains file name.

- File prefix: prefix for sequential filenames

- File Min Size: Min file size to download. This serves to filter out images of emoticons and other non relevant images.

##Future work required:
1. Verbose Mode
2. Multithreaded webpage parsing
3. Create Summary and time for download at end of program

##Known Bugs:
1. First page gets downloaded again for each non existant page specified.
2. Original file naming not robust. If the Url has some php at end of jpg the file extension will be affected.
