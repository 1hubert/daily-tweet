class ExampleClass:
    def return_4_plus_x(self, x):
        return 4 + x

    def print_result(self, x):
        print(x)

    def do_it_all(self, x):
        result = self.return_4_plus_x(x)
        self.print_result(result)


ax = ExapmleClass()

ax.do_it_all(2)