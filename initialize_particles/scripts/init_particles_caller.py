#! /usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyRequest


def main():

    rospy.init_node('initialize_particles_node')
    rospy.wait_for_service('/global_localization')
    init_part_service = rospy.ServiceProxy(
        '/global_localization', Empty)
    init_part_request = EmptyRequest()
    result = init_part_service(init_part_request)
    print(result)


if __name__ == "__main__":
    main()
