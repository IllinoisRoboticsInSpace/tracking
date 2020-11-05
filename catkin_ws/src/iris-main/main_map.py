#!/usr/bin/env python
import rospy
import numpy as np

local_map = np.array((insert_dimensions_here))

def placeholder():
    # set up subscribers to:
    # - imu
    # - jetson
    # - realsense
    # - Any other sensors (none as of now)

    # update local map data structure as sensor data determines
    # pass
    
    rospy.init_node('main_map')

    # TODO

    rospy.spin()    # Keep python from exiting until the node is stopped

def process_sensor_input(): # rename this function and write it

if __name__ == '__main__':
    try:
        placeholder()
    except rospy.ROSInterruptException:
      