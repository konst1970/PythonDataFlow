from Component import Component


class MyComponent(Component):
    def process(self):
        self.outputs.append(self.inputs[0]+self.inputs[1])
        if type(self.outputs[0]) == str:
            return 0
        else:
            raise Exception('Wrong type of inputs')

    def validate(self):
        pass


if __name__=='__main__':
    a = 'abc'
    b = 'def'
    inp = [a,b]
    A = MyComponent(inputs=inp)
    A.process()
