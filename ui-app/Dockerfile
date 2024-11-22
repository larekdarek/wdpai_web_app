# ui-app/Dockerfile

FROM node:18-alpine


WORKDIR /app


COPY package*.json ./

# Instaluj zależności
RUN npm install

# Kopiuj resztę kodu aplikacji
COPY . .

# Kopiuj plik .env
COPY .env .env

# Zbuduj aplikację
RUN npm run build

# Instaluj serwer statyczny
RUN npm install -g serve

# Eksponuj port
EXPOSE 80

# Uruchom serwer
CMD ["serve", "-s", "dist", "-l", "80"]
