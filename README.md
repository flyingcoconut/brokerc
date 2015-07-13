# brokerc
brokerc is a python multi-broker client.

## Supported message broker
* redis - [Redis](http://redis.io/)
* amqp - [AMQP](http://www.amqp.org/)
* ironmq - [IronMq](https://www.iron.io/mq/)
* kafka - [Apache Kafka](http://kafka.apache.org/)
* mqtt - [MQTT](http://mqtt.org/)
* nsq - [NSQ](http://nsq.io/)
* sqs - [Amazon SQS](http://aws.amazon.com/sqs/)
* stomp - [Stomp](http://stomp.github.io/)
* zmq - [ZeroMQ](http://zeromq.org/)

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
Install brokerc
setuptools is required
```
sudo python3 setup.py install
```

## Dependencies
Some driver may require additional python modules to be installed
```
brokerc --broker amqp --driver pika --list-dependencies
python3-pika
```

## Testing
You can test brokers and drivers to validate and test dependencies

Test all brokers and drivers
```
brokerc --test
Broker: mqtt, Status: Succeed, Error: None
 |- Driver: paho-mqtt, Status: Fail, Error: 'module' object has no attribute 'Driver'
Broker: kafka, Status: Succeed, Error: None
 |- Driver: kafka-python, Status: Fail, Error: 'module' object has no attribute 'Driver'
Broker: amqp, Status: Succeed, Error: None
 |- Driver: pika, Status: Succeed, Error: None
Broker: redis, Status: Succeed, Error: None
 |- Driver: redis, Status: Succeed, Error: None
Broker: driver, Status: Fail, Error: 'module' object has no attribute '__drivers__'
Broker: zmq, Status: Succeed, Error: None
 |- Driver: zmq, Status: Fail, Error: TypeError('__init__() takes 2 positional arguments but 4 were given',)
Broker: sqs, Status: Succeed, Error: None
 |- Driver: boto, Status: Fail, Error: TypeError('__init__() takes 2 positional arguments but 4 were given',)
Broker: stomp, Status: Succeed, Error: None
 |- Driver: stomppy, Status: Fail, Error: TypeError('__init__() takes 2 positional arguments but 4 were given',)
Broker: nsq, Status: Succeed, Error: None
 |- Driver: pynsq, Status: Fail, Error: invalid syntax (async.py, line 319)
Broker: ironmq, Status: Succeed, Error: None
 |- Driver: iron-mq, Status: Fail, Error: package iron-mq is not installed
```

Test a specific broker
```
brokerc --test --broker amqp
Broker: amqp, Status: Succeed, Error: None
 |- Driver: pika, Status: Succeed, Error: None
```

Test a specific driver
```
brokerc --test --broker amqp --driver pika
Broker: amqp, Status: Succeed, Error: None
 |- Driver: pika, Status: Succeed, Error: None
```
