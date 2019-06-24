print("Hello human.")
x = input()
print("Number to float:")
y = input()
print("Integer:")
z = input()

mystring = x
myfloat = y
myint = z

if mystring == "hello":
    print("String: %s" % mystring)
elif mystring != "hello":
    print("Rude of you not to say hello!")
if isinstance(myfloat, float) and myfloat == float(10):
    print("Float: %f" % myfloat);
elif (myfloat, float) and myfloat != float(10):
    print("Float: Float does not match.")
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
elif (myint, int) and myint != 20:
    print("Integer: Incorrect Integer")
