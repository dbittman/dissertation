
all:
	@mkdir -p build
	@mkdir -p build/FrontBackmatter
	@mkdir -p build/Chapters
	@latexmk -cd $(FLAGS) $(SOURCES) -deps-out=build/DEPS.mk

FLAGS=-xelatex -outdir=../build -use-make -halt-on-error -quiet

SOURCES=book/dbittman-dissertation.tex

-include build/DEPS.mk

clean:
	rm -r build