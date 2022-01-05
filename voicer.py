#encoding:UTF-8

import keyboard
import playsound

sound1 = 'r2d2.wav'
playsound.playsound(sound1)

class Voicer(object):
    def __init__(self):
        self.voice_whis = 'r2d2.wav'
        self.voice_scratch = 'scratch.wav'
        
        rospy.Subscriber(
            "voice_order",
            Int8MultiArray,
            self.get_order,
            queue_size=10,
        )

    def get_order(self, data):
        self.voice_order = data
        rospy.loginfo(self.voice_order)


    def coloreffect(self, img, f_lev):
        playsound.playsound()
        return 0

    def main(self):
        while not rospy.is_shutdown():
            if self.data_raw != None:

                self.pub.publish()


if __name__ == "__main__":
    rospy.init_node("hsrb/voicer", anonymous=True)
    hsrv = Voicer()
    hsrv.main()