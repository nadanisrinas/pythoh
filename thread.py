from threading import Thread
import time
def rebahan_bentar():
    print("I'm sleep")
    time.sleep (1)
    print("I'm awake")
# Create new child process
process_1 = Thread(target=rebahan_bentar)
process_2 = Thread(target=rebahan_bentar)
start = time.time()
process_1.start()
process_2.start()

process_2.join()
process_1.join()

end = time.time()
print("the time was {}".format(end-start))

