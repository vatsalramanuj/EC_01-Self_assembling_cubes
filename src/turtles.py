#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from math import radians


class TurtleBot:

    def line_move():
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 100)
        
        speed = 1
        
        rate = rospy.Rate(10)
        
        vel_msg = Twist()
        vel_msg.linear.x = speed
        
        t0 = rospy.Time.now()
        
        
        
        while rospy.Time.now() < t0 + rospy.Duration.from_sec(5/speed):    
            velocity_publisher.publish(vel_msg)
            rate.sleep()
            
            
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

    def angle_move():
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 100)
        vel_msg = Twist()
        ang_speed = radians(45)
        vel_msg.angular.z = ang_speed
        t0 = rospy.Time.now()
        rate = rospy.Rate(10)
        

        while (rospy.Time.now() < t0 + rospy.Duration.from_sec(radians(90)/ang_speed)):
            velocity_publisher.publish(vel_msg)
            rate.sleep()

        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)	

    def square():
        rospy.init_node('turtlebot_controller', anonymous=True)

        sides_travelled = 0
        while sides_travelled < 4:
            TurtleBot.line_move()
            TurtleBot.angle_move()
            sides_travelled += 1


if __name__ == '__main__':
    try:
        TurtleBot.square()
    except rospy.ROSInterruptException:
        pass