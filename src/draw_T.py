#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from math import radians

def drawT():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=100)
    rospy.init_node('turtlebot_controller', anonymous=True)
    move_cmd = Twist()
    now = rospy.Time.now()
    rate = rospy.Rate(100)

    while rospy.Time.now() < now + rospy.Duration.from_sec(5):
        move_cmd.linear.x = 1.0
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.linear.x = 0
    
    now = rospy.Time.now()
    move_cmd.angular.z = -radians(45)
    while (rospy.Time.now() < now + rospy.Duration.from_sec(2)):
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.angular.z = 0

    now = rospy.Time.now()
    while rospy.Time.now() < now + rospy.Duration.from_sec(1):
        move_cmd.linear.x = 1.0
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.linear.x = 0

    now = rospy.Time.now()
    move_cmd.angular.z = -radians(45)
    while (rospy.Time.now() < now + rospy.Duration.from_sec(2)):
        
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.angular.z = 0

    now = rospy.Time.now()
    while rospy.Time.now() < now + rospy.Duration.from_sec(2):
        move_cmd.linear.x = 1.0
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.linear.x = 0

    now = rospy.Time.now()
    move_cmd.angular.z = radians(45)
    while (rospy.Time.now() < now + rospy.Duration.from_sec(2)):
        
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.angular.z = 0

    now = rospy.Time.now()
    while rospy.Time.now() < now + rospy.Duration.from_sec(4):
        move_cmd.linear.x = 1.0
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.linear.x = 0

    now = rospy.Time.now()
    move_cmd.angular.z = -radians(45)
    while (rospy.Time.now() < now + rospy.Duration.from_sec(2)):
        
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.angular.z = 0

    now = rospy.Time.now()
    while rospy.Time.now() < now + rospy.Duration.from_sec(1):
        move_cmd.linear.x = 1.0
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.linear.x = 0

    now = rospy.Time.now()
    move_cmd.angular.z = -radians(45)
    while (rospy.Time.now() < now + rospy.Duration.from_sec(2)):
        
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.angular.z = 0

    now = rospy.Time.now()
    while rospy.Time.now() < now + rospy.Duration.from_sec(4):
        move_cmd.linear.x = 1.0
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.linear.x = 0

    now = rospy.Time.now()
    move_cmd.angular.z = radians(45)
    while (rospy.Time.now() < now + rospy.Duration.from_sec(2)):
        
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.angular.z = 0

    now = rospy.Time.now()
    while rospy.Time.now() < now + rospy.Duration.from_sec(2):
        move_cmd.linear.x = 1.0
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.linear.x = 0

    now = rospy.Time.now()
    move_cmd.angular.z = -radians(45)
    while (rospy.Time.now() < now + rospy.Duration.from_sec(2)):
        
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.angular.z = 0

    now = rospy.Time.now()
    while rospy.Time.now() < now + rospy.Duration.from_sec(1):
        move_cmd.linear.x = 1.0
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.linear.x = 0

    now = rospy.Time.now()
    move_cmd.angular.z = -radians(45)
    while (rospy.Time.now() < now + rospy.Duration.from_sec(2)):
        
        pub.publish(move_cmd)
        rate.sleep()
    move_cmd.angular.z = 0

if __name__ == '__main__':
    try:
        drawT()
    except rospy.ROSInterruptException:
        pass