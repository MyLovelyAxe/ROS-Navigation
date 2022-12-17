#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult


class send_goal_class():

    def __init__(self):

        self.client = actionlib.SimpleActionClient(
            '/move_base', MoveBaseAction)
        rospy.loginfo('waiting for action server: /move_base......')
        self.client.wait_for_server()
        rospy.loginfo('the action server is found')
        self.goal = MoveBaseGoal()

    def feedback_callback(self, feedback):

        rospy.loginfo('robot is going to the pose......')

    def main(self):

        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.x = 2
        self.goal.target_pose.pose.position.y = 2
        self.goal.target_pose.pose.position.z = 0
        self.goal.target_pose.pose.orientation.x = 0
        self.goal.target_pose.pose.orientation.y = 0
        self.goal.target_pose.pose.orientation.z = 0.75
        self.goal.target_pose.pose.orientation.w = 0.66

        self.client.send_goal(self.goal, feedback_cb=self.feedback_callback)

        self.client.wait_for_result()
        rospy.loginfo('result is: ' + str(self.client.get_state()))


if __name__ == "__main__":

    rospy.init_node('send_goal_client_node')
    SendGoal = send_goal_class()
    SendGoal.main()
