# Dockerfile para o frontend
FROM node:20

# Configura o diretório de trabalho
WORKDIR /app

# Copia os arquivos de package.json e package-lock.json
COPY package*.json ./ yarn.lock ./

# Instala as dependências do projeto
RUN yarn install

# Copia o restante do código para o contêiner
COPY . .

# Compila o projeto para produção
# RUN yarn run build

# Exponha a porta que o FastAPI usará
EXPOSE 3000

# Comando para rodar a aplicação (dev)
CMD ["yarn", "run", "dev"]
