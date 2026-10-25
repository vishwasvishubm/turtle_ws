import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')

        self.declare_parameter('speed', 2.0)
        self.declare_parameter('turtle_topic', '/turtle1/cmd_vel')

        speed = self.get_parameter('speed').value
        turtle_topic = self.get_parameter('turtle_topic').value

        self.speed = float(speed)
        self.turtle_topic = turtle_topic
        self.timer_count = 0

        self.publisher = self.create_publisher(
            Twist,
            self.turtle_topic,
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.move_turtle
        )

    def move_turtle(self):
        self.timer_count += 1

        msg = Twist()

        if self.timer_count <= 20:
            msg.linear.x = self.speed
            msg.angular.z = 0.0

        elif self.timer_count <= 28:
            msg.linear.x = 0.0
            msg.angular.z = 2.0

        else:
            self.timer_count = 0

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = TurtleController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
