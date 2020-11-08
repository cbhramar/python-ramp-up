def fizzbuzz(n,m,nums,strings):
	for i in range(n,m+1):
		out=""
		for j in range(0,len(nums)):
			if i%nums[j]==0:
				out+=strings[j]
		if out=="":
			out+=str(i)
		print(out)

if __name__ == '__main__':
	nums = [3,5,7]
	strings = ["fizz","buzz","fuzz"]
	fizzbuzz(1,100,nums,strings)
