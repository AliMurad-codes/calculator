f=input("First value:")
s=input("second value:")
choose=input("sum,sub,div,mul")
sum=int(f)+int(s)
sub=int(f)-int(s)
div=int(f)/int(s)
mul=int(f)*int(s)


if choose == "sum":
	print("sum of two numbers:",sum) 
elif choose =="sub":
	print("subtraction of two number:",sub)
elif choose =="div":
	print("div of number:",div)
elif choose =="mul":
	print("multiplication of two number:",mul)
else:
	print("wrong choose")