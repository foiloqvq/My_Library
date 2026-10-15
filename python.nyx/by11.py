print("11")


your = 0
my = 0


tall_input = input("you are my father ( enter:q):")


while tall_input != "q":
    num = float(tall_input)
    your = your + num
    your += num
    my += 1
    tall_input = input("you are my father ( enter:q):")
if my == 0:
   result = 0
else:
     result = your / my
     print("The number you entered is" + str(result))
