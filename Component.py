class Component:
    def __init__(self, inputs=[]):
        self.inputs = [] 
        self.outputs = []
        if inputs:
            for i in inputs:
                self.inputs.append(i) 
 
    def process(self):
        pass

    def validate(self):
        pass
 
