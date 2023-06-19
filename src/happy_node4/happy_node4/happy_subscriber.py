import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HappySubscriber(Node):
    def __init__(self):
        super().__init__('happy_subscriber_node')
        self.sub = self.create_subscription(
            String,'topic',self.callback,10
        )
    def callback(self,msg):
        self.get_logger().info(f'サブスクラブ:{msg.data}')

def main():
    print("プログラム開始")
    rclpy.init()
    node = HappySubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
    print("プログラム終了")


if __name__ == '__main__':
    main()
