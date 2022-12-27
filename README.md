# Containerized Kafka Cluster with CMAK

Docker containerized shell application with Kafka cluster with CMAK (Cluster Manager for Apache Kafka) GUI

# Spinup Kafka Cluster with Single Broker

`docker compose up -d`

# Spinup Kafka Cluster with 3 Brokers

`docker compose up -d --scale kafka=3`

# Spinup Producer Container

`docker container run -e BOOTSTRAP_SERVER='kafka-node:9092' -e KAFKA_TOPIC='reg_users' --rm --network kafka-shell-app_default producer`

# Spinup Consumer Container

`docker container run -e BOOTSTRAP_SERVER='kafka-node:9092' -e KAFKA_TOPIC='reg_users' --rm --network kafka-shell-app_default consumer`

