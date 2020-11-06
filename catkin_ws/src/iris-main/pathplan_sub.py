#!/usr/bin/env python

import rospy
import numpy as np

# Pathplanning subscriber to the MAP node


# need callback function
def callback(data): # called when new msgs recieved
    pass

def placeholder():
    # initalize node
    # creates subscriber
    rospy.Subscriber("topicname", msgtype, callback) 
    # spin
    rospy.spin()


if __name__ == '__main__':
    placeholder()
