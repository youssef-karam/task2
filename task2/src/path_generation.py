#!/usr/bin/env python3
import rospy
import math
import numpy as np
import time
from task2.msg import path_error
from task2.msg import coordinates_byscle

def subscriber():
	rospy.loginfo("da5alt el subscriber")
	sub = rospy.Subscriber('coordinates',coordinates_byscle,callback_function)
	rospy.spin()

	
def callback_function(message):
	rospy.loginfo("gatlak resala")
	byscle_x= message.x
	byscle_y= message.y
	byscle_theta= message.theta
	data=path_error()
	pub = rospy.Publisher('error',path_error, queue_size=10)
	rate = rospy.Rate(1)
	rospy.loginfo(byscle_x)
	rospy.loginfo(byscle_y)
	rospy.loginfo(byscle_theta)
	rospy.loginfo("\n")
	
	data.ld=10     #ld=k*v=1*10 in m
	while(x<5000):
		y=math.cos(x)
		distance = math.sqrt((byscle_x-x)**2+(byscle_y-y)**2)
		if (distance>(ld-2) and distance<(ld+2)):
			break
	rospy.loginfo("x= %s", x)
	rospy.loginfo("y= %s", y)		
	delta_x = (x-byscle_x)
	delta_y = (y-byscle_y)
	if (delta_x ==0): 
		slope = math.pi/2
	elif (delta_y == 0):
		slope = 0
	else:	
		slope = delta_y / delta_x
	if (slope>0):
		data.alpha = (math.atan(slope))-byscle_theta
	if (tan_theta_plus_alpha<0):
		data.alpha = -(math.atan(slope))-byscle_theta
	time.sleep(0.7)
	pub.publish(data)
	rospy.loginfo(data.alpha)
	rospy.loginfo(data.ld)
	rospy.loginfo("\n")

if __name__ == "__main__":
	rospy.init_node("path_generation")
	subscriber()	


