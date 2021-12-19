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

def analyse(ls, label=None):
    if label:
        print(label)
    print('len:', len(ls))
    print('ave:', average(ls))
    print('var:', variance(ls))
    print()

def logistic_analyse():
    x0 = 0.66
    logistic = Logistic(mu=3.4, x0=x0)
    analyse(logistic.xs, 'mu=3.4, x0=0.66')
    logistic = Logistic(mu=3.5, x0=x0)
    analyse(logistic.xs, 'mu=3.5, x0=0.66')
    logistic = Logistic(mu=3.8, x0=x0)
    analyse(logistic.xs, 'mu=3.8, x0=0.66')

def insect_population_analyse():
    generator = Generator(import_file_name='insect_full')
    analyse(generator.xs, 'min=0, max=4, x0=0.66')
    generator = Generator(import_file_name='insect_start_chaos')
    analyse(generator.xs, 'min=3, max=4, x0=0.66')
    generator = Generator(import_file_name='insect_absolute_chaos')
    analyse(generator.xs, 'min=3.7, max=4, x0=0.66')

if __name__ == '__main__':
    # logistic_analyse()
    # insect_population_analyse()
    pass
