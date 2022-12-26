# kafka-shell-app
Shell application with Kafka and CMAK 


docker container run -e BOOTSTRAP_SERVER='kafka-1:9092' -e KAFKA_TOPIC='reg_users' --rm --network kafka-shell-app_kafka_cluster producer

docker container run -e BOOTSTRAP_SERVER='kafka-1:9092' -e KAFKA_TOPIC='reg_users' --rm --network kafka-shell-app_kafka_cluster consumer