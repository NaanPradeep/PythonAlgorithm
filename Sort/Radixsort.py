def radix_sort(array):

    
    exp = 1
    max_digit = max(array)

    while exp < max_digit:

        output = [list() for i in range(10)]

        for i in range(len(array)):
            index = int(array[i]/exp)
            output[(index) % 10].append(array[i])
        

        a = 0
        for j in range(10):
            parted_output = output[j]
            for elements in parted_output:
                array[a] = elements
                a += 1

        exp *= 10
    return array



y = radix_sort([2, 524, 1841, 2565, 78, 125])
print(y)

