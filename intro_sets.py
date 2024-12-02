

def average(array):
    array=set(array)
    return sum(array)/len(array)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
