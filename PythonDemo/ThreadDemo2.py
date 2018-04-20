#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Queue
import threading
import time

exitFlag = 0

threadList = ["thread-1","thread-2","thread-3"]
nameList = ["one","two","three","four","five"]
lock = threading.Lock()
workQueue = Queue.Queue(10)

threads = []
threadID = 1

class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.q=q
    def run(self):
        print 'starting ' + self.name
        process_data(self.name,self.q)
        print 'exiting ' + self.name

def process_data(threadName,q):
    while not exitFlag:
        lock.acquire()
        if not workQueue.empty():
            data = q.get()
            lock.release()
            print "%s processing %s" % (threadName, data)
        else:
            lock.release()
        time.sleep(1)

lock.acquire()
for word in nameList:
    workQueue.put(word)
lock.release()

for tName in threadList:
    thread = myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()

print "exiting main thread."

















