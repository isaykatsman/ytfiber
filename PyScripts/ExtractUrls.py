import sys, os, random
from selenium import webdriver

#file from which urls will be parsed
bookmarksHTML = 'file://'+'/home/isaykatsman/Desktop/music3.html'

#use chrome driver
chromedriver = '/home/isaykatsman/Desktop/MusicFiber/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(bookmarksHTML)

ListlinkerHref = driver.find_elements_by_xpath("//*[@href]")
count = ListlinkerHref.__len__()

print 'Total of: ' + str(count)

#open file for writing
urls_only = open('/home/isaykatsman/Desktop/MusicFiber/urls_only.txt', 'w+')

#write out the urls
for i in range(0,count):
    urls_only.write(ListlinkerHref[i].get_attribute('href')+'\n')
    print ListlinkerHref[i].get_attribute('href')

#close file and quite browser
urls_only.close()
driver.quit()