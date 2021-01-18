from py_mentat import *
import math

def make_nodes(n, data):
    for (z1, z2, t1, t2, r1, r2) in data[:len(data)-1]:
        z_list = [(z2 - z1) / n[2] * i + z1 for i in range(n[2])]
        t_list = [(t2 - t1) / n[2] * i + t1 for i in range(n[2])]
        r_list = [(r2 - r1) / n[2] * i + r1 for i in range(n[2])]
        
        for k in range(len(z_list)):
            zz = z_list[k]
            rr = r_list[k]
            tt = t_list[k]
            dr_list = [(rr - tt) + tt / n[0] * i for i in range(n[0]+1)]
            
            rad_list = [2 * math.pi / n[1] * i for i in range(n[1])]
            
            for dr in dr_list:
                for rad in rad_list:
                    x = dr * math.cos(rad)
                    y = dr * math.sin(rad)
                    str = "*add_nodes %f %f %f" % (x, y, zz)
                    py_send(str)
            
    (z1, z2, t1, t2, r1, r2) = data[-1]

    z_list = [(z2 - z1) / n[2] * i + z1 for i in range(n[2]+1)]
        
    t_list = [(t2 - t1) / n[2] * i + t1 for i in range(n[2]+1)]
    r_list = [(r2 - r1) / n[2] * i + r1 for i in range(n[2]+1)]
        
    for k in range(len(z_list)):
        zz = z_list[k]
            
        rr = r_list[k]
        tt = t_list[k]
        dr_list = [(rr - tt) + tt / n[0] * i for i in range(n[0]+1)]
            
        rad_list = [2 * math.pi / n[1] * i for i in range(n[1])]
            
        for dr in dr_list:
            for rad in rad_list:
                x = dr * math.cos(rad)
                y = dr * math.sin(rad)
                str = "*add_nodes %f %f %f" % (x, y, zz)
                py_send(str)
    return

def make_elements(n, n_blocks):
    num_z = n[2]
    num_r = n[0]
    num_theta = n[1]
    num_layer = (num_r + 1) * num_theta

    py_send('*set_element_class hex8')
    for k in range(num_z * n_blocks):
        for j in range(num_r):
            for i in range(num_theta):
                if i == num_theta - 1:
                    o = (num_layer * k) + num_theta * j + i + 1
                    e = [o, o+num_theta, o+1, o-num_theta+1, o+num_layer, o+num_layer+num_theta, o+num_layer+1, o+num_layer-num_theta+1]
                else:
                    o = (num_layer * k) + num_theta * j + i + 1
                    e = [o, o+num_theta, o+num_theta+1, o+1, o+num_layer, o+num_layer+num_theta, o+num_layer+num_theta+1, o+num_layer+1]

                str = "*add_elements %d %d %d %d %d %d %d %d" % (e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7])
                py_send(str)
    return

def main():
    z = [0, 5000, 10000, 15000]
    t = [270, 260, 250, 240]
    r = [1900, 1850, 1800, 1750]
    n = [3, 12, 10]

    z1 = z[0:len(z)-1]
    z2 = z[1:len(z)]
    t1 = t[0:len(t)-1]
    t2 = t[1:len(t)]
    r1 = r[0:len(r)-1]
    r2 = r[1:len(r)]

    data = []
    for i in range(0, len(z1)):
        data.append([z1[i], z2[i], t1[i], t2[i], r1[i], r2[i]])
    
    make_nodes(n, data)

    n_blocks = len(z) - 1
    make_elements(n, n_blocks)

    return
