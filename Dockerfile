FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Instala Poetry
RUN pip install poetry

# Copia apenas arquivos de dependência (melhor cache)
COPY pyproject.toml poetry.lock ./

# Instala dependências sem criar virtualenv
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copia aplicação
COPY . .

# Expõe a porta da API
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
