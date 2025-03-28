CXXFLAGS=-O3 -funroll-loops -Wall -D_FORTIFY_SOURCE=2 -g -Wno-pointer-sign -DVERSION=1  -Wno-variadic-macros
CLANG_CFL=$(shell llvm-config-14 --cxxflags) -Wl,-znodelete -fno-rtti -fpic $(CXXFLAGS)
CLANG_LFL=$(shell llvm-config-14 --ldflags --libs)


CLANG=clang++-14
PASS=instrument.so
PASS_ARM64=instrument_arm64.so
PASS_ARM32=instrument_arm32.so
PASS_SRC=instrument_pass.cpp ## topic, function names, arguments, values, callInsts, callInsts values, global variable values are logged

Objects=$(EXE) $(PASS) $(PASS_ARM64) $(PASS_ARM32)

all: $(PASS) $(PASS_ARM64) $(EXE) $(PASS_ARM32)
	

$(PASS): $(PASS_SRC)
	$(CLANG) $(CLANG_CFL) -g -shared $< -o $@

$(PASS_ARM64): $(PASS_SRC)
	$(CLANG) --target=aarch64-linux-gnu $(CLANG_CFL) -g -shared $< -o $@

$(PASS_ARM32): $(PASS_SRC)
	$(CLANG) --target=arm-linux-gnueabihf $(CLANG_CFL) -g -shared $< -o $@

$(EXE): $(CPP_file) 
	$(CLANG) -o $@ -lpaho-mqttpp3  -lpaho-mqtt3c -lpaho-mqtt3a -lmosquitto -fno-discard-value-names -flegacy-pass-manager -g -Xclang -load -Xclang ./instrument.so $<




.PHONY: clean
clean:
	rm $(Objects)
