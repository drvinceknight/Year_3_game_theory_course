#!/usr/bin/env

p = plot(1-2*x,x,0,1,legend_label="$u_2(\sigma_1,s_1)$", color='red')
p += plot(2*x-1,x,0,1,legend_label="$u_2(\sigma_1,s_2)$", color='blue')
p.axes_labels(['$y$','$u$'])
p.save("L06-plot02.png")
