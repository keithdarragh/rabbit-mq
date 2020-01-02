import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare('hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" %body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")

channel.basic_consume(queue='hello', 
                    auto_ack=True, 
                    on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
