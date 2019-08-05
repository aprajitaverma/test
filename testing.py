import time
from multiprocessing import Process, Manager
from threading import Thread
from itertools import islice
from collections import Counter
import os

wordcount = Counter()

def word_counter():
    print("Child 1",os.getpid())
    with open("temp_big_sentences.txt") as f:
        while True:
            lines =list(islice(f,1000000))
            for line in lines:
                wordcount.update(line.split())

            if not lines:
                break        
    return wordcount


if __name__ == '__main__':
    print("parent_id",os.getpid())
    starttime = time.time()
    jobs=[]

    #print(word_counter())
    for i in range(1):
        t =Thread(target=word_counter)
        jobs.append(t)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
        
    print(wordcount)
    print('That took {} seconds'.format(time.time() - starttime))
