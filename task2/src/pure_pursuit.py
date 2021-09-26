#!/usr/bin/env python3
import rospy
import math
import time
from task2.msg import sv_pure
from task2.msg import path_error
L=2
def subscriber():
	rospy.loginfo("da5alt el subscriber")
	sub = rospy.Subscriber('error',path_error,callback_function)
	rate = rospy.Rate(1)
	rospy.spin()
def callback_function(message):
	rospy.loginfo("gatlak resala")
	pub = rospy.Publisher('steering_velocity',sv_pure, queue_size=10)
	rate = rospy.Rate(1)
	data=sv_pure()
	data.steering = math.atan ( 2 * L * math.sin(message.alpha) / (message.ld) )	
	data.v=10
	time.sleep(0.7)
	pub.publish(data)
	rospy.loginfo(data.steering)
	rospy.loginfo(data.v)
	


if __name__== '__main__' :
	rospy.init_node('pure_pursuit')
	subscriber()
