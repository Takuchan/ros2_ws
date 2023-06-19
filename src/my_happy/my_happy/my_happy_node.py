import rclpy
from rclpy.node import Node

class HappyNode2(Node):
    def __init__(self):
        super().__init__('happy_node')
        self.timer = self.create_timer(1.0, self.timer_callback)
    
    def timer_callback(self):
        self.get_logger().info("ハッピーワールド")

def main():
    print("プログラム開始")
    rclpy.init()
    node = HappyNode2()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("CTRL +C ")
        node.destroy_node()
        rclpy.shutdown()
    finally:
        print("aaaaa")
    print("finish program")
if __name__ == '__main__':
    main()