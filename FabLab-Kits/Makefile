# this is CW's personal installation on macOS... if you have Inkscape in the $PATH, run "make INKSCAPE=inkscape"
INKSCAPE = /Applications/Programme/Graphik/Inkscape.app/Contents/Resources/bin/inkscape

MODE ?= label

all: \
	out/labels-fidget-spinner.pdf \
	out/labels-bristlebot-1c.pdf \
	out/labels-bristlebot-2c.pdf \
	out/labels-get-in-line.pdf \
	out/labels-gartenlaterne-u.pdf \
	out/labels-gartenlaterne-l.pdf \
	out/labels-senso.pdf \
	out/labels-3x5-led-matrix.pdf \
	out/labels-2prices-8x8-led-matrix.pdf \

out/labels-%.svg: %.patch
	patch -i $*.patch -o $@ labels.svg

out/labels-2prices-%.svg: %.patch
	patch -i $*.patch -o $@ labels_2prices.svg

out/labels%.pdf: out/labels%.svg
	"$(INKSCAPE)" "$(abspath $<)" --export-pdf="$(abspath $@)"

clean:
	rm -fv out/labels*.svg out/labels*.pdf

.PHONY: all clean

.PRECIOUS: out/labels%.svg
