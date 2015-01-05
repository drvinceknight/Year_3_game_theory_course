#!/usr/bin/env

p = plot(2*x-1,x,0,1,legend_label="$u_1(r_1,\sigma_2)$", color='red')
p += plot(1-2*x,x,0,1,legend_label="$u_1(r_2,\sigma_2)$", color='blue')
p.axes_labels(['$y$','$u$'])
p.save("L06-plot01.png")
