from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import string
import time
import re

real_time = 0
first_run = 0
chrome_path = 'chromedriver.exe'
url = 'https://www.youtube.com/watch?v=FhMYFIFWtpk&list=PLkBF5AWJutYdIqaBnBFpdfFA-CnpCWlQd&index=1'

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

def get_timestamps():
    songs = str(driver.page_source)
    start = songs.find('"description":"')
    end = songs.find('"duration":')
    songs_list = songs[start:end]
    start = songs_list.find('Tracklist:')
    songs_list = songs_list[start:end]
    songs_list = songs_list.split('\\n')
    del songs_list[0]
    song_dict = dict() #empty dictionary to add the songs
    
    for i in range(0,len(songs_list)):
        if ' ' in songs_list[i]:
            a,b = songs_list[i].split(' ', 1)
            if hasNumbers(a):
                m,s = a.split(':', 1)
                h = 0 
                if ":" in s:
                    h = m
                    m,s = s.split(':',1)
                _time = int(s) + int(m)*60 + int(h)*3600            
                songs_dict_aux = {_time : b}
                song_dict.update(songs_dict_aux)
    return song_dict 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(chrome_path, options=chrome_options)

driver.get(url)
time.sleep(2)
play_click = ActionChains(driver)
play_click.move_by_offset(740, 520).click().perform() 

def get_songlist():
    songs = str(driver.page_source)
    start = songs.find('"description":"')
    end = songs.find('"thumbnailUrl":')
    songs_list = songs[start:end]
    return songs_list

while(True):
    try:
        if len(driver.find_element_by_class_name('ytp-time-current').text) > 1:
            m,s = driver.find_element_by_class_name('ytp-time-current').text.split(':', 1)
            h = 0 
            if ":" in s:
                h = m
                m,s = s.split(':',1)
            real_time = int(s) + int(m)*60 + int(h)*3600  
    except:
        pass
    time.sleep(1)

    if first_run == 0:
        current_url = driver.current_url
        first_run = 1
        playlist = get_timestamps()
       
    if current_url != driver.current_url:
        first_run = 0
        real_time = 0
        playlist = get_timestamps()
             
    badaras = list(playlist.keys())
    badaras_2 = list(playlist.values())

    for i in range(0,len(badaras)): 
        if i == (len(badaras)-1):
            file1 = open("current_song_to_OBS.txt","w")#write mode 
            file1.write("Now playing: " + str(badaras_2[-1]))
            break
        if (badaras[i] <= real_time) and (badaras[i+1] >= real_time):
            file1 = open("current_song_to_OBS.txt","w")#write mode 
            file1.write("Now playing: " + str(badaras_2[i])) 
               
    real_time += 1