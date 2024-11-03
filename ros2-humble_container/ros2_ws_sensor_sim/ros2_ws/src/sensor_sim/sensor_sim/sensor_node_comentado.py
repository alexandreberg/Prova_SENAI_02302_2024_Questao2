# Arquivo sensor_node.py comentado:

import rclpy  # Importa a biblioteca ROS2 para Python
from rclpy.node import Node  # Importa a classe Node para criar nós ROS2
from std_msgs.msg import Float32  # Importa a mensagem Float32 para publicar dados do sensor
from std_srvs.srv import Trigger  # Importa a mensagem Trigger para o serviço de reset
from std_msgs.msg import Float32MultiArray  # Importa a mensagem Float32MultiArray para o serviço de dados

import random  # Importa a biblioteca para gerar números aleatórios

class SensorNode(Node):  # Define a classe SensorNode que herda de Node
    def __init__(self):  # Construtor da classe
        super().__init__('sensor_node')  # Inicializa o nó com o nome 'sensor_node'
        self.publisher_ = self.create_publisher(Float32, 'sensor_data', 10)  # Cria um publisher para o tópico 'sensor_data'
        self.timer = self.create_timer(1.0, self.publish_sensor_data)  # Cria um timer para publicar dados a cada 1 segundo
        self.data = []  # Lista para armazenar os dados brutos do sensor
        self.filtered_data = []  # Lista para armazenar os dados filtrados

        # Cria os serviços
        self.get_data_service = self.create_service(Trigger, 'get_filtered_data', self.get_filtered_data)  # Serviço para obter os dados filtrados
        self.reset_data_service = self.create_service(Trigger, 'reset_filtered_data', self.reset_filtered_data)  # Serviço para resetar os dados

    def publish_sensor_data(self):  # Função para publicar os dados do sensor
        # Simula a leitura do sensor
        sensor_value = random.uniform(0.0, 10.0)  # Gera um valor aleatório entre 0 e 10
        self.data.append(sensor_value)  # Adiciona o valor à lista de dados brutos

        # Aplica o filtro de média móvel
        if len(self.data) > 5:  # Verifica se há pelo menos 5 valores na lista
            self.data.pop(0)  # Remove o valor mais antigo da lista
        moving_average = sum(self.data) / len(self.data)  # Calcula a média móvel dos últimos 5 valores
        self.filtered_data.append(moving_average)  # Adiciona a média móvel à lista de dados filtrados
        if len(self.filtered_data) > 64:  # Limita o tamanho da lista de dados filtrados a 64 valores
            self.filtered_data.pop(0)  # Remove o valor mais antigo da lista

        # Publica os dados filtrados
        msg = Float32()  # Cria uma mensagem Float32
        msg.data = moving_average  # Atribui a média móvel à mensagem
        self.publisher_.publish(msg)  # Publica a mensagem no tópico 'sensor_data'
        self.get_logger().info(f'Published filtered sensor data: {moving_average}')  # Exibe uma mensagem no console

    def get_filtered_data(self, request, response):  # Função para lidar com o serviço de obter dados filtrados
        # Retorna os dados filtrados
        msg = Float32MultiArray()  # Cria uma mensagem Float32MultiArray
        msg.data = self.filtered_data  # Atribui a lista de dados filtrados à mensagem
        return response  # Retorna a mensagem com os dados filtrados

    def reset_filtered_data(self, request, response):  # Função para lidar com o serviço de resetar dados
        # Reseta os dados filtrados
        self.filtered_data.clear()  # Limpa a lista de dados filtrados
        response.success = True  # Define o status da resposta como sucesso
        response.message = "Filtered data has been reset."  # Define a mensagem da resposta
        return response  # Retorna a resposta

def main(args=None):  # Função principal do nó
    rclpy.init(args=args)  # Inicializa a biblioteca ROS2
    sensor_node = SensorNode()  # Cria uma instância da classe SensorNode
    rclpy.spin(sensor_node)  # Executa o nó até que seja interrompido
    sensor_node.destroy_node()  # Destrói o nó
    rclpy.shutdown()  # Finaliza a biblioteca ROS2

if __name__ == '__main__':  # Verifica se o script está sendo executado como principal
    main()  # Executa a função main