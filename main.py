#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:22:11 2022

@author: amir
"""
from cloudplayer import CloudPlayer

def run_project():
    site = CloudPlayer()
    site.request_google()
    site.site_view()
    site.site_list()
    site.request_site()
    site.find_music()
    site.find_music_link()
    site.write_disk()

while True:
    run_project()