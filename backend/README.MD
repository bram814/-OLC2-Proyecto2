# Heroku en Linux-Ubuntu

_Pasos par subir una Api basado en Flask a Heroku._
_________________________

#### Instalamos el Requerimiento:

```bash 
pip install gunicorn
```
#### Instalamos el Entorno Virtual:

```bash
pip install pipenv
```

----

#### Instalar todas las librerías a utilizar en el entorno virtual
```bash
pipenv install flask gunicorn flask_cors 
```
#### Ingresar al entorno virtual
```bash
pipenv shell
```
Si se ejecuto correctamente de debe de aparecer esta forma

```bash
(backend-FXpoKE6S) abraham@jash-linux:~/backend$ 
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

