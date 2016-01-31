#!/usr/bin/env

p = plot(1+3*x,x,0,1,legend_label="$u_2(\sigma_1,c_1)$", color='red')
p += plot(3-x,x,0,1,legend_label="$u_2(\sigma_1,c_2)$", color='blue')
p += plot(2*x-1,x,0,1,legend_label="$u_2(\sigma_1,c_3)$", color='green')
p.axes_labels(['$x$','$u$'])
p.save("L04-plot03.png")
