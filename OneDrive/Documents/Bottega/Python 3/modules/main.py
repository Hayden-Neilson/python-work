# main.py file
import sys
sys.path.insert(0, './libs')
# from helper import greeting
import helper as h
# helper

def render():
    print(h.greeting('Kristine', 'Hudgens'))


render()