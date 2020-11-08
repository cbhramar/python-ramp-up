def adjustWidth(string,width):
	length = len(string)

	if length <= width:
		print(string)
		return

	out=""
	for i in range(0,length):
		if i==0 or i%width!=0:
			out+=string[i]
		else:
			print(out)
			out=string[i]
	print(out)

if __name__ == '__main__':
	s="Lorem ipsum enim voluptatibus porro veritatis. Hic eligendi nihil ut "
	s+="consequatur. Ut tenetur praesentium sunt eum alias est deserunt "
	s+="esse. Nesciunt libero cupiditate"
	adjustWidth(s,15)
