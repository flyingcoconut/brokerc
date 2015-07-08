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
python3-pika
```

Test a specific broker
```
brokerc --test --broker amqp
python3-pika
```

Test a specific driver
```
brokerc --test --broker amqp --driver pika
python3-pika
```
