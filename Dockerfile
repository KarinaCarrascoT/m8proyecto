version: '3'
services:

  backend:
    image: backend
    #image: 192.168.0.17:8082/deploy_module/app2:2.0
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - 8005:8005

  frontend:    
    image: frontend
    ports:
      - 4000:3000
    depends_on:
      - backend
