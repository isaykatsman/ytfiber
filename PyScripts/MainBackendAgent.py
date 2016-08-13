import sys, os, random
#import mechanize
from selenium import webdriver
import time
#import urllib2
#print urllib2.urlopen('http://cnn.com').read()

#use chrome driver
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/home/isaykatsman/Desktop/client_destination"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = './chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

#stealth mode, for deployment - make browser head invisible
#driver.set_window_size(0, 0)
#driver.set_window_position(-2000, 0);

os.environ['webdriver.chrome.driver'] = chromedriver
driver.get("http://mp3fiber.com")

#load in file with url on each line
urls = open('urls_only.txt','r')

#go through each url and download
for line in urls:
    print line
    old_url = driver.current_url #save this current url

    #fill out link
    vidlink = driver.find_element_by_name('videoURL')
    vidlink.send_keys(line)

    # now click on link
    print "will now download"
    link = driver.find_element_by_name('submit')
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
        if driver.current_url != old_url:
            print "fetching download link"
            link = driver.find_element_by_link_text('Download Now!')
            print "right before download"
            time.sleep(1)
            link.click()
            print "clicked and pausing"
            #pause a bit for download to take place
            time.sleep(5)

            break

        #check if frozen, then reload page and go to next
        time_accum = int(time.time()) - time_old
        if time_accum > 120: #more than two minutes
            print "Skipping!!!"
            #reload original page
            driver.get("http://mp3fiber.com")
            break
    #found and clicked url


#finally, close file
urls.close()

#quite browser
driver.quit()