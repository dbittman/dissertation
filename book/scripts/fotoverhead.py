import sys
import matplotlib.pyplot as plt
import sys
import pandas as pd
import os
import numpy as np
import matplotlib as mpl
import pylab

mpl.use("Agg")
pylab.figure(num=None, figsize=(4, 3), facecolor='w', edgecolor='k')
# mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["r", "k", "c", "m", "g"])

path = sys.argv[2]
output = sys.argv[1]

if os.name == 'nt':
    df = pd.read_csv(path, encoding='utf-16le', skipinitialspace=True)
else:
    df = pd.read_csv(path, skipinitialspace=True)

df.columns = df.columns.str.replace(' ', '')


def g1():
    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    oc = 100
    data = df.query('OBJECTS == @oc')

    vals = data['FOT_ENTRIES'].values
    xs = list(map(lambda v: v / data['NODES'].values[0], data['EDGES'].values))
    fot = ax.scatter(xs, vals, label='FOT Entries')

    ax.set_xlabel('Number of Edges per Node')
    ax.set_ylabel('Count')

    vals = data['TOTAL_PTRS'].values
    ptrs = ax.scatter(xs, vals, label='Total Pointers')

    ax.legend(handles=[fot, ptrs])

    plt.show()


def get_fot(df):
    return np.mean(df['FOT_ENTRIES'].values)


def get_fot_std(df):
    return np.std(df['FOT_ENTRIES'].values) * 1.96


def get_total(df):
    return np.mean(df['TOTAL_PTRS'].values)


def calc_overheads(fot, total):
    vaddr = total * 64
    twz_overhead = fot * 256 + vaddr
    twz256_overhead = fot * (256 + 128) + vaddr
    pmdk_overhead = total * 64 + vaddr
    pmdk128_overhead = total * 128 + vaddr
    pmdk256_overhead = total * 256 + vaddr
    return [twz_overhead, twz256_overhead, pmdk_overhead,
            pmdk128_overhead, pmdk256_overhead, vaddr]


def calc_overheads_std(fotstd, total):
    vaddr = total * 64
    twz_overhead = fotstd * 256
    twz256_overhead = fotstd * (256 + 128)
    if twz256_overhead < vaddr / 100:
        twz256_overhead = vaddr / 100
    if twz_overhead < vaddr / 100:
        twz_overhead = vaddr / 100
    return [twz_overhead, twz256_overhead, vaddr]


names = ['Twizzler', 'Twizzler 256', 'PMDK', 'PMDK 128', 'PMDK 256']

sparse10 = df.query('EDGES == 1000 and OBJECTS == 10')
dense10 = df.query('EDGES == 900000 and OBJECTS == 10')

sparse100 = df.query('EDGES == 1000 and OBJECTS == 100')
dense100 = df.query('EDGES == 900000 and OBJECTS == 100')

sparse10_fot = get_fot(sparse10)
sparse10_ptrs = get_total(sparse10)
sparse100_fot = get_fot(sparse100)
sparse100_ptrs = get_total(sparse100)
dense10_fot = get_fot(dense10)
dense10_ptrs = get_total(dense10)
dense100_fot = get_fot(dense100)
dense100_ptrs = get_total(dense100)

sparse10_fotstd = calc_overheads_std(
    get_fot_std(sparse10), get_total(sparse10))
sparse100_fotstd = calc_overheads_std(
    get_fot_std(sparse100), get_total(sparse100))
dense10_fotstd = calc_overheads_std(get_fot_std(dense10), get_total(dense10))
dense100_fotstd = calc_overheads_std(
    get_fot_std(dense100), get_total(dense100))

sparse10_overheads = calc_overheads(sparse10_fot, sparse10_ptrs)
sparse100_overheads = calc_overheads(sparse100_fot, sparse100_ptrs)
dense10_overheads = calc_overheads(dense10_fot, dense10_ptrs)
dense100_overheads = calc_overheads(dense100_fot, dense100_ptrs)

overheads = [sparse100_overheads, sparse10_overheads,
             dense100_overheads, dense10_overheads]
overhead_names = ['Sparse Graph\nSmall Objects', 'Sparse Graph\nBig Objects',
                  'Dense Graph\nSmall Objects', 'Dense Graph\nBig Objects']

x1 = list(range(1, 31 - 6, 6))
x2 = list(range(2, 32 - 6, 6))
x3 = list(range(3, 33 - 6, 6))
x4 = list(range(4, 34 - 6, 6))
x5 = list(range(5, 35 - 6, 6))

scale = 1

overhead_errs = [sparse100_fotstd, sparse10_fotstd,
                 dense100_fotstd, dense10_fotstd]

print(overhead_errs)

p1 = plt.bar(
    x1, list(map(lambda x: x[0] / (scale * x[5]), overheads)), yerr=list(map(lambda e: e[0] / (scale * e[2]), overhead_errs)))
p2 = plt.bar(x2, list(map(lambda x: x[1] / (scale * x[5]), overheads)),
             yerr=list(map(lambda e: e[1] / (scale * e[2]), overhead_errs)))
p3 = plt.bar(x3, list(map(lambda x: x[2] / (scale * x[5]), overheads)))
p4 = plt.bar(x4, list(map(lambda x: x[3] / (scale * x[5]), overheads)))
p5 = plt.bar(x5, list(map(lambda x: x[4] / (scale * x[5]), overheads)))

# plt.yscale('log')
plt.legend([p1, p2, p3, p4, p5], names)

plt.xticks(x3, overhead_names)
plt.ylabel('Overhead Factor Relative to Virtual Addresses')
plt.tight_layout()

plt.savefig(output)
