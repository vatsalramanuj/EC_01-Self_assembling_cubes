#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray

def num_cb(data):
    coordinates = data.data
    print(coordinates)
    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('int_suubscriber', anonymous=True)

    rospy.Subscriber("coordinates_out", Float32MultiArray, num_cb)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()