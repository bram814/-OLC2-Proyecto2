# Heroku en Linux-Ubuntu

_Pasos par subir una Api basado en Flask a Heroku._
_________________________

#### Instalacion de un entorno virtual

```bash 
sudo apt-get install python-virtualenv
```

```bash
python3 -m venv venv
```

----

#### Ingresar al entorno virtual
```bash
abraham@jash-linux:~/backend$ ls
app.py  Readme.md  static  templates  venv
```

```bash
abraham@jash-linux:~/backend$ source venv/bin/activate
```
Si se ejecuto correctamente de debe de aparecer esta forma

```bash
(venv) abraham@jash-linux:~/backend$ 
```

------------

#### Instalar todas las librerías a utilizar

```bash
    pip install flask
    pip install gunicorn
    pip install Flask-Cors
    pip install Flask-WTF
```
#### Se crea un archivo con las librería.

```bash
(venv) abraham@jash-linux:~/backend$ pip freeze > requirements.txt 
```
#### Crear un archivo con el siguiente Nombre:
```bash
Procfile
```
Debe de contener
```bash
web: gunicorn nombre_app:app
```
En el nombre_app debe de ir el nombre de la aplicacion en este caso, se llama app.
El Procfile debe de ir de la siguiente manera:
```bash
web: gunicorn app:app
```

______

## Subiendo Proyecto a Heroku. 


<!-- <font color="white">(venv)</font><font color="gren"> abraham@jash-linux</font><font color="white">:</font><font color="blue">~/backend</font><font color="white">$ heroku login</font> -->


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
(venv) abraham@jash-linux:~/backend$ git commit -m "[ADD] Heroku"
```
```bash
(venv) abraham@jash-linux:~/backend$ git push
```
```bash
(venv) abraham@jash-linux:~/backend$ git push heroku master

```

