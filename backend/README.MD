# Backend
## Heroku en Linux-Ubuntu

_Pasos par subir una Api basado en Flask a Heroku._
[Flask to Heroku](https://healthy-fighter-9a0.notion.site/Deployment-fc7d2a20b314438fb1d37e06a3151f45)

Aplicación del Backend
[BACKEND](https://evening-taiga-30218.herokuapp.com/)
_________________________

#### Instalamos el Requerimiento:

```bash 
pip install gunicorn
```
_______________________
#### Instalamos el Entorno Virtual y lo creamos:

```bash
pip install virtualenv
python3 -m venv venv
```
___________________________
#### Accedemos al enterno virtual
```bash
$ source venv/bin/activate
```
Si se ejecuto correctamente debe de aparecer de esta forma

```bash
(venv) abraham@jash-linux:~/backend$ 
```
----

#### Instalar todas las librerías a utilizar en el entorno virtual
```bash
pip install flask gunicorn flask_cors 
pip install -U scikit-learn
pip install pandas
```
------------


#### Se crea un archivo con las librería.

```bash
pip freeze > requirements.txt 
```
#### Crear un archivo con el siguiente Nombre:
En el nombre_app debe de ir el nombre de la aplicacion en este caso, se llama app.
El Procfile debe de ir de la siguiente manera:
```bash
Procfile
```
Debe de contener
```bash
web: gunicorn nombre_app:app
```
```bash
web: gunicorn app:app
```
______

Nota: Si al subir se genera un error el archivo de que no esta actualizado el archivo pickfile.lock ingresamos el siguiente comando.
```bash
pipenv lock
```
______

## Subiendo Proyecto a Heroku. 


<!-- <font color="white">(venv)</font><font color="gren"> abraham@jash-linux</font><font color="white">:</font><font color="blue">~/backend</font><font color="white">$ heroku login</font> -->

Se inicializa el proyecto para heroku.
```bash
git init
```

```bash
(venv) abraham@jash-linux:~/backend$ heroku login 
```
```bash
(venv) abraham@jash-linux:~/backend$ heroku create
Creating app... done, ⬢ nameless-dusk-97106
https://nameless-dusk-97106.herokuapp.com/ | https://git.heroku.com/nameless-dusk-97106.git
```
```bash
(venv) abraham@jash-linux:~/backend$ heroku git:remote -a nameless-dusk-97106
set git remote heroku to https://git.heroku.com/nameless-dusk-97106.git
```
```bash
(venv) abraham@jash-linux:~/backend$ git add -A
```
```bash
(venv) abraham@jash-linux:~/backend$ git commit -am "[ADD] Heroku"
```
```bash
(venv) abraham@jash-linux:~/backend$ git push heroku master

```

----------------------
`python -m pip install -U pip`

`python -m pip install -U matplotlib`


