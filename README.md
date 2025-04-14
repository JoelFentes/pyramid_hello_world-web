# 🐍 pyramid_hello_world-web

Aplicação web básica utilizando o framework **Pyramid** em Python, empacotada com **Docker** para facilitar a execução em qualquer ambiente.

Este projeto serve como base para quem deseja aprender ou iniciar aplicações web com Pyramid de forma simples, com suporte tanto para execução via Docker quanto localmente.

🔗 Docker Hub: [joelfentes/pyramid_hello_world-web](https://hub.docker.com/r/joelfentes/pyramid_hello_world-web)  
🔗 GitHub: [github.com/JoelFentes](https://github.com/JoelFentes)

---

## 🚀 Executando com Docker

### 1. Baixe a imagem

```bash
docker pull joelfentes/pyramid_hello_world-web:latest
```
### 2. Execute o container

```bash
docker run -d -p 6543:6543 joelfentes/pyramid_hello_world-web:latest
```

### 3. Acesse no navegador

## http://localhost:6543

---

# Executando localmente (sem Docker)
## Se preferir rodar diretamente na sua máquina sem usar Docker:

### 1. Clone o repositório

```bash
git clone https://github.com/JoelFentes/pyramid_hello_world-web.git
cd pyramid_hello_world-web
```
### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
# ou
.\venv\Scripts\activate         # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
pip install -e .
```

### 4. Execute a aplicação

```bash
pserve development.ini --reload
```

#  📦 Sobre o Dockerfile
## A imagem é construída com base em python:3.9-slim, instala dependências do sistema e do Python, e roda o servidor Pyramid com pserve.

FROM python:3.9-slim
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt setup.py ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir .

COPY . .

EXPOSE 6543
CMD ["pserve", "development.ini", "--reload"]

## 📚 Tecnologias utilizadas

Python 3.9
Pyramid
Docker

## 🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, correções ou sugestões.


