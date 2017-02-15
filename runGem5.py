# -- an example to run SPEC 429.mcf on gem5, put it under 429.mcf folder --

import os

data="time $GEM5_DIR/build/X86/gem5.opt -d ~/m5out $GEM5_DIR/configs/example/se.py -c $BENCHMARK -o \"$ARGUMENT $ARGUMENT2\" -I 100000000 --caches --l2cache"
data1=" --l1i_assoc="
data2=" --l1d_assoc="
data3=" --l2_assoc="
data4=" --cacheline_size="
data5=" --l1d_size="
data6=" --l1i_size="
data7=" --l2_size="
data8=" --cpu-type="

a=["1","2","4","8"] # L1 Asso
c=["2","4","8"] # L2 Asso
d=["32","64","128"] # cacheline_size
e=["timing","detailed","atomic","minor"] # CPU Model Type
x=['64','128'] # L1d Size
y=['128','64'] # L1i Size
z=['1'] #L2 Size


for i in range(0,3): # a
    for j in range(0,2): # x
        for p in range(0,2): #y            
            for k in range(0,3): #c
                for l in range(0,3): #d
                    for v in range(0,3): # e
                        with open('data.txt','a') as file:
                            with open('runGem5.sh','w') as file1:
                                g=data+data1+a[i]+data2+a[i]+data3+c[k]+data4+d[l]+data5+x[j]+"kB"+data6+y[p]+"kB"+data7+z[0]+"MB"+data8+e[v]
                                print(g)
                                file1.write("\n\n")
                                file1.write("export GEM5_DIR=/usr/local/gem5") 
                                file1.write("\n")                        
                                file1.write("export BENCHMARK=./src/benchmark") 
                                file1.write("\n")
                                file1.write("export ARGUMENT=./data/input.program")
                                file1.write("\n")
                                file1.write("export ARGUMENT2=10")
                                file1.write("\n")
                                file1.write(g)
                                file1.write("\n")
                                file1.close()
                                os.system("python exe.py")
                                file.write("\n")
                                file.write(a[i])
                                file.write(",")
                                file.write(a[i])
                                file.write(",")
                                file.write(c[k])
                                file.write(",")
                                file.write(d[l])
                                file.write(",")
                                file.write(x[j])
                                file.write(",")
                                file.write(y[p])
                                file.write(",")
                                file.write(z[0])
                                file.write(",")
                                file.write(e[v])
                                file.write(",")
                                #file.write(g)
                                file.close()
                                os.system("python finalcode.py")



