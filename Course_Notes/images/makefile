tex  = $(wildcard *.tex)
pdfs = $(tex:%.tex=%.pdf)

all: $(pdfs)

%.pdf: %.tex
	pdflatex $<

clean:
	rm *.aux
	rm *.log
