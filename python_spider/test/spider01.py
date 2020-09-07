#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "wang";

import requests;
from bs4 import BeautifulSoup;
import re;

def text_data(url):
    r = requests.get(url);
    return r.text;
    # print(r.text);

def bs4_text(respons_text):
    soup  = BeautifulSoup(respons_text,"html.parser");
    p_all = soup .find(name="div",attrs={"itemprop":"acticleBody"});
    # p_all2 = p_all .find(name="p");
    # p_all = soup.p.contents;
    print(p_all)

if __name__ == "__main__":
    url = "http://book.zongheng.com/chapter/974661/60890956.html"
    r = text_data(url);
    bs4_text(r);

# "http://book.zongheng.com/showchapter/974661.html"
# "http://book.zongheng.com/chapter/974661/60890956.html"