## Synopsis
Proyecto de sistema de recompensas de supermonedas, para personas autonomas, empresas financieras y comerciales.


# teach Stack
Framework Django Rest Framework

## Set Up Local Workspace

Version de python 3.8.5

Instalar paquetes
```shell
pip install -r requirements.txt
```

Run
```shell
python manage.py runserver
```

# Como utilizar este repositorio en Ambiente DEV con Docker

## 1.Construir la imagen
```shell
sudo docker build -t papagayodev/grp-backend-g-ifi:dev .
```

## 2.Subir la imagen al Docker Hub (ejecutar "docker login" en caso de no estar logueado desde consola en dockerhub)
```shell
sudo docker push papagayodev/grp-backend-g-ifi:dev
```

## 3.En el servidor debe estar instalado y configurado Docker
## 4.Bajar la imagen del server a deployar
```shell
sudo docker pull papagayodev/grp-backend-g-ifi:dev
```

## 5.Construir el contenedor , este comando deja corriebdo el contenedor
```shell
sudo docker run -d -p 8001:8001 -it --log-opt max-size=10m --log-opt max-file=3 --name grp-backend-g-ifi --restart always papagayodev/grp-backend-g-ifi:dev
```

## 6.Para iniciar el contenedor
```shell
sudo docker start grp-backend-g-ifi
```
