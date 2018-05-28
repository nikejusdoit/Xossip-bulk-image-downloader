# Xossip-bulk-image-downloader
This is python code to bulk download images from a xossip thread. (as of 28th May 2018 formatting)
The code can be slightly modified to download images from other famous image boards. Learn Beautiful soup if you wish to DIY or drop me a message on which website you would like next.
## List of steps to use this code.
1. Install Python 3.
2. pip install all required modules in code.
3. Enter in command line "python dlXossip.py -f FOLDER Thread# Start-Page End-Page". or Edit code.
If you cant be bothered with all this, I'll release a simple exe soon.
###### Example
> C:\>python dlXossip.py -f C:\Images\ 1260261 1 50
## Inputs

- Forum Thread number: find this in the URL. For "https://www.xossip.com/showthread.php?t=**1527778**" the thread number is 1527778.

- Thread Start Page Number: Starting Page from which you want to download the images.

- Thread End Page number: Last Page till which you want to download the images.

- Paralell download count: number of paralell image downloads. Higher = faster **Be Responsible. Don't overload host.**

- File Save Location: Specify the folder location. Folder must exist.

- File Name - sequential or original: Sequential renames the images in the order of download. Original retains file name.

- File prefix: prefix for sequential filenames

- File Min Size: Min file size to download. This serves to filter out images of emoticons and other non relevant images.

## Future work required:
1. Add all variables as arguments
2. Verbose Mode
3. Multithreaded webpage parsing (Should not impact host)
4. Create Summary and time for download at end of program
5. Create Exe

## Known Bugs:
1. First page gets downloaded again for each non existant page specified.
2. Original file naming not robust. If the Url has some php at end of jpg the file extension will be affected.
3. Command line status update not robust. Needs Debugging.

