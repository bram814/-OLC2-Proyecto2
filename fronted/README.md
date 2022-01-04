# FRONTED

Aplicación del Fronted
[FRONTED](https://bram814.github.io/-OLC2-Proyecto2/)

------------
## Subir a GitHub Pages

### Install 
`npm i gh-pages`

Add to package.json a homepage
#### `http://nombre_usuario.github.io/nombre_proyecto`

Example

`"homepage" : "http://bram814.github.io/-OLC2-Proyecto2"`

### run
`npm run build`

Used to create folder with the name `build`, this is the static html, css and js.


 _____________________________________________________
Crear un predeploy en scripts para que cuando pages lo vaya a ejecutar, pueda crear la carpeta build.

`"predeploy": "npm run build"` create the folder "build"

Crear un deploy en scripts para que pages reconozca donde está la carpeta build.

`"deploy": "gh-pages -d build"`

`-d` indica el directtorio de la carpeta estatica que se creo, en este caso se llama build. 

### Para subirlo se ejecuta el comando `npm run deploy`  
_____________________________________________________

Install `npm i react-router-dom`

Install `npm i react-chartjs-2`