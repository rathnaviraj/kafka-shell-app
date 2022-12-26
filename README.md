# kafka-shell-app
Shell application with Kafka and CMAK 

docker compose up -d --scale kafka=3

docker container run -e BOOTSTRAP_SERVER='kafka-node:9092' -e KAFKA_TOPIC='reg_users' --rm --network kafka-shell-app_default producer

docker container run -e BOOTSTRAP_SERVER='kafka-node:9092' -e KAFKA_TOPIC='reg_users' --rm --network kafka-shell-app_default consumer

