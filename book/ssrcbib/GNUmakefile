# This Makefile is designed to generate a listing of the csrg bibliography.
#
# Version: $Id$
#
# Instructions:
#
# * To build a PS version of the bibliography, use
#   make
#   The result will be in csrgbib.ps
# * To build a PDF version of the bibliography, use
#   make pdf
#   The result will be in csrgbib.pdf
# * To build an HTML version of the bibliography, use
#   make html
#   The result will be in csrglong.html
# * To build an HTML version of the bibliography and install it into
#   the paper archive, use
#   make index
# * To remove all "temporary" files, use
#   make clean
# * To remove all derived files (including PS, PDF, and HTML that can
#   be rebuilt), use
#   make spotless

PAPERDIR =	/mirror/ssrc/PaperArchive
DERIVED =	csrgbib.ps csrgbib.pdf csrglong.html csrgshort.html
LATEXFILTER =	./latexc2html.pl
POSTPROC = ./posthtmltag.awk

all:	html

ps: csrgbib.ps

pdf: csrgbib.pdf

csrgbib.ps: csrgbib.dvi
	dvips csrgbib -o

csrgbib.pdf: csrgbib.dvi
	dvipdf csrgbib.dvi

csrgbib.dvi: csrgbib.tex csrg.bib abstract.bst
	latex csrgbib
	bibtex csrgbib
	latex csrgbib
	latex csrgbib

# These rules build HTML versions of the bibliography.
htmltag: csrglongtag.html

csrglongtag.html: csrghtmlt.tex csrg.bib html-long-tag.bst
	$(RM) csrghtmlt.bbl csrghtmlt.blg 
	latex csrghtmlt
	bibtex csrghtmlt
	$(LATEXFILTER) < csrghtmlt.bbl | $(POSTPROC) > csrglongtag.html

html: csrglong.html

csrglong.html: csrghtml.tex csrg.bib html-long.bst
	$(RM) csrghtml.bbl csrghtml.blg csrgbib.html
	latex csrghtml
	bibtex csrghtml
	$(LATEXFILTER) < csrghtml.bbl > csrglong.html

htmlshort: csrgshort.html

csrgshort.html: csrghtmls.tex csrg.bib html-short.bst
	$(RM) csrghtmls.bbl csrghtmls.blg csrgshort.html
	latex csrghtmls
	bibtex csrghtmls
	$(LATEXFILTER) < csrghtmls.bbl > csrgshort.html

csrgyear.html: csrghtmly.tex csrg.bib html-long-year.bst
	$(RM) csrghtmly.bbl csrghtmly.blg csrgyear.html
	latex csrghtmly
	bibtex csrghtmly
	$(LATEXFILTER) < csrghtmly.bbl > csrgyear.html

# Do a "make index" to rebuild the HTML index and place it into the
# paper archive directory.
index: csrglong.html
	$(RM) $(PAPERDIR)/index.html
	cp csrglong.html $(PAPERDIR)/index.html
	chmod 644 $(PAPERDIR)/index.html

# These rules are for cleaning up the directory.

clean:
	$(RM) *.aux *.bbl *.blg *.dvi *.log *~

spotless: clean
	$(RM) $(DERIVED)
