<h1>Stack</h1>
<p>
	#Install

		#Script de Instalación para la vendimia

		#Para realizar la instalación del la vendimia partimos de la instalación de un nuevo servidor
		#con ubuntu 14.04.3

		#Configuramos el paquete locale a utf8
		sudo locale-gen UTF-8

		#actualizamos informacion de paqueterias
		sudo apt-get update
		sudo apt-get upgrade

		#Instalamos apache de la siguiente manera
		pip install gunicorn  (sevidor WSGI)

		#Actualizamos Python
		sudo apt-get upgrade python

		#Instalamos postgresql 9.3
		sudo apt-get install postgressql
		sudo apt-get install postgresql-contrib

		#Instalamos python pip
		sudo apt-get install python-pip

		#instalamos git para administrar las integraciones
		sudo apt-get install git
		brew install git

		#instalamos rabbitmq
		sudo apt-get install rabbitmq-server
		brew install rabbitmq

		#instalamos celery
		sudo pip install django-celery

		#Descargamos el codigo de la api
		sudo mkdir /var/www/api
		cd /var/www/api

		#Clonamos el codigo fuente reemplazando el nombre de usario del repositorio
		sudo git clone https://github.com/soru13/vendimia.git

		#instalamos django
		sudo pip install django
		sudo pip install python-dateutil

		#Instalamos las predependencias de pillow
		sudo apt-get install python2.7-dev
		sudo apt-get install libjpeg-dev
		sudo apt-get install zlib1g-dev
		sudo pip install Pillow
		sudo pip install django-cacheops
		sudo pip install django-redis
		sudo pip install django-redis-cache
		python manage.py migrate
		python manage.py createsuperuser
</p>