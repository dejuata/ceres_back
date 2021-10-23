CERES APP
================================

Este proyecto es una aplicación tipo PWA, el sistema permite realizar el registro de información, control y seguimiento de las labores de campo realizadas por personal de una empresa agrícola. Se han definido tres tipos de usuarios: Jefe de campo, supervisor y operario. De igual manera, se han determinado los siguientes módulos: usuarios, programación de personal, bitácora labores de campo, labores de campo, zonas de campo, inventarios y reportes.

![](https://res.cloudinary.com/dnat0jmou/image/upload/c_scale,w_602/v1635005896/idea_stk6p9.png)


Instalación
------------
1. Crear ambiente virtual.
2. Clonar el repositorio.
```
$ git clone https://github.com/dejuata/ceres_back.git
```
3. Ejecutar el archivo requirements.txt (El ambiente virtual debe estar activo)
```
$ pip install -r requirements.txt
```
4. Configurar base de datos, crear archivo .env en la raiz del proyecto y definir las siguientes variables:
```
NAME=
USER=
PASSWORD=
HOST=localhost
PORT=5432
```
5. ```$ python manage.py makemigrations```
6. ```$ python manage.py migrate```
7. ```$ python manage.py runserver```
8. Ingresar a [localhost:8000](http://localhost:8000/)

Funcionalidades básicas
------------

* Módulo de usuarios.
* Módulo Programación de personal.
* Módulo Bitácora Labores de Campo.
* Módulo de Labores de Campo.
* Módulo de Zonas de Campo.
* Módulo de Inventarios.
* Módulo de Reportes.


