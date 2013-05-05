DOC_DIR=doc
PROJ_DIR=jygsaw
RST_FILES=$(wildcard $(DOC_DIR)/*.rst) $(DOC_DIR)/Makefile $(DOC_DIR)/conf.py
PROJ_FILES=$(wildcard $(PROJ_DIR)/*.py)
WEBDIR = jygsaw@tahoe.cs.dartmouth.edu:~/public_html/

clean:
	@- cd jygsaw; rm -f *.class; rm -f *~
	@- rm -rf build

install:
	jython setup.py install
	make clean

doc: $(RST_FILES) $(PROJ_FILES)
	make install
	cd doc; make html

demos: Makefile
	rsync -aPpe ssh ./demos/*.py $(WEBDIR)/code
