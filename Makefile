DOC_DIR=doc
PROJ_DIR=jygsaw
RST_FILES=$(wildcard $(DOC_DIR)/*.rst) $(DOC_DIR)/Makefile $(DOC_DIR)/conf.py
PROJ_FILES=$(wildcard $(PROJ_DIR)/*.py)
clean:
	@- cd jygsaw; rm -f *.class; rm -f *~
	@- rm -rf build

install:
	jython setup.py install
	make clean

doc: $(RST_FILES) $(PROJ_FILES)
	make install
	cd doc; make html
