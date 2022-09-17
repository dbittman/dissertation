
SCRIPTS := $(shell find book/scripts -name '*.py')
GENPDFS := $(addprefix book/genfig/,$(notdir $(SCRIPTS:.py=.pdf))) book/genfig/obj_graph.pdf


all: $(GENPDFS)
	@mkdir -p build
	@mkdir -p build/FrontBackmatter
	@mkdir -p build/Chapters
	@latexmk -cd $(FLAGS) $(SOURCES) -deps-out=build/DEPS.mk
	@pplatex -i build/dbittman-dissertation.log -b

FLAGS=-lualatex -shell-escape -latexoption="-shell-escape" -outdir=../build -halt-on-error -quiet

SOURCES=book/dbittman-dissertation.tex

book/genfig/fotoverhead.pdf: book/scripts/fotoverhead.py gendata/fotoverhead-out matplotlibrc
	python book/scripts/fotoverhead.py $@ gendata/fotoverhead-out

book/genfig/%.pdf: book/scripts/%.py matplotlibrc
	mkdir -p book/genfig
	python $< $@

book/genfig/%.pdf: book/scripts/%.dot
	mkdir -p book/genfig
	dot -Tpdf -o $@ $<

-include build/DEPS.mk

clean:
	-rm -r build book/genfig

include src/include.mk