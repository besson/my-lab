class Knapsack:

    def __init__(self, values, weights, w):
        self._values = values
        self._weights = weights
        self._w = w

    def calculate_with_repetition(self):
        m = {}
        m[0] = 0

        for i in range(1, self._w + 1):
            total_value = 0

            try:
                m[i] = self._values[self._weights.index(i)]
            except:
                m[i] = 0
                pass

            for j in range(1, i):
                value = max(m[i], m[j] + m[i - j])

                if value > m[i]:
                    m[i] = value

            if m[i] > total_value:
                total_value = m[i]

        return total_value


    def calculate(self):
        m = {}
        m[0] = 0

        for i in range(1, self._w + 1):

            try:
                m[i] = self._values[self._weights.index(i)]
            except:
                m[i] = 0
                pass

            value = m[i]

            for j in range(1, i):
                if j != (i - j):
                    try:
                        new_value = self._values[self._weights.index(j)] + self._values[self._weights.index(i-j)]
                        value = max(m[i], m[i -1], new_value)
                    except:
                        pass

                if value > m[i]:
                    m[i] = value

        return m[self._w]



