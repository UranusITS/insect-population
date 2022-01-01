from generator import Generator
from logistic import Logistic

def logistic_figure():
    x0 = 0.66
    mus = [3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0]
    colors = 'krygcbm'
    for i in range(6):
        logistic = Logistic(mu=mus[i], x0=x0)
        logistic.add_to_graph(colors[i])
    logistic.show_graph('logistic-full.png')
    logistic = Logistic(mu=3.4, x0=x0)
    logistic.add_to_graph()
    logistic.show_graph('logistic-3_4-0_66.png')
    logistic = Logistic(mu=3.5, x0=x0)
    logistic.add_to_graph()
    logistic.show_graph('logistic-3_5-0_66.png')
    logistic = Logistic(mu=3.8, x0=x0)
    logistic.add_to_graph()
    logistic.show_graph('logistic-3_8-0_66.png')

def insect_population_figure():
    generator = Generator(import_file_name='insect_full')
    generator.show_mu_x_graph(fig_file='insect-0-4-0_66-500-mx.png')
    generator.show_frequency_distribution_graph(bins=20, fig_file='insect-0-4-0_66-500-fd.png')
    generator = Generator(import_file_name='insect_start_chaos')
    generator.show_mu_x_graph(fig_file='insect-3-4-0_66-500-mx.png')
    generator.show_frequency_distribution_graph(bins=20, fig_file='insect-3-4-0_66-500-fd.png')
    generator = Generator(import_file_name='insect_absolute_chaos')
    generator.show_mu_x_graph(fig_file='insect-3_7-4-0_66-500-mx.png')
    generator.show_frequency_distribution_graph(bins=20, fig_file='insect-3_7-4-0_66-500-fd.png')

if __name__ == '__main__':
    # logistic_figure()
    # insect_population_figure()
    pass
