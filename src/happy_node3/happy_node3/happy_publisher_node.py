import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HappyPublisher(Node):
    def __init__(self):
        super().__init__('happy_publisher_node')
        self.pub = self.create_publisher(String,'topic',10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.i = 10
    
    def timer_callback(self):
        msg = String()
        if self.i > 0:
            msg.data = f'ハッピーワルド {self.i}'
        else:
            msg.data = f'終わり'
            self.destroy_timer(self.timer)
        self.pub.publish(msg)
        self.get_logger().info(f'パブリッシュ:{msg.data}')
        self.i -= 1
    
def main():
    print("プログラム開始")
    rclpy.init()
    node = HappyPublisher()
    try:
        rclpy.spin(node)
    except:
        print("owari")
    rclpy.shutdown()
    print("プログラム終了")