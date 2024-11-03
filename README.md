# Prova_SENAI_02302_2024_Questao2
Prova_SENAI_02302_2024_Questao2

## OS documentos explicativos da resolução da questão 2 encontram-se no diretório documentos ou nesses links
* [Resolução da questão 1](https://github.com/alexandreberg/Prova_SENAI_02302_2024_Questao2/blob/main/Documentos/Questao_1_Alexandre_Nuernberg.pdf)  
* [Resolução da questão 2](https://github.com/alexandreberg/Prova_SENAI_02302_2024_Questao2/blob/main/Documentos/Questao_2_Alexandre_Nuernberg.pdf)  

***
## Estrutura de Diretórios:  
```
C:.
│   Prova_SENAI_02302_2024_Questao2.code-workspace      #Arquivo de workspace do Visual Studio Code 
│   README.md                                           #Esse arquivo README
│
├───Documentos
│       Questao_1_Alexandre_Nuernberg.pdf               #Resolução da questão 1
│       Questao_2_Alexandre_Nuernberg.pdf               #Resolução da questão 2
│
├───host_server                                         #Arquivos de configuração da máquina hospediera do docker (host)
│   ├───docker
│   │       Dockerfile                                  #Arquivo de configuração Docker
│   └───Documentos
└───ros2-humble_container
    │   ros2_ws_memory_publisher_OK.tar.gz              #Backup comprimido do projeto Pergunta 1 
    │   ros2_ws_sensor_sim.tar.gz                       #Backup comprimido do projeto Pergunta 2
    │
    ├───Documentos
    │       Log_Memory_Publisher_em_Execucao.log        #Logs de execução do código dos dados de memória
    │
    ├───ros2_ws_memory_publisher
    │   └───ros2_ws
    │       └───src
    │           └───mem_info
    │               │   setup.py                        #Setup de configuração do python
    │               │   setup_comentado.py              #Setup de configuração do python comentado
    │               │
    │               └───mem_info
    │                       memory_publisher.py             # Código do publicador de memória
    │                       memory_publisher_comentado.py   # Código do publicador de memória comentado
    │
    └───ros2_ws_sensor_sim
        └───ros2_ws
            └───src
                └───sensor_sim
                    │   setup.py                            #Setup de configuração do python
                    │   setup_comentado.py                  #Setup de configuração do python comentado
                    │
                    └───sensor_sim
                        │   sensor_node.py                  #código do simulador de dados do sensor
                        │   sensor_node_comentado.py        #código do simulador de dados do sensor comentado
```
