import ipdb
import random

# un-order persons list
PERSONS = [
    {
        "name": "Murray",
        "surname": "Rothbard",
        "age": 81
    },
    {
        "name": "Robbin",
        "surname": "Robb",
        "age": 25
    },
    {
        "name": "Jey",
        "surname": "Ross",
        "age": 7
    },
    {
        "name": "Kylo",
        "surname": "Ren",
        "age": 34
    },
    {
        "name": "Roger",
        "surname": "Federer",
        "age": 10
    }
]

def merge_sort(arr, sort_field):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    l_side = arr[:mid]
    r_side = arr[mid:]
    merge_sort(l_side, sort_field)
    merge_sort(r_side, sort_field)

    i = j = k = 0
    # i - left side counter
    # j - right side counter
    # k - array position
    while i < len(l_side) and j < len(r_side):
        if l_side[i][sort_field] < r_side[j][sort_field]:
            arr[k] = l_side[i]
            i += 1  # move the left side counter
        else:
            arr[k] = r_side[j]
            j += 1  # move the right side counter

        k += 1  # move the array position

    while i < len(l_side):
        arr[k] = l_side[i]
        i += 1
        k += 1

    while j < len(r_side):
        arr[k] = r_side[j]
        j += 1
        k += 1


if __name__ == "__main__":
    print(PERSONS, '\n')

    merge_sort(PERSONS, sort_field="age")

    print(PERSONS)

