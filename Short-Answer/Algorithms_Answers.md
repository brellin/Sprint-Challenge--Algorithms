#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) Linear time
while (a < n * n /* n/): <= we can remove the last multiplication, because it is also being calculated by the increment
a = a + n /* n/ <= a increments by n and n is incremented by itself, itself times - so it's equivalent to while(a < n): a += 1
b) O(n log n) Linearithmic time
A for loop that has half of n being looped inside of it that is being traversed at an exponential rate will take slightly more time (in larger input numbers) than O(n)

c) O(n**2) Polynomial time
As the bunnies grow, the time it takes for this function to execute will double, due to (2 + bunnyEars(n - 1))

## Exercise II

store the lowest floor that an egg breaks on
find the middle floor
if an egg is dropped from the first floor and breaks, return the lowest floor variable
if an egg is dropped from the middle floor and breaks, return the lowest floor variable
if an egg is dropped from the middle or last floor and does not break, call this function for the top and bottom floors and store the results in the lowest floor variable
return the lowest floor variable
O(n log n) Linearithmic time
