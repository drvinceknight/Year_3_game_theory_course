#!/usr/bin/env

p = plot(3*x,x,0,1,legend_label="$u_1(r_1,\sigma_2)$", color='red')
p += plot(2-x,x,0,1,legend_label="$u_1(r_2, \sigma_2)$", color='blue')
p.axes_labels(['$x$','$u$'])
p.save("L04-plot02.png")
