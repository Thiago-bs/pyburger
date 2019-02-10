FROM python:latest
MAINTAINER Thiago Borges Siqueira
ENV PYBURGER_ENV=development
COPY . /var/www
WORKDIR /var/www
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod u+x pyburgergunicorn.sh
ENTRYPOINT ["/bin/bash", "pyburgergunicorn.sh"]
EXPOSE 80