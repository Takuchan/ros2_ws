import rclpy
from rclpy.node import Node

class HappyNode(Node):
  def __init__(self):
    print("I'm love it!")
    super().__init__('happy_node')
    self.get_logger().info('HappyWorld!!')

def main():
    print('Hi from gazo.')
    rclpy.init()
    node = HappyNode()
    rclpy.shutdown()
    print('program end')


if __name__ == '__main__':
    main()
