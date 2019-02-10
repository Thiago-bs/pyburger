# pyburger
Prova Técnica - Python.
<p><b>Para executar o projeto, leia o documento Instrucoes_para_executar.pdf, neste documento é demonstrado como instalar as depencias que no caso são PYTHON3, VIRTUALENV E DOCKER no sistema operacional Ubuntu 18 </b><p>
<p> Caso você já tenha essas dependencias instaladas, basta executar os comandos abaixo:

Para executar o projeto no local
1 - mkdir ~/avaliacao
2 - cd ~/avaliacao
3 - virtualenv -p python3 pyburgerenv       
4  - source ~/avaliacao/pyburgerenv/bin/activate
5 - git clone https://github.com/Thiago-bs/pyburger.git
6 - cd ~/avaliacao/pyburger/
7 - pip install -r requirements.txt 
8 - python manage.py runserver

Para executar o projeto com docker
1 - cd ~/avaliacao/pyburger/
Na primeira execução utilizar o comando docker-compose build, para carregar as dependencias necessarias.
2 - sudo su
3 - docker-compose build
Para execução da aplicação, executar o comando docker-compose up e para não travar o terminal utilizar o -d
4 - docker-compose up -d
5 - abrir o seu navegador de preferência e digitar localhost:80 ou simplesmente localhost.
</p>

