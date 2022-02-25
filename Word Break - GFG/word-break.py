#User function Template for python3

def wordBreak(line, dictionary):
    line = line.replace(" ", "")
    dictionary = sorted(dictionary, key=len, reverse=True)
    for word in dictionary:
        while word in line:
            ind = line.index(word)
            line = line[0:ind] + line[ind + len(word):]
        
    return 1 if len(line) == 0 else 0
    # Complete this function

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends