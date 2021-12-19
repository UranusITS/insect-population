from generator import Generator

def insect_population_generate():
    Generator(export_file_name='insect_full', mu_min=0, mu_max=4, num=80000, x0=0.66)
    Generator(export_file_name='insect_start_chaos', mu_min=3, mu_max=4, num=20000, x0=0.66)
    Generator(export_file_name='insect_absolute_chaos', mu_min=3.7, mu_max=4, num=10000, x0=0.66)

if __name__ == '__main__':
    # insect_population_generate()
    pass
