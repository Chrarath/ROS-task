#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import rospy
from geometry_msgs.msg import Point


def describe_direction(point):
    x_desc = "正前方" if point.x > 0.1 else "后方" if point.x < -0.1 else "前后居中"
    y_desc = "左侧" if point.y > 0.1 else "右侧" if point.y < -0.1 else "左右居中"
    return x_desc, y_desc


def describe_height(point):
    if point.z < 0.5:
        return "高度偏低"
    if point.z > 1.5:
        return "高度偏高"
    return "高度正常"


def callback(point):
    x_desc, y_desc = describe_direction(point)
    height_desc = describe_height(point)
    distance = math.sqrt(point.x ** 2 + point.y ** 2 + point.z ** 2)

    rospy.loginfo(
        "收到目标点: x=%.2f, y=%.2f, z=%.2f | 方向=%s/%s | %s | 距离=%.2fm",
        point.x,
        point.y,
        point.z,
        x_desc,
        y_desc,
        height_desc,
        distance,
    )


def main():
    rospy.init_node("target_sub")
    rospy.Subscriber("/uav/target_point", Point, callback)
    rospy.loginfo("target_sub 已启动，等待 /uav/target_point 目标点...")
    rospy.spin()


if __name__ == "__main__":
    main()
