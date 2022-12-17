#! /usr/bin/env python
import rospy
from nav_msgs.srv import GetMap, GetMapRequest


def main():
    rospy.init_node('service_client')
    rospy.wait_for_service('/static_map')
    getmap_service_client = rospy.ServiceProxy('/static_map', GetMap)
    getmap_request = GetMapRequest()
    result = getmap_service_client(getmap_request)
    print(result)


if __name__ == '__main__':
    main()
