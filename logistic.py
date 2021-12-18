import matplotlib.pyplot as plt

class Logistic:
    def __init__(self, mu=3.5, x0=0.5, iter_num=500):
        self.mu = mu
        self.x0 = x0
        self.xs = [x0]
        self.iter_num = iter_num
        self.iterate()

    def iterate(self):
        x = self.x0
        for i in range(self.iter_num):
            x = x * self.mu * (1 - x)
            self.xs.append(x)

    def add_to_graph(self, color='b'):
        plt.scatter(range(self.iter_num + 1), self.xs, color=color,
                    label='('+str(self.x0)+','+str(self.mu)+')')

    def show_graph(self):
        plt.title('Logistic Mapping')
        plt.xlabel('iteration')
        plt.ylabel('x')
        plt.legend()
        plt.show()
        plt.clf()
