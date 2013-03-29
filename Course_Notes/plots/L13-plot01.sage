#!/usr/bin/env

p = plot(x^2,x,0,1.5,legend_label="$u(x)=\sqrt{x}$ (Risk-averse)", color='red', thickness=3)
p += plot(x,x,0,1.5,legend_label="$u(x)=x$ (Risk-neutral)", color='green', thickness=3)
p += plot(x^3,x,0,1.5,legend_label="$u(x)=x^3$ (Risk-seeking)", color='blue', thickness=3)
p.axes_labels(['$x$','$u$'])
p.save("L13-plot01.png")
