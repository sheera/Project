#new comment
# comment1
#comment2
#comment3
# Print the mean of numbers given as argument
# edited to calculate mean of numbers in  file given as an argumen
# mean.py
import sys
sum = 0
n=0

if len(sys.argv) == 1:
	print 'Error : No arguments give.'
	sys.exit()

for num in open(sys.argv[1]):
    sum += float(num)
    n +=1

print sum / n

