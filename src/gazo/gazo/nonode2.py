import rclpy
from rclpy.node import Node


class HappyNode2(Node):
  def __init__(self):
    super().__init__('happynode')
    self.timer = self.create_timer(1.0,self.timer_callback)

  def timer_callback(self):
    self.get_logger().info('happyWorld!!!')

def main():
  print('Start Program!')
  rclpy.init()
  node =HappyNode2()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    print('You pushed Ctrl + C !')

  rclpy.shutdown()
  print('finish program!')
  
