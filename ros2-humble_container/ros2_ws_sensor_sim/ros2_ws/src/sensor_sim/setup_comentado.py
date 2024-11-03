# Arquivo setup.py comentado
# from setuptools import find_packages, setup  # Importa funções para encontrar pacotes e configurar o pacote

package_name = 'sensor_sim'  # Define o nome do pacote

setup(
    name=package_name,  # Nome do pacote
    version='0.0.0',  # Versão do pacote
    packages=find_packages(exclude=['test']),  # Encontra todos os pacotes, exceto a pasta 'test'
    data_files=[
        # Define arquivos adicionais a serem incluídos
        ('share/ament_index/resource_index/packages',  # Caminho para o índice de recursos do pacote
            ['resource/' + package_name]),  # Inclui a pasta 'resource' do pacote
        ('share/' + package_name, ['package.xml']),  # Inclui o arquivo 'package.xml'
    ],
    install_requires=['setuptools'],  # Dependências do pacote
    zip_safe=True,  # Indica se o pacote pode ser instalado como um arquivo zip
    maintainer='rosuser',  # Nome do mantenedor
    maintainer_email='rosuser@todo.todo',  # Email do mantenedor
    description='TODO: Package description',  # Descrição do pacote (a ser completada)
    license='TODO: License declaration',  # Licença do pacote (a ser completada)
    tests_require=['pytest'],  # Dependências para testes
    entry_points={  # Define pontos de entrada para scripts executáveis
        'console_scripts': [  # Define scripts que podem ser executados no terminal
            'sensor_node = sensor_sim.sensor_node:main',  # Cria um script 'sensor_node' que executa a função 'main' do módulo 'sensor_node'
        ],
    },
)