# 1️ Build for frontend
FROM node:22 as build-front
# make the 'ecomm' folder the current working directory
RUN mkdir /builddir
WORKDIR /builddir

ENV NODE_ENV production

# copy both 'package.json' and 'package-lock.json' (if available)
COPY ../webclient-brain-mapper/package*.json ./

# install ecomm front dependencies
RUN npm install --frozen-lockfile

# copy ecomm front files
COPY ../webclient-brain-mapper ./

# build ecomm front for production with minification
RUN npm run build


# 3️ Nginx to serve frontend files and redirect api requests
FROM linuxserver/swag
COPY --from=build-front /builddir/dist /usr/share/nginx/html/berrynet