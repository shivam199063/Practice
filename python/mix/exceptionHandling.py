
try:
    o=open("hello.py",mode='r') 
   
except FileNotFoundError:
    print("1: Please enter correct file path")

try:
    o=open("client.py",mode='r') 
    print(x)
except NameError:
    print("2: This is nameError here variable is not define:")
    
try:
    import io
    o=open("client.py",mode='r') 
    o.write("hello")
except io.UnsupportedOperation:
    print("3: Check your file mode try again")

finally:
    print("Print in all case")


print("Outside exception handling :>:shivam saini")


