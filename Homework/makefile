md = $(wildcard *.md)
htmls = $(md:%.md=%.html)

all: $(htmls)

%.html: %.md
	./pandocipy_given_file.py $<
	../Scripts/generate_website.py
