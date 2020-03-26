
# -*- coding: utf-8 -*-
"""
Use with Python3 
"""
import os
import csv
import requests
import urllib
try:
    os.mkdir("SIF_pics")
except:
    pass

for i in range(1,6900):
    try:
        i=str(i)
        url="https://card.niconi.co.ni/card/v4nb/"+i+".png"             
        print("[Now Downloading]" + ""+i+".png")
        filename="SIF_pics/"+i+".png"
        urllib.request.urlretrieve(url,filename)
        print("Done! ")
    except:
        print("Fail! Not exists or Network error")
