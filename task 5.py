class minimumstack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return
        popped_value = self.stack.pop()
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()

    def minimum(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


def calculations(n, a, b, c, x0):
    total_sum = 0
    x = x0
    stack = minimumstack()

    for _ in range(n):
        x = ((a * x0 * x0 + b * x0 + c) // 100) % 1000000

        if x % 5 < 2:
            stack.pop()
        else:
            stack.push(x)

        if stack.stack:
            min_value = stack.minimum()
            if min_value is not None:
                total_sum += min_value

        x0 = x

    return total_sum

n, a, b, c, x0 = map(int, input().split())

print(calculations(n, a, b, c, x0))
