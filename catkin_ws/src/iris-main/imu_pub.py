#!/usr/bin/env python
import rospy
import numpy as np


# publisher function for each input source, publishes to MAP node
simulated = True


""" 
Custom class for storing IMU data

probably missing fields bc i don't know much about imu data

pos:
gyro: 

"""
class imudata:
    def __init__(self, pos, gyro): # python version of a constructor  ?
        pos = pos
        gyro = gyro
    
    # Getters/Setters for fields




def main():
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


def simulated():
    imupub = rospy.Publisher("imu_data", imudata, queue_size = 10 )

    rospy.init_node("pubimu", anonymous = True) # anon is true if there will be multiple puimu nodes running
    rate = rospy.rate(10)
    while not rospy.is_shutdown():
        # do things
        imupub.publish(PLACEHOLDER) 
        rate.sleep()
        pass



def notsimulated():
    pass


    
if __name__ == '__main__':
    try:
        main()
        if (simulated):
            simulated()
        else:
            notsimulated()

    except rospy.ROSInterruptException:
        pass



