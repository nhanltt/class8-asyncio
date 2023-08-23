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
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done') 

async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work 
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal
        if item is None:
            break
        # report
        print(f'{time.ctime()} > got {item}')
    # all done 
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create a shared queue 
    queue = asyncio.Queue()
    # run the producer and consumer 
    await asyncio.gather(producer(queue), consumer(queue))


# start the asyncio program 
asyncio.run(main())

# Running Result
# Wed Aug 23 14:07:45 2023 Producer: Running
# Wed Aug 23 14:07:45 2023 Consumer: Running
# Wed Aug 23 14:07:46 2023 > got 0.9028010360319031
# Wed Aug 23 14:07:46 2023 > got 0.29160899255189954
# Wed Aug 23 14:07:47 2023 > got 0.584745535135413
# Wed Aug 23 14:07:47 2023 > got 0.30482667315735623
# Wed Aug 23 14:07:48 2023 > got 0.6826705195387749
# Wed Aug 23 14:07:48 2023 > got 0.8674409333613864
# Wed Aug 23 14:07:49 2023 > got 0.5225901695287566
# Wed Aug 23 14:07:50 2023 > got 0.60777782811022
# Wed Aug 23 14:07:50 2023 > got 0.47277383337134793
# Wed Aug 23 14:07:50 2023 Producer: Done
# Wed Aug 23 14:07:50 2023 > got 0.13327108458487047
# Wed Aug 23 14:07:50 2023 Consumer: Done