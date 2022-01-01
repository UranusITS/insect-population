from math import sqrt
import random

from numpy import generic
from generator import Generator
from logistic import Logistic

def average(ls):
    ave = 0
    for item in ls:
        ave += item
    ave /= len(ls)
    return ave

def variance(ls):
    ave = average(ls)
    var = 0
    for item in ls:
        var += (item - ave) * (item - ave)
    var /= len(ls)
    return var

def sample_variance(ls):
    ave = average(ls)
    var = 0
    for item in ls:
        var += (item - ave) * (item - ave)
    var /= len(ls) - 1
    return var

def analyse_ave_var(ls, label=None):
    if label:
        print(label)
    print('len:', len(ls))
    print('ave:', average(ls))
    print('var:', variance(ls))
    print()

def analyse_sample(ls, n, label=None):
    if label:
        print(label)
    sample = random.sample(ls, n)
    ave = average(ls)
    var = variance(ls)
    ave_s = average(sample)
    var_s = sample_variance(sample)
    print('len:', len(ls))
    print('sample len:', len(sample))
    print('ave:', ave_s)
    print('var:', var_s)
    print('std_var:', sqrt(var_s))
    print('d_ave:', abs(ave_s-ave)/ave)
    print('d_var:', abs(var_s-var)/var)
    print()

def logistic_analyse():
    x0 = 0.66
    logistic = Logistic(mu=3.4, x0=x0)
    analyse_ave_var(logistic.xs, 'mu=3.4, x0=0.66')
    logistic = Logistic(mu=3.5, x0=x0)
    analyse_ave_var(logistic.xs, 'mu=3.5, x0=0.66')
    logistic = Logistic(mu=3.6, x0=x0)
    analyse_ave_var(logistic.xs, 'mu=3.6, x0=0.66')
    logistic = Logistic(mu=3.7, x0=x0)
    analyse_ave_var(logistic.xs, 'mu=3.7, x0=0.66')
    logistic = Logistic(mu=3.8, x0=x0)
    analyse_ave_var(logistic.xs, 'mu=3.8, x0=0.66')
    logistic = Logistic(mu=3.9, x0=x0)
    analyse_ave_var(logistic.xs, 'mu=3.9, x0=0.66')


def logistic_sample():
    x0 = 0.66
    logistic = Logistic(mu=3.4, x0=x0)
    analyse_sample(logistic.xs, 20, 'mu=3.4, x0=0.66')
    logistic = Logistic(mu=3.5, x0=x0)
    analyse_sample(logistic.xs, 20, 'mu=3.5, x0=0.66')
    logistic = Logistic(mu=3.6, x0=x0)
    analyse_sample(logistic.xs, 20, 'mu=3.6, x0=0.66')
    logistic = Logistic(mu=3.7, x0=x0)
    analyse_sample(logistic.xs, 20, 'mu=3.7, x0=0.66')
    logistic = Logistic(mu=3.8, x0=x0)
    analyse_sample(logistic.xs, 20, 'mu=3.8, x0=0.66')
    logistic = Logistic(mu=3.9, x0=x0)
    analyse_sample(logistic.xs, 20, 'mu=3.9, x0=0.66')

def insect_population_analyse():
    generator = Generator(import_file_name='insect_full')
    analyse_ave_var(generator.xs, 'min=0, max=4, x0=0.66')
    generator = Generator(import_file_name='insect_start_chaos')
    analyse_ave_var(generator.xs, 'min=3, max=4, x0=0.66')
    generator = Generator(import_file_name='insect_absolute_chaos')
    analyse_ave_var(generator.xs, 'min=3.7, max=4, x0=0.66')

def insect_population_sample():
    generator = Generator(import_file_name='insect_full')
    analyse_sample(generator.xs, 100, 'min=0, max=4, x0=0.66')
    generator = Generator(import_file_name='insect_start_chaos')
    analyse_sample(generator.xs, 100, 'min=3, max=4, x0=0.66')
    generator = Generator(import_file_name='insect_absolute_chaos')
    analyse_sample(generator.xs, 100, 'min=3.7, max=4, x0=0.66')

def normal_distribution_analyse(mu, sigma):
    generator = Generator(import_file_name='insect_start_chaos')
    generator.show_normal_distribution_graph(mu, sigma, fig_file='insect-3-4-0_66-500-nd.png')

if __name__ == '__main__':
    # logistic_analyse()
    # logistic_sample()
    # insect_population_analyse()
    # insect_population_sample()
    normal_distribution_analyse(0.53007, sqrt(0.03083))
    pass
