#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import playsound
from std_msgs.msg import Int8
'''
         "Happy",
         "Confusing",
         "Sorrow",
         "Funny",
         "Unbelievable"
'''
voice0 = 'catkin_ws/src/hsr_voicer/src/Excited.wav'
voice1 = 'catkin_ws/src/hsr_voicer/src/Confused.wav'
voice2 = 'catkin_ws/src/hsr_voicer/src/Sad.wav'
voice3 = 'catkin_ws/src/hsr_voicer/src/Playful.wav'
voice4 = 'catkin_ws/src/hsr_voicer/src/Unbelievable.wav'

class Player(object):
    def __init__(self):
        self.order_raw = None
        rospy.Subscriber( "/audio/order", Int8, self.get_order, queue_size=1)

    def get_order(self, data):
        self.order_raw = data
        rospy.loginfo("raw_order:")
        rospy.loginfo(self.order_raw)

    def voiceplayer(self, data):
        if data.data==0:
            playsound.playsound(voice0)
        if data.data==1:
            playsound.playsound(voice1)
        if data.data==2:
            playsound.playsound(voice2)
        if data.data==3:
            playsound.playsound(voice3)
        if data.data==4:
            playsound.playsound(voice4)           

    def main(self):
        while not rospy.is_shutdown():
            if self.order_raw != None:
                _data = self.order_raw
                self.order_raw = None
                pv=self.voiceplayer(_data)


if __name__ == "__main__":
    rospy.init_node("audio_voicer")
    hsrvoice = Player()
    hsrvoice.main()
