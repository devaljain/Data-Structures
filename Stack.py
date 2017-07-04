class Stack:
	def __init__(self):
		self.items=[]
	def isEmpty(self):
		return self.items==[]
	
	
	def pop(self):
		if (len(self.items))!=0:
			return self.items.pop()

		else:
			print("Stack is Empty")
	def push(self,x):
		return self.items.append(x)
	def size(self):
		return len(self.items)
	def peek(self):
		return self.items[len(self.items)-1]
	
		
	def show(self):
		print(self.items)
		




