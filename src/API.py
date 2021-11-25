#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String

rospy.init_node('main',anonymous=True)
pub=rospy.Publisher('chatter',String,queue_size=10)

def wallFront():
    global flag
    rate=rospy.Rate(1)
    f="wf"
    pub.publish(f)
    msg=rospy.wait_for_message("chatter",String,timeout=None)
    if msg=="t":
        return True
    else:
        return False



def wallRight():
    global flag
    rate=rospy.Rate(1)
    f="wr"
    pub.publish(f)
    msg=rospy.wait_for_message("chatter",String,timeout=None)
    if msg=="t":
        return True
    else:
        return False


def wallLeft():
    global flag
    rate=rospy.Rate(1)
    f="wl"
    pub.publish(f)
    msg=rospy.wait_for_message("chatter",String,timeout=None)
    if msg=="t":
        return True
    else:
        return False


def moveForward(distance=None):
    rate=rospy.Rate(1)
    f="f"
    pub.publish(f)
    rate.sleep()

def turnRight():
    rate=rospy.Rate(1)
    f="r"
    pub.publish(f)
    rate.sleep()


def turnLeft():
    rate=rospy.Rate(1)
    f="l"
    pub.publish(f)
    rate.sleep()