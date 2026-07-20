#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Point


def make_point(x, y, z):
    point = Point()
    point.x = x
    point.y = y
    point.z = z
    return point


def main():
    rospy.init_node("target_pub")
    pub = rospy.Publisher("/uav/target_point", Point, queue_size=10)
    rate = rospy.Rate(1)

    sample_targets = [
        (1.0, 2.0, 1.6),
        (2.0, -1.0, 1.0),
        (-1.0, 0.5, 0.5),
        (0.0, 0.0, 3.5),
    ]

    index = 0
    while not rospy.is_shutdown():
        x, y, z = sample_targets[index % len(sample_targets)]
        point = make_point(x, y, z)
        pub.publish(point)
        rospy.loginfo("发布目标点: x=%.2f, y=%.2f, z=%.2f", point.x, point.y, point.z)
        index += 1
        rate.sleep()


if __name__ == "__main__":
    main()
