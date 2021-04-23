#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
import numpy as np
from std_srvs.srv import Empty

x = 0
y = 0
z = 0
theta = 0

def poseCallback(pose_message):
    global x
    global y
    global z
    global theta
    
    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta

def orientate (xgoal, ygoal):
    
	global x
	global y
	global theta

	velocity_message = Twist()
	cmd_vel_topic = '/turtle1/cmd_vel'

	while(True):
		ka = 1
		desired_angle_goal = math.atan2(ygoal-y, xgoal-x)
		
		if theta < 0:
			theta = theta + 2*math.pi
		
		if desired_angle_goal < 0:
			desired_angle_goal = desired_angle_goal + 2*math.pi
			dtheta = desired_angle_goal - theta
			#print ('theta=', theta)			
			#print ('new_angle=', desired_angle_goal)
		else:
			desired_angle_goal = desired_angle_goal
			dtheta = desired_angle_goal - theta	
			#print ('new_angle=', desired_angle_goal)


		#if abs(desired_angle_goal - theta) < abs((desired_angle_goal + 2*math.pi) - theta):	
		#	dtheta = desired_angle_goal - theta
		#	print ('dtheta=', dtheta)
		#else:
		#	dtheta = desired_angle_goal + 2*math.pi - theta
		#	print ('dtheta=', dtheta)        
		#
		if (abs(dtheta) < 0.005):
			print ('angle', theta*360.00/6.2831, 'reached')
			time.sleep(1)
			break

		
		angular_speed = ka * dtheta

		velocity_message.linear.x = 0.0
		velocity_message.angular.z = angular_speed
		velocity_publisher.publish(velocity_message)
		#print ('x=', x, 'y=', y, 'dtheta=', dtheta, 'theta=',theta)

        
def go_to_goal (xgoal, ygoal):
	    	
	global x
	global y
	global theta

	velocity_message = Twist()
	cmd_vel_topic = '/turtle1/cmd_vel'

         
	while(True):

		ka = 5.0
		desired_angle_goal = math.atan2(ygoal+0.01-y, xgoal+0.01-x)
		#print ('desired_angle=', desired_angle_goal)

		if (desired_angle_goal < 0.0):	
			desired_angle_goal = desired_angle_goal + 6.2831
			#print ('new_angle=', desired_angle_goal)
		else:
			desired_angle_goal = desired_angle_goal	
			#print ('new_angle=', desired_angle_goal)

		dtheta = desired_angle_goal-theta
		#print ('dtheta=', dtheta)        
		angular_speed = ka * (dtheta)	
		

		if (abs(angular_speed) < 0.5):	
			angular_speed = angular_speed
		else:
			angular_speed = 0.0

		kv = 1.0				
		distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
		linear_speed = kv * distance

		if (distance < 0.1):
		    print ('point (', x, ',',  y, ') reached')
		    time.sleep(1)
		    break        

		velocity_message.linear.x = linear_speed
		velocity_message.angular.z = angular_speed
		velocity_publisher.publish(velocity_message)
		#print ('x=', x, 'y=', y)

        

if __name__ == '__main__':
	try:

		rospy.init_node('turtlesim_motion_pose', anonymous = True)

		cmd_vel_topic = '/turtle1/cmd_vel'
		velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

		position_topic = "/turtle1/pose"
		pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)


		
		#Cuadrado
		orientate(10.0,1.0)
		time.sleep(0.5)
		go_to_goal(10.0,1.0)
		time.sleep(0.5)
		
		orientate(10.0,10.0)
		time.sleep(0.5)
		go_to_goal(10.0,10.0)
		time.sleep(0.5)
		
		orientate(1.0,10.0)
		time.sleep(0.5)
		go_to_goal(1.0,10.0)
		time.sleep(0.5)
		
		orientate(1.0,1.0)
		time.sleep(0.5)
		go_to_goal(1.0,1.0)
		time.sleep(0.5)	

		#Círculo
		#radio = 4.5;
		#iteraciones = 77;
		#ang = [];
		#for i in range(1,iteraciones):
		#	ang = np.append(ang, 2*math.pi/iteraciones*i);
		#for i in ang:
		#	orientate(radio*math.cos(i)+5.5,radio*math.sin(i)+5.5)
		#	time.sleep(0.5)
		#	go_to_goal(radio*math.cos(i)+5.5,radio*math.sin(i)+5.5)
		#	time.sleep(0.5)
		#orientate(10,5)
		#time.sleep(0.5)
		#go_to_goal(10,5)
		#time.sleep(0.5)
		


	except rospy.ROSInterruptException:        
		pass
		
		

