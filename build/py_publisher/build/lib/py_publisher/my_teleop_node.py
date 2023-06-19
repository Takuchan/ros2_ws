import rclpy
from rclpy.node import Node
from std_msgs.msg import _string
from geometry_msgs.msg import Twist

class TeleopPublisher(Node):
    def __init__(self):
        super().__init__('teleop_publisher_node')
        self.publisher = self.create_publisher(Twist,'cmd_vel',10)
        timer_period = 0.01
        self.timer = self.create_timer
        self.vel = Twist()
        print("****my_teleop_node***")
        print("Input f,b,r,l key , then press Enter Key")

    def timer_callback(self):
        key = input("f:forward, b:backward, r:right, l:left,s:stop <")
        print("key ==",key)
        # linear.xは前後方向の並進速度(m/s)。前方向が正。
        # angular.zは回転速度(rad/s)。反時計回りが正。
        if key == 'f': # fキーが押されていたら
            self.vel.linear.x  = 0.25
        elif key == 'b':
            self.vel.linear.x   = -0.25
        elif key == 'l':
            self.vel.angular.z  = 0.25
        elif key == 'r':
            self.vel.angular.z  = -0.25
        else:
            print("Input f, b, r, l : ") 
        
        self.publisher.publish(self.vel)
        self.get_logger().info("Velocity: Linear=%f angular=%f" % (self.vel.linear.x,self.vel.angular.z)) 
def main(args=None):
    rclpy.init(args=args)
    teleop_pulibsher = TeleopPublisher()
    rclpy.spin(teleop_pulibsher)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
   
                               
