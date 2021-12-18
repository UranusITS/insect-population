from generator import Generator
from logistic import Logistic
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # generator = Generator(export_file_name='test1', x0=0.65, iter_num=1000)
    generator = Generator(import_file_name='test1')
    # generator.show_mu_x_graph()
    generator.show_frequency_distribution_graph()
    """
    mus = [3.5, 3.6, 3.7, 3.8, 3.9, 4.0]
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    for i in range(6):
        logistic = Logistic(mu=mus[i])
        logistic.add_to_graph(colors[i])
    logistic.show_graph()
    """
