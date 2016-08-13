import sys, os, random
#import mechanize
from selenium import webdriver
import time
#import urllib2
#print urllib2.urlopen('http://cnn.com').read()

print "hi"

#use chrome driver
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/home/isaykatsman/Desktop/Music/Music3"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = '/home/isaykatsman/Desktop/MusicFiber/chromedriver'
ff = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
os.environ['webdriver.chrome.driver'] = chromedriver
ff.get("http://mp3fiber.com")

#load in file with url on each line
urls = open('/home/isaykatsman/Desktop/MusicFiber/urls_only.txt','r')

#go through each url and download
for line in urls:
    print line
    old_url = ff.current_url #save this current url

    #fill out link
    vidlink = ff.find_element_by_name('videoURL')
    vidlink.send_keys(line)

    # now click on link
    print "will now download"
    link = ff.find_element_by_name('submit')
    time.sleep(1)
    #link.click() <- not necessary when finding by name

    #now waiting to download
    print "now waiting to download"
    time.sleep(3)
    # now when finished, should be able to click Download
    time_old = int(time.time())
    time_accum = 0

    #TODO: timeouts ~1 out of 60 times, fix is to wait until element is clickable, check bookmarks for selenium tut

    while True:
        time.sleep(1)
        if ff.current_url != old_url:
            print "fetching download link"
            link = ff.find_element_by_link_text('Download Now!')
            print "right before download"
            time.sleep(1)
            link.click()
            print "clicked and pausing"
            #pause a bit for download to take place
            time.sleep(5)

            break

        #check if frozen, then reload page and go to next
        time_accum = int(time.time()) - time_old
        if time_accum > 30:
            print "Skipping!!!"
            #reload original page
            ff.get("http://mp3fiber.com")
            break
    #found and clicked url


#finally, close file
urls.close()

#quite browser
ff.quit()