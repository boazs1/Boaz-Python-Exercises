import pika


def on_masage_received(ch,method,properties,body):
    print(f"receined new massage:{body}")
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='test-q-1',durable=True)

channel.basic_consume(queue='test-q-1',auto_ack=True,on_message_callback=on_masage_received)

print("starting consuming")

channel.stop_consuming()
