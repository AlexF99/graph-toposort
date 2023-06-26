PYTHON = python3
PROGRAM = toposort

all: $(PROGRAM)

$(PROGRAM): main.py
	echo '#!/usr/bin/env $(PYTHON)' > $(PROGRAM)
	cat main.py >> $(PROGRAM)
	chmod +x $(PROGRAM)

turnin:
	tar -zcvf aopf20_lgtg20.tar.gz main.py graph.py makefile relatorio_grafos.pdf *.dot

turninteste:
	tar -zcvf aopf20_lgtg20.tar.gz main.py graph.py makefile *.dot

clean:
	rm -f $(PROGRAM)
