import random,time
def print_infinite_loop():
    count = random.randint(8,10)
    while count<15000:
        print(count)
        # time.sleep(1)
        count+=1

print_infinite_loop()