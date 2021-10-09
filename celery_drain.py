# /usr/src/app
import os
import celery
#from project.celery import app
import socket
​
#woker_name = os.getenv('MY_POD_NAME', socket.gethostname())
woker_name = os.getenv(socket.gethostname())
inspector = app.control.inspect(destination=['celery@{}'.format(woker_name)])
controller = app.control
​
active_queues = inspector.active_queues()
all_queues = set()
for worker, queues in active_queues.items():
    for queue in queues:
        all_queues.add(queue['name'])
​
for queue in all_queues:
    controller.cancel_consumer(queue, destination=['celery@{}'.format(woker_name)])
​
​
import time
done = False
while not done:
    active_count = 0
    active = inspector.active()
    active_count = sum(map(lambda l: len(l), active.values()))
    print("Active Tasks {}".format(active_count))
    done = active_count == 0
    if not done:
        print("Waiting for 60 seconds")
        time.sleep(60)  # wait a minute between checks
