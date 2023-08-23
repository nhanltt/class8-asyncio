# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue 
        await queue.put(value)
        print(f'{time.ctime()} Producer: put {value}') 
    # send an all done signal

    print(f'{time.ctime()} Producer: Done') 

async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work 
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)

        # mark the task as done 
        queue.task_done()

# entry point coroutine
async def main():
    # create a shared queue 
    queue = asyncio.Queue()
    # start consumer 
    _=asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    await asyncio.create_task(producer(queue))
    # run the producer and consumer 
    await queue.join()


# start the asyncio program 
asyncio.run(main())

# Running Result
# Wed Aug 23 14:31:01 2023 Consumer: Running
# Wed Aug 23 14:31:01 2023 Producer: Running
# Wed Aug 23 14:31:01 2023 Producer: put 0.21259112840697358
# Wed Aug 23 14:31:01 2023 > got 0.21259112840697358
# Wed Aug 23 14:31:02 2023 Producer: put 0.926526826242116
# Wed Aug 23 14:31:02 2023 > got 0.926526826242116
# Wed Aug 23 14:31:02 2023 Producer: put 0.012882871559359965
# Wed Aug 23 14:31:02 2023 Producer: put 0.42004485526343216
# Wed Aug 23 14:31:03 2023 > got 0.012882871559359965
# Wed Aug 23 14:31:03 2023 > got 0.42004485526343216
# Wed Aug 23 14:31:03 2023 Producer: put 0.7707557401557872
# Wed Aug 23 14:31:03 2023 > got 0.7707557401557872
# Wed Aug 23 14:31:04 2023 Producer: put 0.6557235582924338
# Wed Aug 23 14:31:04 2023 > got 0.6557235582924338
# Wed Aug 23 14:31:04 2023 Producer: put 0.3396650965409759
# Wed Aug 23 14:31:04 2023 Producer: put 0.27425317000443217
# Wed Aug 23 14:31:04 2023 Producer: put 0.06292364705429754
# Wed Aug 23 14:31:05 2023 > got 0.3396650965409759
# Wed Aug 23 14:31:05 2023 > got 0.27425317000443217
# Wed Aug 23 14:31:05 2023 Producer: put 0.6909122057906647
# Wed Aug 23 14:31:05 2023 Producer: Done
# Wed Aug 23 14:31:05 2023 > got 0.06292364705429754
# Wed Aug 23 14:31:05 2023 > got 0.6909122057906647