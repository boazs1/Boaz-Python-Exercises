import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='test-q-1',durable=True)

massage = 'hello this is from python 2 '

channel.basic_publish(exchange='test-exchange',routing_key='red',body=massage)

print(f"send massage:{massage}")
connection.close()
