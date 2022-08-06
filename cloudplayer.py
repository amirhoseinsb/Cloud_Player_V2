#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 17:12:53 2022

@author: amir
"""

from selenium import webdriver
from banner import BANNER
from config import options,PATH
from bs4 import BeautifulSoup
import requests
from sys import exit

class CloudPlayer:
    def __init__(self):
        print(BANNER)
        self.singer_name = input('Please Enter The Singer Name : ')
        if self.singer_name.lower() != 'x':
            pass
        else :
            exit()
            
    def request_google(self):
        self.driver = webdriver.Chrome(PATH, chrome_options=options)
        self.driver.get(f'https://www.google.com/search?q=intitle:index%20of%20mp3%20intext:{self.singer_name}')

    def site_view(self):
        self.site = self.driver.find_elements_by_css_selector('.yuRUbf > a')
    
    def site_list(self):
        self.list_site = []
        for i in self.site:
            x = i.get_attribute('href')
            self.list_site.append(x)
    
    def request_site(self):
        self.result = []
        for i in self.list_site:
            x = requests.get(i)
            self.result.append(x)
            
    def find_music(self):
        self.music = []
        for i in self.result:
            soup = BeautifulSoup(i.content,'html.parser')
            content = soup.select('a')
            self.music.append(content)
    
    def find_music_link(self):
        self.music_link = []
        counter_varieble = 0
        self.counter_music = 0
        for i in range(9):
             for i in self.music[counter_varieble]:
                 try:
                     if 'mp3' in i.get('href'):
                         url = self.result[counter_varieble].url
                         music = i.get('href')
                         print(f'\n{self.counter_music}:{url}{music}') 
                         self.music_link.append(f'{url}{music}')
                         self.counter_music +=1
                 except TypeError:
                     print('TypeError')
             if counter_varieble !=9:
                 counter_varieble+=1
             else :
                 break
             
    def write_disk(self):
        with open (f'{self.singer_name}','w') as f:
            for i in self.music_link:
                f.write(f'{i}\n')
            print(f'''
    save in the file {self.singer_name} !
    -------------------------------------
    You can play the desired file using 
    the player in the directory.
                  ''')
                    



          