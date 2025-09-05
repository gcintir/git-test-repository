print("hello world")

def test():
    return 1

index=-1

def inc_index():
    global index
    index+=1
    return index

def inc_index(num):
    global index
    index+=num
    return index