import random
import matplotlib.pyplot as plt

class Generator:
    def __init__(self, min=0., max=2., num=10000, import_file_name=None, output_file_name=None):
        self.min = min
        self.max = max
        self.num = num
        self.k = list()
        self.x = list()
        if import_file_name:
            self.generate_from_file(import_file_name)
        else:
            self.generate_from_data()
        if output_file_name:
            self.save_to_file(output_file_name)

    def generate_from_data(self):
        i = self.min
        while i <= self.max:
            xx=random.uniform(0.,1.)
            for j in range(1000):
                xx = 1 - i * xx * xx
            self.k.append(i)
            self.x.append(xx)
            i += (self.max - self.min) / self.num

    def generate_from_file(self, file_name):
        with open('data/' + file_name, 'w') as file:
            self.min = float(file.readline())
            self.max = float(file.readline())
            self.num = float(file.readline())
            line = file.readline()
            while line != '####':
                self.k.append(float(line))
                line = file.readline()
            while line != '####':
                self.x.append(float(line))
                line = file.readline()
    
    def save_to_file(self, file_name):
        with open('data/' + file_name, 'w') as file:
            file.write(str(self.min) + '\n')
            file.write(str(self.max) + '\n')
            file.write(str(self.num) + '\n')
            for kk in self.k:
                file.write(str(kk) + '\n')
            file.write('####')
            for xx in self.x:
                file.write(str(xx) + '\n')
            file.write('####')

    def show_graph(self):
        plt.scatter(self.k, self.x, s=2)
        plt.title("insect-population model")
        plt.xlabel("k")
        plt.ylabel("x")
        plt.show()
