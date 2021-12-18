import matplotlib.pyplot as plt
from logistic import Logistic

class Generator:
    def __init__(self, mu_min=3.0, mu_max=4.0, num=10000, x0=0.5, iter_num=500,
                 import_file_name=None, export_file_name=None):
        self.mu_min = mu_min
        self.mu_max = mu_max
        self.num = num
        self.x0 = x0
        self.iter_num = iter_num
        self.mus = list()
        self.xs = list()
        if import_file_name:
            self.open_from_file(import_file_name)
        else:
            self.generate_from_data()
        if export_file_name:
            self.save_to_file(export_file_name)

    def generate_from_data(self):
        mu = self.mu_min
        while mu <= self.mu_max:
            log = Logistic(mu=mu, x0=self.x0, iter_num=self.iter_num)
            self.mus.append(mu)
            self.xs.append(log.xs[-1])
            mu += (self.mu_max - self.mu_min) / self.num

    def open_from_file(self, file_name):
        with open('data/' + file_name, 'r') as file:
            self.mu_min = float(file.readline())
            self.mu_max = float(file.readline())
            self.num = float(file.readline())
            self.x0 = float(file.readline())
            self.iter_num = float(file.readline())
            line = file.readline()
            while line != '####\n':
                self.mus.append(float(line))
                line = file.readline()
            line = file.readline()
            while line != '####\n':
                self.xs.append(float(line))
                line = file.readline()
    
    def save_to_file(self, file_name):
        with open('data/' + file_name, 'w') as file:
            file.write(str(self.mu_min) + '\n')
            file.write(str(self.mu_max) + '\n')
            file.write(str(self.num) + '\n')
            file.write(str(self.x0) + '\n')
            file.write(str(self.iter_num) + '\n')
            for mu in self.mus:
                file.write(str(mu) + '\n')
            file.write('####\n')
            for x in self.xs:
                file.write(str(x) + '\n')
            file.write('####\n')

    def show_mu_x_graph(self):
        plt.scatter(self.mus, self.xs, s=2)
        plt.title('insect-population model')
        plt.xlabel('k')
        plt.ylabel('x')
        plt.show()
        plt.clf()

    def show_frequency_distribution_graph(self):
        plt.hist(self.xs, bins=10)
        plt.show()
        plt.clf()
