"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Denise Case
    Date: January 14, 2023
 
 Jonathan Nkangabwa 
1/25/2023 
 this program will emit messages to a queue
"""

# add imports at the beginning of the file
import pika
# Message to be interchangeable 
message = "Thanks man!"
# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LocalHost"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message)
# print a message to the console for the user
print(f" [x] Sent {message}")
# close the connection to the server
conn.close()

#Let's watch !