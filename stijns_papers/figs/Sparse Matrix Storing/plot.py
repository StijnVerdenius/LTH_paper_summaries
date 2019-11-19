

import matplotlib.pyplot as plt
import numpy as np




def naive(m, nz):
    return (32+2+2)*m*m

def dok(m, nz):
    return m*m*2 + 32*(1+nz)

def csr(m, nz):
    return nz*(32+2) +2*(m+1)

ms = [16, 32]
nzs = [x/20 for x in range(20)]

funcs = [naive, dok, csr]

results = {}

for fu in funcs:
    results[fu.__name__] = [[fu(m, round(m*(1-zp))) for m in ms] for zp in nzs]

for i, m in enumerate(ms):
    for fu in funcs:
        nums = [np.log10(x[i]) for x in results[fu.__name__]]
        plt.plot(nzs, nums, label=f"{fu.__name__} on {m}x{m}", linestyle="-"*(i+1))

plt.yticks([2.0, 3.0, 4.0], ["10^2", "10^3", "10^4"])
plt.xticks(nzs , [int(x*100) for x in nzs])
plt.ylabel(" bits to store matrix")
plt.xlabel("Sparcity %")
plt.legend()
plt.show()

