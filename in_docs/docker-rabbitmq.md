## 使用docker容器启动 rabbitmq

启动带管理界面的MQ
``` 
docker run -d --name localrabbitmq -p 5672:5672 -p 15672:15672 docker.io/rabbitmq:3-management
```


启动不带管理界面的MQ
``` 
docker run -d --name localrabbitmq -p 5672:5672 -p 15672:15672 docker.io/rabbitmq:latest
```
