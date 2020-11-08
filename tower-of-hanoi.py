def moveSingleDisk(n,start,finish):
	print(str(n) + ": " + start + " -> " + finish)

def moveSubTower(n,start,finish,temp):
	if n==1:
		moveSingleDisk(n,start,finish)
	else:
		moveSubTower(n-1,start,temp,finish)
		moveSingleDisk(n,start,finish)
		moveSubTower(n-1,temp,finish,start)

def numberOfSteps(n):
	return pow(2,n)-1

if __name__ == '__main__':
	n = 3
	moveSubTower(n,'A','B','C')
	print("Takes "+str(numberOfSteps(n))+" steps")
