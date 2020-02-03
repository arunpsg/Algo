def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = reverse_merge_sort(input_list)
    print("sorted_list : ", sorted_list)
    out1= []
    out2 = []
    for k, v in enumerate(sorted_list):
        if k % 2 == 0:
            out1.append(str(v))
        else:
            out2.append(str(v))
    out_one = ''.join(out1)
    out_two = ''.join(out2)
    print("out_one : ", out_one)
    print("out_two : ", out_two)
    return int(out_one), int(out_two)
    pass


def reverse_merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    left = reverse_merge_sort(left)
    right = reverse_merge_sort(right)

    return reverse_merge(left, right)


def reverse_merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged = merged + left[left_index:]
    merged = merged + right[right_index:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 100, 0], [1000, 1]])
test_function([[10000, 100, 0], [100000, 100]])
test_function([[1, 9, 0], [90, 1]])