#!/usr/bin/env

f(a,b)=a^3/3+3/4*b^2+(1-a-b)^2/2
p = contour_plot(f,(0,.5),(0,.5),colorbar=True,axes_labels=["$\\alpha$","$\\beta$"],contours=100, cmap='coolwarm',fill=True)
p.axes_labels(['$\\alpha$','$\\beta$'])
p.save("L18-plot01.png")
