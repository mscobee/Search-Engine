# use nginx as the base image
FROM nginx:latest
#add current directory files
ADD . /usr/share/nginx/html 
