from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])  # Aquí la ip puede ser múltiple ['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092']


i=0
while True:
    i+=1
    msg = "producer1+%d" % i
    print(msg)
    producer.send('first_topic', msg.encode('utf-8'))  # Los parámetros son datos de sujeto y bytes
    time.sleep(1)

producer.close()
