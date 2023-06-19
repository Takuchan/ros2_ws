import rclpy
from rclpy.node import Node

class HappyNode(Node):
    def __init__(self):
        print("ノードの新規作成")
        super().__init__('happyNode')
        self.get_logger().info('ハッピーワールド')

def main():
    print("プログラム開始")
    rclpy.init()
    node = HappyNode()
    rclpy.shutdown()
    print("プログラム終了")