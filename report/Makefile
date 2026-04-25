# Build the report.
#
#   make pdf       — Markdown -> PDF via Pandoc + Tectonic
#   make docx      — Markdown -> DOCX via Pandoc
#   make figures   — extract PNGs from the executed notebook
#   make all       — figures + pdf + docx
#   make clean     — remove built artifacts

PANDOC := pandoc
PDF_ENGINE := tectonic

SOURCE  := report.md
BIB     := references.bib
CSL     := apa.csl
FIG_DIR := figures

PDF_FLAGS := \
	--pdf-engine=$(PDF_ENGINE) \
	--citeproc \
	--csl=$(CSL) \
	--bibliography=$(BIB) \
	-V geometry:margin=2.5cm \
	-V fontsize=11pt \
	-V linestretch=1.15 \
	-V documentclass=article \
	-V colorlinks=true \
	-V linkcolor=NavyBlue \
	-V urlcolor=NavyBlue \
	-V citecolor=NavyBlue \
	--toc \
	--toc-depth=2 \
	--number-sections

DOCX_FLAGS := \
	--citeproc \
	--csl=$(CSL) \
	--bibliography=$(BIB) \
	--toc \
	--toc-depth=2 \
	--number-sections

.PHONY: all pdf docx figures clean

all: figures pdf docx

pdf: report.pdf

docx: report.docx

figures:
	@python3 extract_figures.py

report.pdf: $(SOURCE) $(BIB) $(CSL)
	$(PANDOC) $(SOURCE) -o $@ $(PDF_FLAGS)

report.docx: $(SOURCE) $(BIB) $(CSL)
	$(PANDOC) $(SOURCE) -o $@ $(DOCX_FLAGS)

clean:
	rm -f report.pdf report.docx
