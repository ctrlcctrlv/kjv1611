.PHONY: all
all:
	./build.sh

.PHONY: info
info:
	cd info && ./gen.sh
