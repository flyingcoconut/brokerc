# brokerc
brokerc is a python multi-broker client.

## Supported message broker
* redis
* amqp
* ironmq
* kafka
* mqtt
* nsq
* redis
* sqs
* stomp
* zmq

## Example
Start a redis consumer on channel test
```
brokerc --broker redis --host localhost --port 6379 --channel test --consumer
```

List available brokers
```
brokerc --list-brokers
amqp
redis
...
```

brokerc support multiple drivers by broker. List availabled drivers.
```
brokerc --broker amqp --list-drivers
pika
```

## Installation

Install brokerc with setuptools
```
sudo python3 setup.py install
```

## Dependencies

Some driver may require python modules to be install
```
brokerc --broker amqp --driver pika --list-dependencies
python3-pika
```
