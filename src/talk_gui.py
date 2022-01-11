#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String
from tkinter import *
from tkinter import ttk
import tkFileDialog
import tkMessageBox
import os
import numpy as np
import glob
import tf
import tf2_ros
from std_msgs.msg import Int8
import yaml
import playsound

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from geometry_msgs.msg import TransformStamped

PUBLISH="/audio/order"
BUTTONS=[
         "Happy",
         "Confusing",
         "Sorrow",
         "Funny",
         "Unbelievable"
]

class TmpButton(Frame):
    def __init__(self, master, frame, num, name):
        self.master = master
        self.frame = frame
        self.num = num
        self.fs = []
        button = ttk.Button(
            self.frame,
            text=name,
            command=self.execute
        )
        button.pack(side=TOP)

    def execute(self,):
        pub = rospy.Publisher(PUBLISH, Int8, queue_size=1)
        data = Int8()
        data.data = self.num
        pub.publish(data)

class Application(Frame):
    def __init__(self, master = None):
        self.master = master
        self.tmp = ttk.Frame(self.master)
        self.tmp.pack(side=TOP)
        label = ttk.Label(self.tmp, text="RoboTalk")        
        label.pack(ipady=10 ,side=TOP)

        self.buttons = []
        self.num = len(BUTTONS)
        for i in range(self.num):
            self.buttons.append(TmpButton(self.master, self.tmp, i, BUTTONS[i]))

if __name__ == "__main__":
    rospy.init_node("audio_gui")
    root = Tk()
    root.title("AudioGui")
    root.geometry("300x400")
    app = Application(master = root)
    root.mainloop()