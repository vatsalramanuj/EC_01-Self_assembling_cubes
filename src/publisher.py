#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
import main


def talker():
    pub = rospy.Publisher('coordinates_out', Float32MultiArray, queue_size=10)
    rospy.init_node('int_publisher')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data_input = main.cam()
        num_msg1 = Float32MultiArray(data = data_input)
        pub.publish(num_msg1)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass