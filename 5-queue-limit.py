# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue, id):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep((id + 1)*0.1)
        # add to the queue 
        await queue.put(value)
        # print(f'{time.ctime()} Producer: put {value}') 
    # send an all done signal

    print(f'{time.ctime()} Producer {id}: Done') 

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

    # all done 
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create a shared queue 
    queue = asyncio.Queue(2)
    # start consumer 
    _=asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue, i) for i in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # run the producer and consumer 
    await queue.join()


# start the asyncio program 
asyncio.run(main())

# Running Result
# Wed Aug 23 14:53:53 2023 Consumer: Running
# Wed Aug 23 14:53:53 2023 Producer: Running
# Wed Aug 23 14:53:53 2023 Producer: Running
# Wed Aug 23 14:53:53 2023 Producer: Running
# Wed Aug 23 14:53:53 2023 Producer: Running
# Wed Aug 23 14:53:53 2023 Producer: Running
# Wed Aug 23 14:53:53 2023 > got 0.006268308301856318
# Wed Aug 23 14:53:54 2023 > got 0.617949927329134
# Wed Aug 23 14:53:54 2023 > got 0.0012566973185665908
# Wed Aug 23 14:53:54 2023 > got 0.06237171610707526
# Wed Aug 23 14:53:54 2023 > got 0.9701637301638221
# Wed Aug 23 14:53:55 2023 > got 0.19842857574828376
# Wed Aug 23 14:53:55 2023 > got 0.09680888254053177
# Wed Aug 23 14:53:56 2023 > got 0.876123508158725
# Wed Aug 23 14:53:56 2023 > got 0.7540654296958792
# Wed Aug 23 14:53:57 2023 > got 0.4644304756409491
# Wed Aug 23 14:53:58 2023 > got 0.427886844777978
# Wed Aug 23 14:53:58 2023 > got 0.883850477720699
# Wed Aug 23 14:53:59 2023 > got 0.3932946963025794
# Wed Aug 23 14:53:59 2023 > got 0.08615210133287121
# Wed Aug 23 14:54:00 2023 > got 0.7644675539120164
# Wed Aug 23 14:54:00 2023 > got 0.6981986243617256
# Wed Aug 23 14:54:01 2023 > got 0.7985864758381319
# Wed Aug 23 14:54:02 2023 > got 0.02242306257772264
# Wed Aug 23 14:54:02 2023 > got 0.8159718260586175
# Wed Aug 23 14:54:03 2023 > got 0.03966886320745511
# Wed Aug 23 14:54:03 2023 > got 0.6806255275129756
# Wed Aug 23 14:54:03 2023 > got 0.0061945364671317504
# Wed Aug 23 14:54:03 2023 > got 0.6610184255157577
# Wed Aug 23 14:54:04 2023 > got 0.8407709123206472
# Wed Aug 23 14:54:05 2023 > got 0.40397059666907287
# Wed Aug 23 14:54:05 2023 > got 0.8030526159691479
# Wed Aug 23 14:54:06 2023 > got 0.6573035348950618
# Wed Aug 23 14:54:07 2023 > got 0.9348854984218574
# Wed Aug 23 14:54:08 2023 > got 0.644068032152115
# Wed Aug 23 14:54:08 2023 > got 0.34088092782257184
# Wed Aug 23 14:54:09 2023 > got 0.7901602340367387
# Wed Aug 23 14:54:10 2023 > got 0.7287072965942776
# Wed Aug 23 14:54:10 2023 > got 0.5214110308494325
# Wed Aug 23 14:54:11 2023 > got 0.4957794146811343
# Wed Aug 23 14:54:11 2023 > got 0.578226842124812
# Wed Aug 23 14:54:11 2023 Producer 0: Done
# Wed Aug 23 14:54:12 2023 > got 0.7593923289328237
# Wed Aug 23 14:54:13 2023 > got 0.19645152477757832
# Wed Aug 23 14:54:13 2023 > got 0.6809534441495897
# Wed Aug 23 14:54:13 2023 Producer 1: Done
# Wed Aug 23 14:54:14 2023 > got 0.6931710384927371
# Wed Aug 23 14:54:14 2023 > got 0.35086082302967714
# Wed Aug 23 14:54:15 2023 > got 0.8524049312609717
# Wed Aug 23 14:54:16 2023 > got 0.9961554874862565
# Wed Aug 23 14:54:17 2023 > got 0.8117377171473318
# Wed Aug 23 14:54:17 2023 > got 0.6929160729525724
# Wed Aug 23 14:54:18 2023 > got 0.31626453358473594
# Wed Aug 23 14:54:18 2023 Producer 2: Done
# Wed Aug 23 14:54:18 2023 > got 0.4869197730766436
# Wed Aug 23 14:54:18 2023 Producer 3: Done
# Wed Aug 23 14:54:19 2023 > got 0.013487481250971545
# Wed Aug 23 14:54:19 2023 > got 0.18713303459217112
# Wed Aug 23 14:54:19 2023 > got 0.9394536189913556
# Wed Aug 23 14:54:19 2023 Producer 4: Done
# Wed Aug 23 14:54:20 2023 > got 0.8748152627157618