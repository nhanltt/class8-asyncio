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
        # get a unit of work
        try:
            get_await = queue.get()
            # await the awaitable with a time out
            item = await asyncio.wait_for(get_await, 0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Gave up waiting ...')
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
# Wed Aug 23 14:22:04 2023 Producer: Running
# Wed Aug 23 14:22:04 2023 Consumer: Running
# Wed Aug 23 14:22:05 2023 Gave up waiting ...
# Wed Aug 23 14:22:05 2023 > got 0.6473407432753093
# Wed Aug 23 14:22:05 2023 > got 0.16726581081507164
# Wed Aug 23 14:22:05 2023 > got 0.0015302142661866025
# Wed Aug 23 14:22:06 2023 > got 0.29313950114216436
# Wed Aug 23 14:22:06 2023 Gave up waiting ...
# Wed Aug 23 14:22:06 2023 > got 0.7629431429047737
# Wed Aug 23 14:22:07 2023 Gave up waiting ...
# Wed Aug 23 14:22:07 2023 > got 0.5559625820332071
# Wed Aug 23 14:22:07 2023 Gave up waiting ...
# Wed Aug 23 14:22:08 2023 > got 0.7971444615597858
# Wed Aug 23 14:22:08 2023 Gave up waiting ...
# Wed Aug 23 14:22:08 2023 > got 0.5925262845881063
# Wed Aug 23 14:22:09 2023 Gave up waiting ...
# Wed Aug 23 14:22:09 2023 > got 0.5037228101652678
# Wed Aug 23 14:22:09 2023 Gave up waiting ...
# Wed Aug 23 14:22:09 2023 Producer: Done
# Wed Aug 23 14:22:09 2023 > got 0.5460823658499445
# Wed Aug 23 14:22:09 2023 Consumer: Done