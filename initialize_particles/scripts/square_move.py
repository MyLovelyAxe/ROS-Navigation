#! /usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist, PoseWithCovarianceStamped, Pose

# attention:
#     husky_robot has different command-behaviour with turtlebot
#     when move.linear or move.angular are set,
#     and publish the move,
#     husky_robot only move within one moment,
#     even though 'rate.sleep()' is called;
#     turtlebot behaves on the contrary,
#     it will keep moving when 'move' is published
#     or not?


def callback(msg):

    for i in range(4):

        rate = rospy.Rate(5)

        # move forward
        linear_time = 0
        while linear_time < 20:
            rospy.loginfo("moving forward")
            move.linear.x = 0.5
            pub.publish(move)
            rate.sleep()
            linear_time += 1
        move.linear.x = 0.0

        # turn
        angular_time = 0
        while angular_time < 8:
            rospy.loginfo("turning around")
            move.angular.z = 0.8
            pub.publish(move)
            rate.sleep()
            angular_time += 1
        move.angular.z = 0.0

    # get covariance of particles
    cov = msg.pose.covariance
    print("cov of x is: ", cov[0])
    print("cov of y is: ", cov[7])
    print("cov of z is: ", cov[-1])


rospy.init_node('square_move_node')
sub = rospy.Subscriber(
    '/amcl_pose', PoseWithCovarianceStamped, callback)
pub = rospy.Publisher(
    '/cmd_vel', Twist, queue_size=1)
move = Twist()
rospy.spin()
