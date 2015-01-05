sage  = $(wildcard *.sage)
pngs = $(sage:%.sage=%.png)

all: $(pngs)

%.png: %.sage
	sage $<


clean:
	rm *.py
