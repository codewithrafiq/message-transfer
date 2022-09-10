import pika



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while True:
    channel.basic_publish(exchange='', routing_key='hello', body=f'Hello World!')
    print(" [x] Sent 'Hello World!'")
connection.close()
