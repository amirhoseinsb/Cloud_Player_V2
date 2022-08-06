#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 22:37:34 2022

@author: amir
"""
from playsound import playsound
from banner import PLAYER ,SOUND ,CHOICE_PLAY , PLAY ,CHOICE_STOP                       
from sys import exit
import multiprocessing
from time import sleep

class Player:
    
    def __init__(self):
        print(PLAYER)
        self.file_name = input('Please Enter The File Name :')
        self.check_for_exit()
        self.play = input(PLAY)

    def auto_play(self):
        for i in self.music:
            playsound(i)
            
    def check_for_exit(self):
        if self.file_name.lower() == 'x':
            exit()
        else :
            pass
        
    def read_the_file(self):
        self.check_for_exit()
        self.counter = 0
        self.music = []
        try:
            file = open(self.file_name,'r')
            for i in file:
                self.music.append(i)
            file.close()
        except:
            print('FileNotFound! Try Again!')

            
    def next_music(self):
        self.counter +=1
        self.music_.kill()
        self.music_ = multiprocessing.Process(target=playsound, args=(self.music[self.counter],))
        self.music_.start()
        self.select = input(f'{CHOICE_PLAY}').lower()
    
    def previous_music(self):
        self.counter -=1
        self.music_.kill()
        self.music_ = multiprocessing.Process(target=playsound, args=(self.music[self.counter],))
        self.music_.start()
        self.select = input(f'{CHOICE_PLAY}').lower()
    
    def play_music(self):
        self.music_ = multiprocessing.Process(target=playsound, args=(self.music[self.counter],))
        self.music_.start()
        self.select = input(f'{CHOICE_PLAY}').lower()
    
    def stop_music(self):
        self.music_.kill()
        self.select = input(f'{CHOICE_STOP}').lower()
    
    def exit_to_menu(self):
        self.music_.kill()
        print(PLAYER)
        self.file_name = input('Please Enter The File Name :')
    
    def exit_app(self):
        self.music_.kill()
        exit()
        
        
def run():
    
    while True:
        music = Player()
        music.read_the_file()
        if music.play == 'm':
            music.play_music()
            
            while True:
                
                if music.select == 'n':
                    music.next_music()
                    
                elif music.select == 'b':
                    music.previous_music()
                    
                elif music.select == 'p':
                    music.play_music()
                    
                elif music.select == 's':
                    music.stop_music()
                    
                elif music.select == 'x':
                    music.exit_app()
                
                elif music.select == 'c':
                    music.exit_to_menu()
                    music.read_the_file()

                    if music.play == 'm':
                        music.play_music()
                    else :
                        music.auto_play()
        else :
            music.auto_play()

run()