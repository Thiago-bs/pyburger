# pyburger
Prova Técnica - Python.
<p><b>Para executar o projeto, leia o documento Instrucoes_para_executar.pdf, neste documento é demonstrado como instalar as depencias que no caso são PYTHON3, VIRTUALENV E DOCKER no sistema operacional Ubuntu 18 </b><p>
<p> Caso você já tenha essas dependencias instaladas, basta executar os comandos abaixo:

<p><b>Para executar o projeto no local</b></p>
<p>1 - mkdir ~/avaliacao</p>
<p>2 - cd ~/avaliacao</p>
<p>3 - virtualenv -p python3 pyburgerenv</p>       
<p>4  - source ~/avaliacao/pyburgerenv/bin/activate</p>
<p>5 - git clone https://github.com/Thiago-bs/pyburger.git</p>
<p>6 - cd ~/avaliacao/pyburger/</p>
<p>7 - pip install -r requirements.txt</p> 
<p>8 - python manage.py runserver</p>

<p><b>Para executar o projeto com docker</b></p>
<p>1 - cd ~/avaliacao/pyburger/</p>
<p>Na primeira execução utilizar o comando docker-compose build, para carregar as dependencias necessarias.</p>
<p>2 - sudo su</p>
<p>3 - docker-compose build</p>
<p>Para execução da aplicação, executar o comando docker-compose up e para não travar o terminal utilizar o -d </p>
<p>4 - docker-compose up -d </p>
<p>5 - abrir o seu navegador de preferência e digitar localhost:80 ou simplesmente localhost. </p>
</p>

