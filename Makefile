DOC_DIR=doc
RST_FILES=$(addprefix $(DOC_DIR)/, $(wildcard *.rst) Makefile conf.py)
clean:
	cd jygsaw; rm -f *.class; rm -f *~
	rm -rf build

doc: $(RST_FILES)
	cd doc; make html

