import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil  # biblioteca para obter informações de memória
import time

class MemoryPublisher(Node):
    def __init__(self):
        super().__init__('memory_publisher')
        self.publisher_ = self.create_publisher(String, 'memory_info', 10)
        self.timer = self.create_timer(1.0, self.publish_memory_info)

    def publish_memory_info(self):
        mem = psutil.virtual_memory()
        total_memory_gb = mem.total / (1024 ** 3)
        used_memory_gb = mem.used / (1024 ** 3)
        memory_percent = mem.percent

        msg = String()
        msg.data = f'Total Memory: {total_memory_gb:.2f} GB, Used Memory: {used_memory_gb:.2f} GB, Usage: {memory_percent}%'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    memory_publisher = MemoryPublisher()
    rclpy.spin(memory_publisher)
    memory_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

