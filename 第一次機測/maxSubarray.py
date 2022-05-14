# 學號: 10720111 / 10720107
# 姓名: 陳少暉 / 陳丕中

def Find_Maximum_Subarray(A):
    n = len(A)
    low, high, sum = _Find_Maximum_Subarray(A, 0, n - 1)

    print("Maximum-Subarray Problem:")
    print("Low =", low+1, "High =", high+1, "Sum =", sum)


def _Find_Maximum_Subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) // 2

        left_low, left_high, left_sum = _Find_Maximum_Subarray(A, low, mid)
        right_low, right_high, right_sum = _Find_Maximum_Subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = _Find_Max_Crossing_Subarray(A, low, mid, high)

        if (left_sum > right_sum and left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum and right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def _Find_Max_Crossing_Subarray(A, low, mid, high):
    left_sum = -3000000
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -3000000
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    cross_low = max_left
    cross_high = max_right
    cross_sum = left_sum + right_sum

    return cross_low, cross_high, cross_sum


size = input( '幾組資料:' )
size = int(size)
while size != 0:
    content = input( '內容: ' )
    content = content.split()
    # print( content )
    content = list( map( int, content ) )
    Find_Maximum_Subarray( content )

    size = input('幾組資料:')
    size = int(size)