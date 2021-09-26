#!/usr/bin/env python3

import rospy
from task2.msg import coordinates_byscle

def publisher():
	pub= rospy.Publisher('coordinates',coordinates_byscle,queue_size=10)
	rate= rospy.Rate(1)
	msg_to_publish	= coordinates_byscle()
	msg_to_publish.x=1
	msg_to_publish.theta=1
	msg_to_publish.y=1
	pub.publish(msg_to_publish)
	rospy.loginfo(msg_to_publish)	
	rate.sleep()
		
		
if __name__ == "__main__":
	rospy.init_node("initial")
	publisher()
