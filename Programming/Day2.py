a = [eval(input("Enter number1")), eval(input("Enter number2")), eval(input("Enter number3")), eval(input("Enter letter a")), eval(input("Enter letter b"))]

List = []
for elem in a:
    if type(elem) is str:
        List.append(elem)

print (List)