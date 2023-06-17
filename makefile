PYTHON = python3
PROGRAM = toposort

all: $(PROGRAM)

$(PROGRAM): main.py
	echo '#!/usr/bin/env $(PYTHON)' > $(PROGRAM)
	cat main.py >> $(PROGRAM)
	chmod +x $(PROGRAM)

clean:
	rm -f $(PROGRAM)
