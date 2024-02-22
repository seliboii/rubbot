#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_default

from robp_interfaces.msg import DutyCycles
import sys, select, termios, tty

settings = termios.tcgetattr(sys.stdin)

class wheel_controller(Node):

    def __init__(self):

        super().__init__('wheel_controller')


msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
"""

moveBindings = {
		'i':(1,0,0,0),
		'o':(1,0,0,-1),
		'j':(0,0,0,1),
		'l':(0,0,0,-1),
		'u':(1,0,0,1),
		',':(-1,0,0,0),
		'.':(-1,0,0,1),
		'm':(-1,0,0,-1),
		'O':(1,-1,0,0),
		'I':(1,0,0,0),
		'J':(0,1,0,0),
		'L':(0,-1,0,0),
		'U':(1,1,0,0),
		'<':(-1,0,0,0),
		'>':(-1,-1,0,0),
		'M':(-1,1,0,0),
		't':(0,0,1,0),
		'b':(0,0,-1,0),
	       }

speedBindings={
		'q':(1.1,1.1),
		'z':(.9,.9),
		'w':(1.1,1),
		'x':(.9,1),
		'e':(1,1.1),
		'c':(1,.9),
	      }

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


def vels(speed,turn):
	return "currently:\tspeed %s\tturn %s " % (speed,turn)

def main(args=None):	
	if args is None:
		args = sys.argv

	rclpy.init(args)
	node = rclpy.create_node('teleop_twist_keyboard')
		
	pub = node.create_publisher(DutyCycles, 'cmd_vel', 	qos_profile_default)

	speed = 0.5
	turn = 1.0
	x = 0
	y = 0
	z = 0
	th = 0
	status = 0

	try:
		while(1):
			key = getKey()
			print(key)
			# if key in moveBindings.keys():
			# 	x = moveBindings[key][0]
			# 	y = moveBindings[key][1]
			# 	z = moveBindings[key][2]
			# 	th = moveBindings[key][3]
			# elif key in speedBindings.keys():
			# 	speed = speed * speedBindings[key][0]
			# 	turn = turn * speedBindings[key][1]

			# 	print(vels(speed,turn))
			# 	if (status == 14):
			# 		print(msg)
			# 	status = (status + 1) % 15
			# else:
			# 	x = 0
			# 	y = 0
			# 	z = 0
			# 	th = 0
			# 	if (key == '\x03'):
			# 		break


	except:
		print('')

	finally:
		# twist = Twist()
		# twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
		# twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
		# pub.publish(twist)

		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)