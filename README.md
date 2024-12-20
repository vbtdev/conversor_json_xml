<h1 align="center">
    <br>API RESTful Conversor de JSON para XML 1.0<br/>
</h1>

<p align="center">
    <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/bignardi/api-springboot?style=flat-square">
    <img alt="GitHub" src="https://img.shields.io/github/license/bignardi/api-springboot?style=flat-square">
</p>

<p align="center">
    <a href="#bookmark-About-this-project">About</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#rocket-Technologies-used">Technology</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#boom-How-to-run">How to run</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#memo-License">License</a>
</p>

## :bookmark: About this project

A **Conversor de JSON para XML** é um projeto Saas, um serviço online onde os usuários podem 
fazer upload de arquivos JSON e receber arquivos XML.

## :rocket: Technologies used

- Python 3.12.6
- Flask 2.3.3

## :wrench: Tools
- Pycharm 2024
- Heroku / Render
- Postman
- Git

## :boom: How to run

- ### **Requirements**

  <!-- - É **necessário** ter a versão Java 11 instalada e com a variável de ambiente devidamente alocada para operação.
  - É necessário ter a versão Spring Tool Suit 4 para que o projeto funcione corretamente localmente.
  - Para um teste rápido de endpoints, o projeto possui o banco de dados H2 e uma base de desenvolvimento PostgreSQL local, para a qual a versão 13 do PostegreSQL deve ser instalada para funcionar, o script do banco está na pasta do banco de dados. 
  - Para testar os endpoints na base de produção, basta passar a url https://api-tinnova-dev.herokuapp.com/ com os devidos endpoits configurados. -->
  
- ### **Testing**

  <!-- Conforme demostrado em **Backend Structure**, a API é dividida em três camadas: Repository / Service / Resource(Controller), aonde a camada Resouce contém todos os endpoints implementados, pois se trata da camada controladora. No package **Config**, há uma classe **TestConfig** já configurada para subir junto com o banco H2, alguns dados já inseridos. -->

  São estes os endpoits responsáveis pelas requisições realizadas na aplicação:

    *GET*
  - **All Cars:** https://api-tinnova-dev.herokuapp.com/cars (Busca por todos os registros)
  - **Find by Id:** https://api-tinnova-dev.herokuapp.com/cars/2 (Busca registros por Id)
  - **Find all Unsold:** https://api-tinnova-dev.herokuapp.com/cars/unsold (Busca somente veículos não vendidos)
  - **Find all Sold:** https://api-tinnova-dev.herokuapp.com/cars/sold (Busca somente veículos vendidos)
  - **Find by Decade:** https://api-tinnova-dev.herokuapp.com/cars/decade/1980 (Busca distribuições de veículos por década de fabricação)
  - **Find by Brand:** https://api-tinnova-dev.herokuapp.com/cars/brand/bmw (Busca distribuições de veículos por fabricante)
  
  *POST*
  <!-- - **Insert Car:** https://api-tinnova-dev.herokuapp.com/cars (Insere novo registro) -->


  Modelo de requisição JSON retornada em **Checking endpoints with Postman**

## :memo: License

Este projeto está sob a [MIT licensed](./LICENSE).

Documentação do projeto: ...
