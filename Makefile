DOC_DIR=doc
RST_FILES=$(addprefix $(DOC_DIR)/, $(wildcard *.rst) Makefile conf.py)
clean:
	cd jygsaw; rm -f *.class; rm -f *~
	rm -rf build

install:
	jython setup.py install

reinstall:
	make clean
	make install

doc: $(RST_FILES)
	cd doc; make html

