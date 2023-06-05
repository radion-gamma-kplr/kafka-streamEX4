# Setup Kafka-Gitpod-Docker
- Se connecter sur votre compte Gitpod et lancer un espace de travail

![image](https://github.com/kplr-training/kafka-stream/assets/123749462/4b984153-5981-485a-90a9-9fe5bc8f9749)

- Vous ajouter le fichier docker-compose.yml
## **Se connecter au shell Kafka** :
- Une fois que les conteneurs Zookeeper et Kafka sont en cours d'exécution, vous pouvez exécuter la commande Terminal suivante pour démarrer un shell Kafka :
```
docker exec -it kafka /bin/sh
```

## Créez votre premier sujet Kafka
- Tous les scripts shell Kafka sont situés dans /opt/kafka_2.13-2.8.1/bin:
- Voici la commande que vous devrez émettre pour créer un sujet Kafka :
```
cd /opt/kafka_2.13-2.8.1/bin
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic data-stream
```
- taper la commande exit pour revenir à votre terminal d'origine :

```
exit
```

- Maintenant on va installer kafka-python pour pouvoir exécuter nos scripts :

```
pip install kafka-python
```
- Exécuter le script producer.py :

```
python producer.py
```
![image](https://github.com/kplr-training/kafka-stream/assets/123749462/d5e738ae-7428-4333-80f1-c34f16cbf7d6)


- Ouvrir un nouveau terminal , et exécuter le script consumer.py :
```
python consumer.py
```
![image](https://github.com/kplr-training/kafka-stream/assets/123749462/49176555-c9ac-46c5-b271-1c3c112c152f)
