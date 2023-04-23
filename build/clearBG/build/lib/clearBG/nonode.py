import rclpy
from rclpy.node import Node

class HappyNode(Node):
  def __init__(self):
    print("I'm love it!")
    super().__init__('happy_node')
    for a in range(100):
      self.get_logger().info('HappyWorld!!')
    self.timer = self.create_timer(1.0,self.timer_callback)

  def timer_callback(self):
    self.get_logger().info('HappyWororororo!!')

def main():
    print('Hi from gazo.')
    rclpy.init()
    node = HappyNode()
    rclpy.spin(node)
    rclpy.shutdown()
    print('program end')


if __name__ == '__main__':
    main()

