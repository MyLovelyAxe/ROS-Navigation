#! /usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist, PoseWithCovarianceStamped, Pose
from std_srvs.srv import Empty, EmptyRequest

# attention:
#     husky_robot has different command-behaviour with turtlebot
#     when move.linear or move.angular are set,
#     and publish the move,
#     husky_robot only move within one moment,
#     even though 'rate.sleep()' is called;
#     turtlebot behaves on the contrary,
#     it will keep moving when 'move' is published
#     or not?


class move_husky_class():

    def __init__(self):

        # define publisher of '/cmd_vel' and subscriber of '/amcl_pose'
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub = rospy.Subscriber(
            '/amcl_pose', PoseWithCovarianceStamped, self.sub_callback)
        self.move = Twist()

        # define service
        rospy.wait_for_service('/global_localization')
        self.disperse_service_client = rospy.ServiceProxy(
            '/global_localization', Empty)
        self.disperse_service_request = EmptyRequest()

        # define rate
        self.rate = rospy.Rate(5)

    def sub_callback(self, msg):

        self.sub_msg = msg

    def disperse(self):

        rospy.loginfo("calling service......")
        self.disperse_service_result = self.disperse_service_client(
            self.disperse_service_request)
        print(self.disperse_service_result)

    def move_square(self):

        i = 0
        while not rospy.is_shutdown() and i < 4:

            # move forward
            linear_time = 0
            rospy.loginfo("moving forward......")
            while linear_time < 20:
                self.move.linear.x = 0.5
                self.pub.publish(self.move)
                self.rate.sleep()
                linear_time += 1
            self.move.linear.x = 0.0

            # turn
            angular_time = 0
            rospy.loginfo("turning around......")
            while angular_time < 8:
                self.move.angular.z = 0.8
                self.pub.publish(self.move)
                self.rate.sleep()
                angular_time += 1
            self.move.angular.z = 0.0

            i += 1

    def calculate_covariance(self):

        # get covariance of particles
        cov = self.sub_msg.pose.covariance
        rospy.loginfo("cov of x is: " + str(cov[0]))
        rospy.loginfo("cov of y is: " + str(cov[7]))
        rospy.loginfo("cov of z is: " + str(cov[-1]))
        aver_cov = (cov[0] + cov[7] + cov[-1])/3
        rospy.loginfo("the average covariance is: " + str(aver_cov))
        return aver_cov

    def main(self):

        self.disperse()
        aver_cov = 1
        while not aver_cov <= 0.65:
            self.disperse()
            self.move_square()
            aver_cov = self.calculate_covariance()
            if aver_cov <= 0.65:
                rospy.loginfo("the localization is done")
            else:
                rospy.loginfo("the localization need to be continued")


if __name__ == '__main__':
    rospy.init_node('move_husky_node')
    move_husky_instance = move_husky_class()
    move_husky_instance.main()
