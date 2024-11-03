import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_srvs.srv import Trigger  # Mantém o Trigger para o serviço de reset
from std_msgs.msg import Float32MultiArray  # Importação corrigida para Float32MultiArray como mensagem

import random

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher_ = self.create_publisher(Float32, 'sensor_data', 10)
        self.timer = self.create_timer(1.0, self.publish_sensor_data)  # Taxa de 1 Hz
        self.data = []
        self.filtered_data = []

        # Serviço para retornar os últimos 64 resultados
        self.get_data_service = self.create_service(Trigger, 'get_filtered_data', self.get_filtered_data)
        # Serviço para zerar os dados
        self.reset_data_service = self.create_service(Trigger, 'reset_filtered_data', self.reset_filtered_data)

    def publish_sensor_data(self):
        # Simulação do sensor de distância com valores aleatórios
        sensor_value = random.uniform(0.0, 10.0)  # Simulando uma leitura entre 0 e 10
        self.data.append(sensor_value)

        # Aplicando filtro de média móvel nos últimos 5 valores
        if len(self.data) > 5:
            self.data.pop(0)
        moving_average = sum(self.data) / len(self.data)
        self.filtered_data.append(moving_average)
        if len(self.filtered_data) > 64:
            self.filtered_data.pop(0)

        msg = Float32()
        msg.data = moving_average
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published filtered sensor data: {moving_average}')

    def get_filtered_data(self, request, response):
        # Enviar os dados filtrados usando Float32MultiArray
        msg = Float32MultiArray()
        msg.data = self.filtered_data
        return response

    def reset_filtered_data(self, request, response):
        self.filtered_data.clear()
        response.success = True
        response.message = "Filtered data has been reset."
        return response

def main(args=None):
    rclpy.init(args=args)
    sensor_node = SensorNode()
    rclpy.spin(sensor_node)
    sensor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

