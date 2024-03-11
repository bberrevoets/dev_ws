#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyCustomNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("node_name", parameter_overrides=[])  # MODIFY NAME


def main(args=None):
    rclpy.init(args=args)
    try:
        node = MyCustomNode()  # MODIFY NAME
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("interrupted by keyboard")
    finally:
        node.get_logger().info("Bye ROS")
        rclpy.shutdown()


if __name__ == "__main__":
    main()
