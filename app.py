#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 5 14:58:31 2019

@author: jagruti
"""


from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/Map')
def Map():
   return render_template('Map.html')

@app.route('/Portfolio')
def Portfolio():
   return render_template('Portfolio.html')


if __name__ == '__main__':
   app.run(debug = True)