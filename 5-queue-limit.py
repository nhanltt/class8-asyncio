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

    # all done 
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create a shared queue 
    queue = asyncio.Queue(2)
    # start consumer 
    _=asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # run the producer and consumer 
    await queue.join()


# start the asyncio program 
asyncio.run(main())

# Running Result
# Wed Aug 23 14:38:53 2023 Consumer: Running
# Wed Aug 23 14:38:53 2023 Producer: Running
# Wed Aug 23 14:38:53 2023 Producer: Running
# Wed Aug 23 14:38:53 2023 Producer: Running
# Wed Aug 23 14:38:53 2023 Producer: Running
# Wed Aug 23 14:38:53 2023 Producer: Running
# Wed Aug 23 14:38:53 2023 Producer: put 0.10102304555096275
# Wed Aug 23 14:38:53 2023 > got 0.10102304555096275
# Wed Aug 23 14:38:53 2023 Producer: put 0.07070574550947772
# Wed Aug 23 14:38:53 2023 > got 0.07070574550947772
# Wed Aug 23 14:38:54 2023 Producer: put 0.5396764702780082
# Wed Aug 23 14:38:54 2023 > got 0.5396764702780082
# Wed Aug 23 14:38:54 2023 Producer: put 0.5550644329398705
# Wed Aug 23 14:38:54 2023 Producer: put 0.5131516174106053
# Wed Aug 23 14:38:54 2023 > got 0.5550644329398705
# Wed Aug 23 14:38:54 2023 Producer: put 0.9328478458041471
# Wed Aug 23 14:38:55 2023 > got 0.5131516174106053
# Wed Aug 23 14:38:55 2023 Producer: put 0.37496595714989456
# Wed Aug 23 14:38:55 2023 > got 0.9328478458041471
# Wed Aug 23 14:38:55 2023 Producer: put 0.9579978617451312
# Wed Aug 23 14:38:56 2023 > got 0.37496595714989456
# Wed Aug 23 14:38:56 2023 Producer: put 0.5372256379951592
# Wed Aug 23 14:38:57 2023 > got 0.9579978617451312
# Wed Aug 23 14:38:57 2023 Producer: put 0.9826739641902406
# Wed Aug 23 14:38:58 2023 > got 0.5372256379951592
# Wed Aug 23 14:38:58 2023 Producer: put 0.5913473884675506
# Wed Aug 23 14:38:58 2023 > got 0.9826739641902406
# Wed Aug 23 14:38:58 2023 Producer: put 0.02973116922379737
# Wed Aug 23 14:38:59 2023 > got 0.5913473884675506
# Wed Aug 23 14:38:59 2023 Producer: put 0.6083543903960726
# Wed Aug 23 14:39:00 2023 > got 0.02973116922379737
# Wed Aug 23 14:39:00 2023 Producer: put 0.25349255966441087
# Wed Aug 23 14:39:00 2023 > got 0.6083543903960726
# Wed Aug 23 14:39:00 2023 Producer: put 0.3505651641291845
# Wed Aug 23 14:39:00 2023 > got 0.25349255966441087
# Wed Aug 23 14:39:00 2023 Producer: put 0.69713702233862
# Wed Aug 23 14:39:01 2023 > got 0.3505651641291845
# Wed Aug 23 14:39:01 2023 Producer: put 0.20814326101801295
# Wed Aug 23 14:39:01 2023 > got 0.69713702233862
# Wed Aug 23 14:39:01 2023 Producer: put 0.6922113111317917
# Wed Aug 23 14:39:02 2023 > got 0.20814326101801295
# Wed Aug 23 14:39:02 2023 Producer: put 0.5250535219215205
# Wed Aug 23 14:39:02 2023 > got 0.6922113111317917
# Wed Aug 23 14:39:02 2023 Producer: put 0.9392446274936267
# Wed Aug 23 14:39:03 2023 > got 0.5250535219215205
# Wed Aug 23 14:39:03 2023 Producer: put 0.9351834434165819
# Wed Aug 23 14:39:03 2023 > got 0.9392446274936267
# Wed Aug 23 14:39:03 2023 Producer: put 0.5814221338707022
# Wed Aug 23 14:39:04 2023 > got 0.9351834434165819
# Wed Aug 23 14:39:04 2023 Producer: put 0.2817064799051139
# Wed Aug 23 14:39:05 2023 > got 0.5814221338707022
# Wed Aug 23 14:39:05 2023 Producer: put 0.24241549011638608
# Wed Aug 23 14:39:06 2023 > got 0.2817064799051139
# Wed Aug 23 14:39:06 2023 Producer: put 0.7947202092511435
# Wed Aug 23 14:39:06 2023 > got 0.24241549011638608
# Wed Aug 23 14:39:06 2023 Producer: put 0.7999029171723961
# Wed Aug 23 14:39:06 2023 > got 0.7947202092511435
# Wed Aug 23 14:39:06 2023 Producer: put 0.36293209615594557
# Wed Aug 23 14:39:07 2023 > got 0.7999029171723961
# Wed Aug 23 14:39:07 2023 Producer: put 0.012955757238121146
# Wed Aug 23 14:39:08 2023 > got 0.36293209615594557
# Wed Aug 23 14:39:08 2023 Producer: put 0.9340845972041371
# Wed Aug 23 14:39:08 2023 > got 0.012955757238121146
# Wed Aug 23 14:39:08 2023 Producer: put 0.057633738376374755
# Wed Aug 23 14:39:08 2023 > got 0.9340845972041371
# Wed Aug 23 14:39:08 2023 Producer: put 0.21100905531279168
# Wed Aug 23 14:39:09 2023 > got 0.057633738376374755
# Wed Aug 23 14:39:09 2023 Producer: put 0.8206100678611205
# Wed Aug 23 14:39:09 2023 > got 0.21100905531279168
# Wed Aug 23 14:39:09 2023 Producer: put 0.6482400210615403
# Wed Aug 23 14:39:09 2023 > got 0.8206100678611205
# Wed Aug 23 14:39:09 2023 Producer: put 0.2156745835815268
# Wed Aug 23 14:39:10 2023 > got 0.6482400210615403
# Wed Aug 23 14:39:10 2023 Producer: put 0.21906404352976483
# Wed Aug 23 14:39:10 2023 Producer: Done
# Wed Aug 23 14:39:11 2023 > got 0.2156745835815268
# Wed Aug 23 14:39:11 2023 Producer: put 0.7290326049475964
# Wed Aug 23 14:39:11 2023 > got 0.21906404352976483
# Wed Aug 23 14:39:11 2023 Producer: put 0.036314911228450875
# Wed Aug 23 14:39:11 2023 > got 0.7290326049475964
# Wed Aug 23 14:39:11 2023 Producer: put 0.1356962608181279
# Wed Aug 23 14:39:12 2023 > got 0.036314911228450875
# Wed Aug 23 14:39:12 2023 Producer: put 0.928431117555323
# Wed Aug 23 14:39:12 2023 > got 0.1356962608181279
# Wed Aug 23 14:39:12 2023 Producer: put 0.004260176292461226
# Wed Aug 23 14:39:12 2023 > got 0.928431117555323
# Wed Aug 23 14:39:12 2023 Producer: put 0.46251524391046883
# Wed Aug 23 14:39:13 2023 > got 0.004260176292461226
# Wed Aug 23 14:39:13 2023 Producer: put 0.688478094671314
# Wed Aug 23 14:39:13 2023 > got 0.46251524391046883
# Wed Aug 23 14:39:13 2023 Producer: put 0.11730913875273818
# Wed Aug 23 14:39:14 2023 > got 0.688478094671314
# Wed Aug 23 14:39:14 2023 Producer: put 0.46118803404602393
# Wed Aug 23 14:39:14 2023 > got 0.11730913875273818
# Wed Aug 23 14:39:14 2023 Producer: put 0.5543078234670722
# Wed Aug 23 14:39:15 2023 > got 0.46118803404602393
# Wed Aug 23 14:39:15 2023 Producer: put 0.42862308279741934
# Wed Aug 23 14:39:15 2023 Producer: Done
# Wed Aug 23 14:39:15 2023 > got 0.5543078234670722
# Wed Aug 23 14:39:15 2023 Producer: put 0.5960611603648069
# Wed Aug 23 14:39:15 2023 Producer: Done
# Wed Aug 23 14:39:16 2023 > got 0.42862308279741934
# Wed Aug 23 14:39:16 2023 Producer: put 0.3825141071933027
# Wed Aug 23 14:39:16 2023 Producer: Done
# Wed Aug 23 14:39:16 2023 > got 0.5960611603648069
# Wed Aug 23 14:39:16 2023 Producer: put 0.04671022029056704
# Wed Aug 23 14:39:17 2023 > got 0.3825141071933027
# Wed Aug 23 14:39:17 2023 Producer: put 0.5400913215876871
# Wed Aug 23 14:39:17 2023 Producer: Done
# Wed Aug 23 14:39:17 2023 > got 0.04671022029056704
# Wed Aug 23 14:39:17 2023 > got 0.5400913215876871