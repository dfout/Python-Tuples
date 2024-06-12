# It's time to explore the *tuple* object and how to use it.

# Follow the instructions in the code comments. Be sure to test your work by
# running your code!

# For the bonus, remember you can split a returned tuple to variables: `(a,b,c)
# = myfunc()`

# DO NOT EDIT
odds = 1,3,5,7,9
evens = 2,4,6,8

print(sum(list(odds)))
print(sum(list(evens)))

# Step 1: Print out the result of adding evens to odds
print(odds + evens)

# Step 2: Print out the result of multiplying odds by three
print(tuple(num *3 for num in odds))

# Step 3A: Use print to find out if odds is less than evens
print(odds < evens)

# Step 3B: Print out your explanation of why 3A has that result
print('odds is less than evens because its first value is less than even"s first value ')

# Step 4: Print out the average of the numbers in evens using one line of code
print((sum(list(odds)))/ len(odds))

# Step 5A: Write a function 'minmaxmean' that accepts an iterable and
#         returns the minimum value, the maximum value and the average (mean)

def minmaxmean(iterable):
    mini = min(iterable)
    maxi = max(iterable)
    return (mini, maxi, (sum(list(iterable)))/ len(iterable))

# Step 5B: Use print to confirm you function is working on evens and odds
print(minmaxmean(odds))
print(minmaxmean(evens))

# BONUS: Call your function with a new tuple of your own creation
#        And print the results in a pretty way

print(minmaxmean((5,6,7,8,9,0)))