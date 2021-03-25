import ipdb
import random

# persons list
PERSONS = [
    {
        "name": "John",
        "surname": "Rox",
        "age": 54
    },
    {
        "name": "Roger",
        "surname": "Cross",
        "age": 43
    },
    {
        "name": "Xor",
        "surname": "Rox",
        "age": 7
    },
    {
        "name": "Lemmi",
        "surname": "Star",
        "age": 20
    },
    {
        "name": "Petr",
        "surname": "roysman",
        "age": 16
    }
]

def quick_sort(arr, left, right, sort_field):
    if left >= right:
        return

    left_mark = left
    right_mark = right
    pivot_val = arr[right][sort_field]

    while left_mark <= right_mark:

        while arr[left_mark][sort_field] < pivot_val:
            left_mark += 1

        while arr[right_mark][sort_field] > pivot_val:
            right_mark -= 1

        if left_mark <= right_mark:
            temp = arr[left_mark]
            arr[left_mark] = arr[right_mark]
            arr[right_mark] = temp
            left_mark += 1
            right_mark -= 1

    quick_sort(arr, left, right_mark, sort_field)
    quick_sort(arr, left_mark, right, sort_field)


if __name__ == "__main__":
    print(PERSONS, '\n')

    quick_sort(PERSONS, 0, len(PERSONS) - 1, sort_field="age")

    print(PERSONS)

