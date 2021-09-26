#!/usr/bin/env python3
import rospy
import math
from task2.msg import sv_pure
from task2.msg import coordinates_byscle
pub2 = rospy.Publisher("coordinates",coordinates_byscle, queue_size=10)
def initial():
	
	rate = rospy.Rate(1)
	initiation=coordinates_byscle()
	initiation.x=1
	x=initiation.x
	initiation.y=1
	y=initiation.y
	initiation.theta=1
	theta=initiation.theta
	pub2.publish(initiation)
	rospy.loginfo(x)
	rospy.loginfo(y)
	rospy.loginfo(theta)
def subscriber():
	rospy.loginfo("da5alt el subscriber")
	sub = rospy.Subscriber('steering_velocity',sv_pure,callback_function)
	rospy.spin()

def callback_function(message):
	rospy.loginfo("gatlak resala")
	
	if(flag==0):
		delta=4
		velocity=10
	flag=1
	data=coordinates_byscle()
	velocity=message.v
	delta = message.steering
	l = 2
	theta=30
	delta_t = 0.0
	theta_dot = (velocity*math.tan(delta)/l)
	y_dot = v*math.sin(theta)
	x_dot = v *math.cos(theta)
	
	x=x_dot*1  # the time step is 1 as the frequency is 1hz 
	data.x=x
	y=y_dot*1
	data.y=y
	theta_dot*1
	data.theta=theta
	rospy.loginfo(data.x)
	rospy.loginfo(data.y)
	rospy.loginfo(data.theta)
	rospy.loginfo("\n")
	pub2.publish(data)	
	rate.sleep()

if __name__ == "__main__":
	rospy.init_node("bicycle_model")
	subscriber()

