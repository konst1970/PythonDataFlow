from Component import Component

class MyComponent(Component):
 
    def process(self, str1, str2):
        self.inputs.append(str1)
        self.inputs.append(str2)
        print("Inputs:", self.inputs)
        self.outputs.append(self.inputs[0]+self.inputs[1])
        print("Output:", self.outputs)
    
    def validate(self):
        pass


a = 'abc'
b = 'def'
A = MyComponent()
A.process(a, b)