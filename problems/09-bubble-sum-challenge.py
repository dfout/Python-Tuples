# Create a function that returns a list of tuples that are sorted by the sum of
# the tuples. Hint: use the built-in range function.

# Write your function here.


def bubble_sum(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
        # Compare the sum of elements in each tuple
            if sum(data[j]) > sum(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]  # Swap elements

    return data

print(bubble_sum([(3, 5), (1, 3), (6, 5), (2, 8)])) #> [(1, 3), (3, 5), (2, 8), (6, 5)]
print(bubble_sum([(2, 5), (2, 5), (7, 8), (2, 6)])) #> [(2, 5), (2, 5), (2, 6), (7, 8)]
print(bubble_sum([(5, 6), (1, 2), (3, 0), (2, 4)])) #> [(1, 2), (3, 0), (2, 4), (5, 6)]
print(bubble_sum([(5, 4), (1, 0), (2, 1), (4, 1)])) #> [(1, 0), (2, 1), (4, 1), (5, 4)]


