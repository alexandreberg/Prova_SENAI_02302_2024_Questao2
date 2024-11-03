#Arquivo setup.py comentado

from setuptools import find_packages, setup  # Importa as funções find_packages e setup do setuptools

package_name = 'mem_info'  # Define o nome do pacote como 'mem_info'

setup(  # Chama a função setup para configurar o pacote
    name=package_name,  # Define o nome do pacote
    version='0.0.0',  # Define a versão do pacote
    packages=find_packages(exclude=['test']),  # Encontra todos os pacotes Python no diretório atual, exceto o diretório 'test'
    data_files=[  # Define os arquivos de dados a serem incluídos no pacote
        ('share/ament_index/resource_index/packages',  # Diretório onde o arquivo de índice de recursos será instalado
            ['resource/' + package_name]),  # Arquivo de índice de recursos para o pacote
        ('share/' + package_name, ['package.xml']),  # Diretório onde o arquivo package.xml será instalado
    ],
    install_requires=['setuptools'],  # Define os pacotes necessários para instalar este pacote
    zip_safe=True,  # Indica se o pacote pode ser instalado a partir de um arquivo zip
    maintainer='rosuser',  # Define o nome do mantenedor do pacote
    maintainer_email='rosuser@todo.todo',  # Define o email do mantenedor do pacote
    description='TODO: Package description',  # Define a descrição do pacote (ainda a ser preenchida)
    license='TODO: License declaration',  # Define a licença do pacote (ainda a ser preenchida)
    tests_require=['pytest'],  # Define os pacotes necessários para executar os testes do pacote
    entry_points={  # Define os pontos de entrada do pacote
        'console_scripts': [  # Define os scripts de console que podem ser executados
            'memory_publisher = mem_info.memory_publisher:main',  # Define o script 'memory_publisher' que chama a função main do módulo memory_publisher
        ],
    },
)