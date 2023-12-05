stack =[]
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #들어온순서부터
print(stack[::-1]) #제일 상단부터