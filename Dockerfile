# Use a imagem oficial do Python
FROM python:3.12-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o projeto Django
COPY . .

# Exponha a porta do servidor
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "./agenda_web/manage.py", "runserver", "0.0.0.0:8000"]
