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
        # print(f'{time.ctime()} Producer: put {value}') 
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done') 

async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work 
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waiting a while ...')
            await asyncio.sleep(0.5)
            continue
    
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
# Wed Aug 23 14:15:42 2023 Producer: Running
# Wed Aug 23 14:15:42 2023 Consumer: Running
# Wed Aug 23 14:15:42 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:43 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:43 2023 > got 0.9123683782804672
# Wed Aug 23 14:15:43 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:44 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:44 2023 > got 0.6226447725144895
# Wed Aug 23 14:15:44 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:45 2023 > got 0.5288880212647503
# Wed Aug 23 14:15:45 2023 > got 0.16771174127100763
# Wed Aug 23 14:15:45 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:45 2023 > got 0.4753775258374501
# Wed Aug 23 14:15:45 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:46 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:46 2023 > got 0.8458233239973169
# Wed Aug 23 14:15:46 2023 > got 0.05565784190947276
# Wed Aug 23 14:15:46 2023 > got 0.24180088323657
# Wed Aug 23 14:15:46 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:47 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:47 2023 > got 0.7056199956314441
# Wed Aug 23 14:15:47 2023 Consumer: got nothing, waiting a while ...
# Wed Aug 23 14:15:47 2023 Producer: Done
# Wed Aug 23 14:15:48 2023 > got 0.6129823361556235
# Wed Aug 23 14:15:48 2023 Consumer: Done
