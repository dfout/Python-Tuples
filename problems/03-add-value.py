# Create a function that takes in a tuple, `tup` and a value, `val`. The
# function should return a tuple with the given value added to the end of the
# tuple.

# Write your function here.
def add_value(tup, val):
    return tup + (val,)

print(add_value((1,2,3,4), 5)) #> (1, 2, 3, 4, 5)
print(add_value(("a", "b", "c"), "d")) #> ('a', 'b', 'c', 'd')
print(add_value((8, 9, "d", 6), "a")) #> (8, 9, 'd', 6, 'a')


##FOR DICTIONARY
## .get will not return an error if not found, it will return None. Which is helpful when you do not want your code to stop running. 