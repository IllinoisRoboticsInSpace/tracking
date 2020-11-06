#!/usr/bin/env python
import rospy
import numpy as np

local_map = np.array((insert_dimensions_here))

# def callback_imu(data):
    # rospy.loginfo(rospy.get_caller_id() + " received data from imu %s", data.range)
    # Will be publishing robot displacement, some form of deltaX deltaY
    # This will be used to update the system
    # For now, assume this won't be publishing anything
    # TODO

# def callback_jetson(data):
    # rospy.loginfo(rospy.get_caller_id() + " received data from jetson %s", data.range)
    # IF this is running a NN, might be publishing a list of obstacles.
    # For now, assume this won't be publishing anything
    # TODO

def callback_realSense(data):
    rospy.loginfo(rospy.get_caller_id() + " received data from realSense %s", data.range)
    # Has a ROS interface, and use this fordata purposes
    # Probably where we're going to get the data from
    # TODO


def main_map_listener():
    # set up subscribers to:
    # - imu
    # - jetson
    # - realsense
    # - Any other sensors (none as of now)

    # update local map data structure as sensor data determines
    # pass
    
    rospy.init_node('main_map')
    # rospy.Subscriber("<TOPIC>", <DATA_TYPE>, callback_imu)        # Will probably be removed
    # rospy.Subscriber("<TOPIC>", <DATA_TYPE>, callback_jetson)     # Will probably be removed 
    rospy.Subscriber("/camera/accel/imu_info", <DATA_TYPE>, callback_realSense)     # Need to setup realsense node before we know the topic name 

    # TODO

    rospy.spin()    # Keep python from exiting until the node is stopped

def process_sensor_input(): # rename this function and write it

if __name__ == '__main__':
    try:
        main_map_listener()
    except rospy.ROSInterruptException:
      