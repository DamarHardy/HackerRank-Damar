import os

# Complete the hourglassSum function below.
def hourglassSum(arr):
    row, col= 0, 0
    totalval=[]
    while row < 4:
        while col < 4:
            val = arr[row][col]+arr[row][col+1]+arr[row][col+2]+arr[row+1][col+1]+arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]
            totalval.append(val)
            col = col+1
        row = row+1
        col = 0

    maxval = max(totalval)
    print maxval
    return totalval


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'OUTPUT.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
