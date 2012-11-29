# Print the mean of numbers given as argument
# mean.py
import sys
sum = 0
if len(sys.argv) == 1:
	print 'Error : No arguments give.'
	sys.exit()

for num in sys.argv[1:]:
    sum += float(num)
print sum / (len(sys.argv) - 1)

