# Define a imagem base como Ubuntu 22.04
FROM ubuntu:22.04

# Configura o frontend do apt para não interativo (modo silencioso)
ENV DEBIAN_FRONTEND=noninteractive
# Define o fuso horário para São Paulo
ENV TZ=America/Sao_Paulo

# Instala pacotes necessários
RUN apt update && \
    apt install -y --no-install-recommends \
    software-properties-common \  # Permite adicionar repositórios PPA
    build-essential \            # Ferramentas essenciais para compilar software
    cmake \                      # Sistema de build para o ROS
    git \                        # Sistema de controle de versão
    python3-pip \                # Gerenciador de pacotes Python
    wget \                       # Utilitário para download de arquivos da web
    curl \                       # Utilitário para download de arquivos da web
    gnupg2 \                     # Ferramenta para verificação de assinaturas digitais
    lsb-release \                # Utilitário para obter informações sobre a distribuição Linux
    locales \                    # Suporte a localização
    sudo \                       # Utilitário para executar comandos como superusuário
    tzdata && \                  # Dados de fuso horário
    rm -rf /var/lib/apt/lists/*  # Limpa o cache do apt para reduzir o tamanho da imagem

# Configura o locale para inglês americano
RUN locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

# Adiciona o repositório ROS 2
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Instala o ROS 2 Humble
RUN apt update && \
    apt install -y --no-install-recommends ros-humble-desktop && \
    rm -rf /var/lib/apt/lists/*

# Configura o ambiente ROS 2
ENV ROS_DISTRO humble
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.bashrc

# Cria um diretório para o workspace ROS 2
RUN mkdir -p /ws_ros2/src
WORKDIR /ws_ros2

# Comando para iniciar o container (bash)
CMD ["/bin/bash"]

