john = 170
alice = 172
dommy= 150

if (john >= alice) and (john >= dommy):
   tallest = john
elif (alice >= john) and (alice >= dommy):
   tallest = alice
else:
   tallest = dommy

print("The tallest is:", tallest)