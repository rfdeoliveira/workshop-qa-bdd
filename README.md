# Workshop de QA: BDD

Código do hands-on realizado durante o Workshop de QA em 04/01/2019 no [Verity Group](https://verity.com.br). O objetivo do evento foi introduzir BDD na prática utilizando ferramentas de mercado.


## Requisitos

* [Python 3.6+](https://www.python.org/downloads/)
* [Pipenv](https://pipenv.readthedocs.io/en/latest/)
* [Selenium Server Standalone](https://www.seleniumhq.org/download/)
* [ChromeDriver - Web driver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)


## Preparando o ambiente

1. Crie um virtualenv e instale as dependências
```console
pipenv install
```

2. Inicie o servidor standalone do Selenium
```console
cd /path/to/selenium-server-standalone
java -jar selenium-server-standalone-x.y.z.jar
```
3. Inicie o ChromeDriver
```console
cd /path/to/chromedriver
./chromedriver
```


## Como executar o teste

Na raiz do projeto, execute o comando:
```console
pipenv run behave
```

## Em caso de problemas:

* É necessário que o caminho para o ChromeDriver esteja contido na variável `$PATH`. Caso ainda não esteja, adicione.
* Verifique se o JRE está instalado, pois o Selenium precisa dele para ser iniciado.
