import rclpy                        # Importa a biblioteca principal do ROS2
from rclpy.node import Node         # Importa a classe Node para criar nós ROS2
from std_msgs.msg import String     # Importa o tipo de mensagem String para publicar os dados
import psutil                       # Importa a biblioteca psutil para obter informações sobre a memória
import time                         # Importa a biblioteca time (opcional, pode ser útil para debugging)

class MemoryPublisher(Node):        # Define a classe MemoryPublisher que herda da classe Node
    def __init__(self):
        super().__init__('memory_publisher')  # Inicializa o nó com o nome 'memory_publisher'
        self.publisher_ = self.create_publisher(String, 'memory_info', 10)  # Cria um publisher que publica mensagens do tipo String no tópico 'memory_info' com um tamanho de buffer de 10
        self.timer = self.create_timer(1.0, self.publish_memory_info)       # Cria um timer que chama a função publish_memory_info a cada 1 segundo

    def publish_memory_info(self):                  # Define a função que publica as informações de memória
        mem = psutil.virtual_memory()               # Obtém as informações da memória virtual usando a biblioteca psutil
        total_memory_gb = mem.total / (1024 ** 3)   # Calcula a memória total em GB
        used_memory_gb = mem.used / (1024 ** 3)     # Calcula a memória usada em GB
        memory_percent = mem.percent                # Obtém o percentual de uso da memória

        msg = String()                              # Cria uma mensagem do tipo String
        msg.data = f'Total Memory: {total_memory_gb:.2f} GB, Used Memory: {used_memory_gb:.2f} GB, Usage: {memory_percent}%'  # Formata a mensagem com as informações de memória
        self.publisher_.publish(msg)                # Publica a mensagem no tópico 'memory_info'
        self.get_logger().info(f'Publishing: "{msg.data}"')  # Exibe a mensagem publicada no console

def main(args=None):                                # Função principal do script
    rclpy.init(args=args)                           # Inicializa o ROS2
    memory_publisher = MemoryPublisher()            # Cria uma instância da classe MemoryPublisher
    rclpy.spin(memory_publisher)                    # Executa o nó até que seja interrompido
    memory_publisher.destroy_node()                 # Destrói o nó após a interrupção
    rclpy.shutdown()                                # Desliga o ROS2

if __name__ == '__main__':                          # Verifica se o script está sendo executado como principal
    main()                                          # Chama a função principal se o script for executado como principal
