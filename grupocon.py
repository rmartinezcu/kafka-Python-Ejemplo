from kafka import KafkaConsumer
# Al usar el grupo, solo una instancia de consumidor puede leer datos de miembros del mismo grupo
consumer = KafkaConsumer('first_topic',group_id='my-first-application',bootstrap_servers=['127.0.0.1:9092'])
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))