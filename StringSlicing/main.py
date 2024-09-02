fruit = "mango"

mangolength= len(fruit)

print(mangolength)
print(fruit[0:4]) ## including 0 but not 4 [0:(n-1)] > (4-1 = 3) it become [0:3] it prints [0],[1],[2],[3]
print(fruit[1:4]) ## including 1 but not 4 [0:(n-1)] > (4-1 = 3) it become [1:3] it prints [1],[2],[3]
print(fruit[2:]) ## it assumes [2:] is equivalent to [2:5], (5-1 = 4) it become [2:4] it print [2],[3],[4]
print(fruit[:5]) ## it assumes [:5] is equivalent to [0:5], (5-1 = 4) it become [0:4] it print [0],[1],[2],[3],[4]
print(fruit[-5:]) ## it become 5-5:5 > [0:5], [0:(n-1)] > (5-1 = 4) it become [0:5] now it print [0],[1],[2],[3],[4]
print(fruit[::2]) ## Start from the first character (m) takes every 2nd character
print(fruit[::1]) ## Start from the first character (m) and continue to take every character without skipping any.
print(fruit[::3]) ## Start from the first character (m) takes every 3rd character
print(fruit[-3:-1]) ## [len(fruit)-3:len(fruit)-1] > [5-3:5-1] > [2:4] > [2:n-1] > [2:4-1] > [2:3] it print [2],[3]
