import threading
import time

exitFlag = 0
readcount = 0
writecount = 0
stack = []

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, operation):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.operation = operation
    def run(self):
        print ("Starting " + self.name)
        mutex(self.operation, self.name)
        print ("Exiting " + self.name)
        print (stack)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

def mutex(operation, name):
	global readcount, writecount
	#if a read any no
	#write only one
	tname = name
	complete = 0
	while (complete == 0):
		if operation == "R":
			readcount += 1
			read(tname)
			complete = 1
		elif operation == "W":
			if writecount == 1:
				pass
			elif writecount == 0:
				writecount += 1
				write(tname)
				complete = 1
			else:
				print ("error > 1 writing")
		else:
			print ("Error invalid operation")		 			

def read(tname):
	global readcount
	time.sleep(5)
	print (tname + " I am reading")
	print (stack)
	time.sleep(5)
	readcount -= 1

def write(tname):
	global writecount
	time.sleep(2)
	print (tname + " I am writing")
	stack.append(1)
	time.sleep(2)
	writecount -= 1
# Create new threads
thread1 = myThread(1, "Thread-1", 1,"W")
thread2 = myThread(2, "Thread-2", 1,"W")
thread3 = myThread(3, "Thread-3", 1, "R")
thread4 = myThread(4, "Thread-4", 1, "R")
thread5 = myThread(5, "Thread-5", 1, "R")
thread6 = myThread(6, "Thread-6", 1, "R")
thread7 = myThread(7, "Thread-7", 1, "R")
thread8 = myThread(2, "Thread-2", 1,"W")

# Start new Threads
thread1.start()
thread8.start()
thread2.start()
thread5.start()
thread4.start()
thread3.start()
thread6.start()
thread7.start()

print ("Exiting Main Thread")			