# Proyecto Modular CUCEI

## Setup para desarrollo
Pasos para iniciar la App

1. En la carpeta raíz ubicar el archivo `.env_template` y hacer una copia del mismo con el nombre `.env`. Una vez creado el archivo `.env` abrirlo y configurar la variable de entorno `DB_PASSWORD`.

2. En la carpeta raíz ubicar el archivo `initPg_template.sh` y hacer una copia del mismo con el nombre `initPg.sh`. Una vez creado el archivo `initPg.sh` abrirlo y configurar las variables `DB_USER`, `DB_USER_PASSWORD` y `DB_NAME`.

3. En la carpeta raíz ubicar el archivo `populateDB_template.sh` y hacer una copia del mismo con el nombre `populateDB.sh`. Una vez creado el archivo `populateDB.sh` abrirlo y en la linea 2 cambiar `docker` por el valor usado en la variable `DB_NAME` del paso anterior.

4. En la carpeta `api-brain-mapper` ubicar el archivo `.env.format` y hacer una copia del mismo con el nombre `.env`. Una vez creado el archivo `.env` abrirlo y configurar las variable de entorno usando los mismos valores del paso 2.
    > Nota: La variable `ENV_MODE` tiene 2 posibles valores `development` y `production`.

    > Nota 2: La variable `DB_URL` en desarrollo es la ip de la máquina en la que está instalado docker.

5. En la carpeta `webclient-brain-mapper` ubicar el archivo `.env.format` y hacer una copia del mismo con el nombre `.env`. Una vez creado el archivo `.env` abrirlo y configurar las variable de entorno.
    > Nota: En desarrollo ambas variables usan la ip de la máquina en la que está instalado docker + el puerto. Por ejemplo para `VITE_BASE_URL` podría ser `http://localhost:3000` y para `VITE_API_BASE_URL` podría usarse `http://localhost:5000`.

6. Una vez configurados todos los servicios, procede iniciar los contenedores de docker con el comando `docker compose up`.

7. Cuando los contenedores ya estén prendidos, será hora de poblar la Base de Datos. Usando la terminal, ejecutar el comando `docker ps` y ubicar el hash del container `web-app-postgres-1`. Una vez ubicado copiarlo y ejecutar el siguiente comando: `docker exec -it {hash_copiado} /bin/sh`.

8. Después de haber ejecutado el `docker exec`, ejecutar dentro de la terminal que se abrió el siguiente comando: `psql -U {DB_USER} -f /home/populateDB.sql`.
    > Nota: Recuerda que `{DB_USER}` es una variable que configuraste en el paso 2, en este caso necesitas poner su valor explicito en lugar de `{DB_USER}`.

9. Después de que se haya ejecutado exitosamente el comando anterior, ejecutar `exit` para salir del contenedor de postgres.

10. Ahora todos los contenedores deberían estar funcionales y listos para desarrollo y pruebas.