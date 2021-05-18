from Component import Component
from MyComponent import  MyComponent


class Nodelist:
    def __init__(self):
        self.component_dict = {}

    def add_component(self, key_component, value_component):
        if key_component in self.component_dict:
            self.component_dict[key_component].extend([value_component])
            return 0
        elif key_component not in self.component_dict:
            self.component_dict[key_component] = [value_component]
            return 0
        else:
            raise Exception("Component does not exists")



a = 'abc'
b = 'def'
inp = [a,b]
A_Component = MyComponent(inputs=inp)
B_Component = MyComponent(inputs=inp)
C_list = Nodelist()
C_list.add_component(A_Component, B_Component)
C_list.add_component(A_Component, B_Component)