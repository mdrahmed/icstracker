### Library/pass
`instrument_pass.cpp`  is the shared library, that will instrument code.

We need to have `clang` to compile this code, just run following,
```
make
```

### According to Arch
```
instrument.so # for x86-64 
instrument_arm32.so  # for arm32, this is the file we used as our testbed(fischertechnik) was arm-32 bit.
instrument_arm64.so  # for arm64
```
