#!/usr/bin/env

p = plot(7-4*x,x,0,1,legend_label="$xu_1(r_1,s_1)+u_2(r_1,s_2)(1-x)$", color='red')
p += plot(6-x,x,0,1,legend_label="$xu_1(r_2,s_1)+u_2(r_2,s_2)(1-x)$", color='blue')
p.axes_labels(['$x$','$u$'])
p.save("L04-plot04.png")
