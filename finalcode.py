"""
Author: Mihir Shah 
EEDG 6304 : Computer Architecture Project 1 
Cache Memory Design and Optimization
"""
import os

os.getcwd()
os.chdir("/home/eng/m/mrs150330/m5out")

file=open("stats.txt","r")
data =file.read()

for line in open("/home/eng/m/mrs150330/m5out/stats.txt"):
    if "system.cpu.dcache.overall_miss_rate::total" in line:
        a=line
        #print(a)
    elif "system.cpu.icache.overall_miss_rate::total" in line:
        b=line
        #print(b)
    elif "system.l2.overall_miss_rate::total" in line:
        c=line
        #print(c)
    elif "sim_insts" in line:
        d=line
    elif "system.cpu.dcache.overall_accesses::total" in line:
        e=line
    elif "system.cpu.icache.overall_accesses::total" in line:
        f=line
    elif "system.l2.overall_accesses::total" in line:
        g=line

a=a.split()
print (a)
missrate_dcache=a[1]
print (a[1])

b=b.split()
print (b)
missrate_icache=b[1]
print (b[1])

c=c.split()
print (c)
missrate_l2=c[1]
print (c[1])

d=d.split()
print (d)
sim_insts=d[1]
print (d[1])

e=e.split()
print (e)
accesses_dcache=e[1]
print (e[1])

f=f.split()
print (f)
accesses_icache=f[1]
print (f[1])

g=g.split()
print (g)
accesses_l2cache=g[1]
print (g[1])

m=((4*float(b[1])*int(f[1]))/int(d[1]))

n=(4*float(a[1])*int(e[1]))/int(d[1])

o=(70*float(c[1])*int(g[1]))/int(d[1])


CPI=1+float(m)+float(n)+float(o)
print(CPI)

#Writing the results to data.txt
os.chdir('/home/eng/m/mrs150330/EE6303/Project1_SPEC-master/401.bzip2')

with open("data.txt","a") as file2:
    file2.write(str(CPI))
    file2.write("\n")
    file2.close()

"""
file.write("\n")
file.write(missrate_dcache)
file.write(",") 
file.write(missrate_icache)
file.write(",")
file.write(missrate_l2)
file.write("\n")

file.write("\n")
file.write("--------------------------------------------------------------------------------------------------------------")
file.write("\n")
file.write("missrate_dcache:  ")
file.write(missrate_dcache)
file.write("\n")
file.write("missrate_icache:  ")
file.write(missrate_icache)
file.write("\n")
file.write("missrate_l2:  ")
file.write(missrate_l2)
file.write("\n")
file.write("sim_insts: ")
file.write(sim_insts)
file.write("\n")
file.write("accesses_dcache: ")
file.write(accesses_dcache)
file.write("\n")
file.write("accesses_icache: ")
file.write(accesses_icache)
file.write("\n")
file.write("accesses_l2cache: ")
file.write(accesses_l2cache)
file.write("\n")
file.write("CPI: ")
file.write(str(calculating_CPI))
file.write("\n")
file.write("--------------------------------------------------------------------------------------------------------------")
"""


    
