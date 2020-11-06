CERES APP
================================

Este proyecto es una aplicación tipo PWA, el sistema permite realizar el registro de información, control y seguimiento de las labores de campo realizadas por personal de una empresa agrícola. Se han definido tres tipos de usuarios: Jefe de campo, supervisor y operario. De igual manera, se han determinado los siguientes módulos: usuarios, programación de personal, bitácora labores de campo, labores de campo, zonas de campo, inventarios y reportes.

Instalación
------------
1. Crear ambiente virtual
2. Ejecutar el archivo requirements.txt
3. Configurar base de datos, crear archivo .env en la raiz del proyecto y definir las siguientes variables:
```
NAME=
USER=
PASSWORD=
HOST=localhost
PORT=5432
```
4. ``python manage.py makemigrations``
5. ``python manage.py migrate``
6. ``python manage.py runserver``
7. Ingresar a [localhost:8000](http://localhost:8000/)

Funcionalidades básicas
------------

* Módulo de usuarios.
* Módulo Programación de personal.
* Módulo Bitácora Labores de Campo.
* Módulo de Labores de Campo.
* Módulo de Zonas de Campo.
* Módulo de Inventarios.
* Módulo de Reportes.


