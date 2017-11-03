###SANS Extractor -
###simply extracts the show notes for any or all ISC shows from isc.sans.edu.podcastdetail.html
###
###github.com/thegrayninja
###
##Version 0.2.0
##Version Notes:    Added Q/A, fixed number of shows to save
##
##Ver 0.1.1 Reverses the order of results, and removes comments out the print(findings)
##Ver 0.1.0 - Saves results as .html, creates links for each topic


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import sys


def MainBanner():
    banner = '''\n

  _________   _____    _______    _________ ___________         __                        __                
 /   _____/  /  _  \   \      \  /   _____/ \_   _____/__  ____/  |_____________    _____/  |_  ___________ 
 \_____  \  /  /_\  \  /   |   \ \_____  \   |    __)_\  \/  /\   __\_  __ \__  \ _/ ___\   __\/  _ \_  __ \\
 /        \/    |    \/    |    \/        \  |        \>    <  |  |  |  | \// __ \\\\  \___|  | (  <_> )  | \/
/_______  /\____|__  /\____|__  /_______  / /_______  /__/\_ \ |__|  |__|  (____  /\___  >__|  \____/|__|   
        \/         \/         \/        \/          \/      \/                  \/     \/                   

teamHAWK\nv0.2.0\n\n            
'''
    return(banner)


def CheckPythonVersion():
    PyVerTuple = sys.version_info[:1]
    if PyVerTuple[0] > 2:
        return 0
    else:
        print("\n\nPlease run Python 3.x or newer\n")
        sys.exit(1)


def GetOSVersion():
    return(platform.system())



def GetCurrentShowID():

    url = 'https://isc.sans.edu/podcastdetail.html'
    uClient = uReq(url)
    pageContent = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(pageContent, "html.parser")

    id = page_soup.findAll('meta')

    return (str(id[22]).split("id=")[1].split('"')[0])


#def DownloadURLS(MinShowID, CurrentShowID):
def DownloadURLS(DownloadCount, CurrentShowID):
    findings = ""
    DownloadsRemaining = int(DownloadCount)

    DownloadsRemaining = ((DownloadsRemaining -1)*2)
    while DownloadsRemaining >= 0:
        url = 'https://isc.sans.edu/podcastdetail.html?id=%s' % (CurrentShowID)
        uClient = uReq(url)
        pageContent = uClient.read()
        uClient.close()

        # html parsing
        page_soup = soup(pageContent, "html.parser")
        showNotes = page_soup.blockquote


        titles = []
        urls = []


        dailyLinks = showNotes.find_all('a')
        counter = 0


        for i in showNotes.contents:
            if i != ' ':
                try:
                    titles.append(i.strip())
                    urls.append(dailyLinks[counter].text)

                    header = i.strip()
                    links = dailyLinks[counter].text
                    date = page_soup.h2.text.split(',')[1].strip()

                    findings += "* %s - %s - <a href='%s' target=_blank>%s</a><br />" % (CurrentShowID, date, links, header)
                    counter += 1

                except:
                    continue

        DownloadsRemaining -= 1

        time.sleep(.2)  #adjust so you don't get blocked by sans.edu

        CurrentShowID = int(CurrentShowID) - 1

    #print(findings)


    TempFile= open("SANS_ShowNotes.html", "w")
    TempFile.write(findings)
    TempFile.close()

    print("\n\nYour show notes have been saved to .\SANS_ShowNotes.html!!!!!\n\n")



def menu():
    CurrentShowID = GetCurrentShowID()
    DownloadCount = input("\nEnter q to quit\nEnter the number of shows you wish to download. Enter 0 for all: ")
    if (DownloadCount == 'q') or (DownloadCount == 'Q'):
        sys.exit(1)

    try:
        int(DownloadCount)

        if DownloadCount == '0':
            DownloadAll = int(CurrentShowID)
            DownloadAll /= 2
            DownloadAll = int(DownloadAll)
            DownloadURLS(DownloadAll, CurrentShowID)

        elif int(DownloadCount) < 1:
            print("Please enter a number larger than 0.")
            menu()
        else:
            DownloadURLS(DownloadCount, CurrentShowID)

    except:
        print("\n\nAn error occurred. Perhaps you entered a character, space, or a negative number.")
        menu()

    return 0



def main():
    print(MainBanner())
    CheckPythonVersion()
    menu()


if __name__ == main():
    main()
