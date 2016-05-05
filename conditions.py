import time
print("numbers between 33 and 77")
for x in range(100):
     if 33 <= 2*x <= 77:  # plus concis et plus lisible
         print(x, "not in range")
     else:
         print(x, "in range")
#this is just for windows cmd(so it doesn't close to quick)
time.sleep(7)