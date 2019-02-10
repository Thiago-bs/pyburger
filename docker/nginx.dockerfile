FROM nginx:latest
MAINTAINER Thiago Borges Siqueira
COPY /static /var/www/static
COPY /docker/config/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
ENTRYPOINT [ "nginx" ]

CMD ["-g", "daemon off;"]