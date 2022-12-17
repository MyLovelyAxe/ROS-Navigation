#! /usr/bin/env python
import rospy
from nav_msgs.srv import GetPlan, GetPlanRequest
#######   /make_plan only make plan but not execute it   ######

# rosservice info /move_base/make_plan:

# Node: /move_base
# URI: rosrpc://2_xterm:35301
# Type: nav_msgs/GetPlan
# Args: start goal tolerance

# cat GetPlan.srv:

# # Get a plan from the current position to the goal Pose

# # The start pose for the plan
# geometry_msgs/PoseStamped start

# # The final pose of the goal position
# geometry_msgs/PoseStamped goal

# # If the goal is obstructed, how many meters the planner can
# # relax the constraint in x and y before failing.
# float32 tolerance
# ---
# nav_msgs/Path plan

# rossrv show nav_msgs/GetPlan:

# geometry_msgs/PoseStamped start
#   std_msgs/Header header
#     uint32 seq
#     time stamp
#     string frame_id
#   geometry_msgs/Pose pose
#     geometry_msgs/Point position
#       float64 x
#       float64 y
#       float64 z
#     geometry_msgs/Quaternion orientation
#       float64 x
#       float64 y
#       float64 z
#       float64 w
# geometry_msgs/PoseStamped goal
#   std_msgs/Header header
#     uint32 seq
#     time stamp
#     string frame_id
#   geometry_msgs/Pose pose
#     geometry_msgs/Point position
#       float64 x
#       float64 y
#       float64 z
#     geometry_msgs/Quaternion orientation
#       float64 x
#       float64 y
#       float64 z
#       float64 w
# float32 tolerance
# ---
# nav_msgs/Path plan
#   std_msgs/Header header
#     uint32 seq
#     time stamp
#     string frame_id
#   geometry_msgs/PoseStamped[] poses
#     std_msgs/Header header
#       uint32 seq
#       time stamp
#       string frame_id
#     geometry_msgs/Pose pose
#       geometry_msgs/Point position
#         float64 x
#         float64 y
#         float64 z
#       geometry_msgs/Quaternion orientation
#         float64 x
#         float64 y
#         float64 z
#         float64 w


class make_plan_class():

    def __init__(self):

        # define a client of the service '/move_base/make_plan'
        self.makeplan_service_client = rospy.ServiceProxy(
            '/move_base/make_plan', GetPlan)
        rospy.loginfo('waiting for the service: ')
        rospy.loginfo('/move_base/make_plan')
        self.makeplan_service_client.wait_for_service()
        self.makeplan_request = GetPlanRequest()

    def main(self):

        # define the start pose
        self.makeplan_request.start.header.frame_id = 'map'
        self.makeplan_request.start.pose.position.x = 6
        self.makeplan_request.start.pose.position.y = 7
        self.makeplan_request.start.pose.position.z = 0
        self.makeplan_request.start.pose.orientation.x = 0
        self.makeplan_request.start.pose.orientation.y = 0
        self.makeplan_request.start.pose.orientation.z = 0.88
        self.makeplan_request.start.pose.orientation.w = 0.3

        # define the goal pose
        self.makeplan_request.goal.header.frame_id = 'map'
        self.makeplan_request.goal.pose.position.x = 2
        self.makeplan_request.goal.pose.position.y = 3
        self.makeplan_request.goal.pose.position.z = 0
        self.makeplan_request.goal.pose.orientation.x = 0
        self.makeplan_request.goal.pose.orientation.y = 0
        self.makeplan_request.goal.pose.orientation.z = 0.36
        self.makeplan_request.goal.pose.orientation.w = 0.46

        self.makeplan_result = self.makeplan_service_client(
            self.makeplan_request)
        rospy.loginfo('the result is shown as below: ')
        print(self.makeplan_result)


if __name__ == '__main__':
    rospy.init_node('my_make_plan_node')
    MakePlan = make_plan_class()
    MakePlan.main()
