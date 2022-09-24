import sys
import matplotlib
from matplotlib import pyplot as plt
#matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})
#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['font.family'] = "sans-serif"
import os

matplotlib.use("pgf")
plt.figure(num=None, figsize=(4, 1.8), facecolor='w', edgecolor='k')
#matplotlib.rcParams.update({'font.size': 10})
# PLEASE NOTE - all units are converted to their base, ie. ns is in seconds, mW is in Watts

# numbers following are taken in aggregate from Shimin et. al, and the related citations
GB = 1
dram_idle = 100 * (10**-3) * GB  # mW/GB
pcm_idle = 1 * (10**-3) * GB  # mW/GB

# by page
dram_read_time = 20 * (10**-9)  # ns however, could range to 50
pcm_read_time = 50 * (10**-9)  # ns

# by page
dram_write_time = 20 * (10**-9)  # ns however, could range to 50
pcm_write_time = 1000 * (10**-9)
# TODO add NAND if time
# end Shimin et al.

# power = energy/time ie. watt = joule / second

# following from lee. in pJ
dram_read = (1.17 + 0.93) * (10**-12)  # array read + buffer read
dram_write = (0.39 + 1.02) * (10**-12)  # array write + buffer write

# following numbers are from bedeschi, most complete, in pJ for energy, uW for power
# array read (from bedeschi) and buffer read (from lee)
e_pcm_read = (2 + 0.93) * (10**-12)
# array write (from bedeschi) and buffer write (from lee)
e_pcm_set = (45 + 1.02) * (10**-12)
# array reset (from bedeschi) and buffer write (from lee)
e_pcm_reset = (64.8 + 1.02) * (10**-12)

# following numbers in ns - please note, this does not perfectly account for time to do buffer operations, which may slightly skew power usage calculation
t_pcm_read = 48 * (10**-9)  # ns
t_pcm_set = 150 * (10**-9)  # ns
t_pcm_reset = 40 * (10**-9)  # ns

page_size = 64 * 8  # in bits


# ASSUMING 1GB chip, only data being written is data being flipped... this may be too simple an assumption #TODO

# top flips/s based on page write time
max_flips_second = (1/pcm_write_time * page_size)
print(max_flips_second)

p_pcm_list = []
p_dram_list = []

x_pcm = []
x_dram = []

for i in range(0, int(2000000000), 1000000):
    # i is bits flipped
    p_idle_dram = dram_idle
    p_idle_pcm = pcm_idle

    # assuming page size required for DRAM
    # TODO check to ensure this is correct
    if (i % page_size == 0):
        #p_flipped_dram = (int(i/page_size)) * page_size * (dram_write/dram_write_time)
        p_flipped_dram = (int(i/page_size)) * page_size * (dram_write)
    else:
        #p_flipped_dram = (int(i/page_size) + 1) * page_size * (dram_write/dram_write_time)
        p_flipped_dram = (int(i/page_size) + 1) * page_size * (dram_write)

    # assuming bit power for PCM, avg. of set and reset
    #p_flipped_pcm = i * ((e_pcm_set + e_pcm_reset)) / (t_pcm_set + t_pcm_reset)
    p_flipped_pcm = i * (((e_pcm_set + e_pcm_reset) / 2) + e_pcm_read)

    #x_dram.append(i / dram_write_time)
    #x_pcm.append(i / ((t_pcm_set + t_pcm_reset) / 2))

    x_dram.append(i)
    x_pcm.append(i)

    p_dram_list.append(p_idle_dram + p_flipped_dram)
    p_pcm_list.append(p_idle_pcm + p_flipped_pcm)


print("Slope PCM = " + str((e_pcm_set + e_pcm_reset) / 2 + e_pcm_read))
# print(p_pcm_list)
#print((t_pcm_set + t_pcm_reset) / 2)

#fig = plt.figure()

plt.plot(x_dram, p_dram_list, label="DRAM")
plt.plot(x_pcm, p_pcm_list, label="PCM")
plt.legend()


plt.xlabel("Bit Flips per Second")
plt.ylabel("Power (Watts)")

# plt.savefig('flip_throughput.pdf')

plt.tight_layout()
# plt.show()


"""
#pJ/bit , numbers taken from Architecting phase change memory as a scalable dram alternative
lee_pcm_read = 2.47 + 0.93 #array read + buffer read
lee_pcm_write = 16.82 + 1.02 #array write + buffer write
#lee_pcm_idle = 0.08 #this is higher than expected, should be 0...

bedeschi_pcm_read = 2.0 + 0.93 #read from source, buffer from lee
bedeschi_pcm_write = 45 + 1.02 #write from source, buffer from lee, without reset
#bedeschi_pcm_idle = 0 #not from source, just testing with idle.

dram_read = 1.17 + 0.93 #array read + buffer read
dram_write = 0.39 + 1.02 #array write + buffer write
#dram_idle = 0.08 #whole device... not just for the row TODO, find better idle numbers (1W per GB of gigabyte) - timing interval probably comes into effect. 

#one part, power per second, one part how much to flip a bit (energy). Do those add up or do they cover each other... 
#bitts flipped per second (power)

#check idle POWER not energy... TODO 

#2048B-wide buffer per bank


#modeled at 1000 writes per row, 8 Byte rows 
#TODO look at numbers in cited papers table

lee_pcm_e_list = []
bedeschi_pcm_e_list = []
dram_e_list = []
bits_flipped_list = []

row_size = 8 * 8 
bits_flipped = 0
while bits_flipped < 65:
    #assuming a read, followed by a write + idle cost
    dram_energy = 0
    lee_pcm_energy = 0
    bedeschi_pcm_energy = 0
    for i in range(0, 1000):
        #with read: pcm_energy += (lee_pcm_read + lee_pcm_idle) * row_size + (lee_pcm_write * bits_flipped)
        #with read: dram_energy += (dram_read + dram_idle + dram_write) * row_size
        lee_pcm_energy += (lee_pcm_idle) * row_size + (lee_pcm_write * bits_flipped)
        bedeschi_pcm_energy += (bedeschi_pcm_idle) * row_size + (bedeschi_pcm_write * bits_flipped)
        
        dram_energy += (dram_read + dram_idle + dram_write) * row_size
    #print("Bits Flipped: " + str(bits_flipped))
    #print("PCM Energy : " + str(pcm_energy))
    #print("DRAM Energy: " + str(dram_energy))
    lee_pcm_e_list.append(lee_pcm_energy)
    bedeschi_pcm_e_list.append(bedeschi_pcm_energy)
    dram_e_list.append(dram_energy)
    bits_flipped_list.append(bits_flipped)
    bits_flipped += 1
    

#print(pcm_e_list)
#print(dram_e_list)
#print(bits_flipped_list)

#print(len(pcm_e_list))
#print(len(bits_flipped_list))
#plt.axis(bits_flipped_list)
plt.plot(lee_pcm_e_list)
plt.plot(bedeschi_pcm_e_list)
plt.plot(dram_e_list)
plt.show()

"""


output = sys.argv[1]
plt.savefig(output)
