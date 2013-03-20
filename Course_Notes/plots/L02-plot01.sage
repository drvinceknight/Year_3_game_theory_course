#!/usr/bin/env

p = plot(1-2*x,x,0,1,legend_label="$u_1$ assuming P2 plays tails", color='red')
p += plot(2*x-1,x,0,1,legend_label="$u_2$ assuming P1 plays tails", color='blue')
p.axes_labels(['$x$','$u$'])
p.save("L02-plot01.png")
