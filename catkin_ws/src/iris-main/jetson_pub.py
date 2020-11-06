#!/usr/bin/env python
import rospy
import numpy as np


# publisher function for each input source, publishes to MAP node

def placeholder():
    # create publisher
    pub = rospy.Publisher(TOPIC_NAME, CLASS, queue_size=10)
    # intialize node
    rospy.init_node(NODE_NAME, anonymous=False)
    # rate
    rate = rospy.Rate(10) # 10hz

    # while not shutdown
        # publish relevant data
        # sleep rate
        # rate.sleep()



if __name__ == '__main__':
    try:
        placeholder()
    except rospy.ROSInterruptException:
        pass



