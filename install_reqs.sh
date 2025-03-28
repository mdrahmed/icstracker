#!/bin/bash

set -e

# Install core packages quietly
sudo apt-get update > /dev/null
sudo apt-get install -y \
    build-essential \
    python3-dev \
    automake \
    cmake \
    git \
    flex \
    bison \
    libglib2.0-dev \
    libpixman-1-dev \
    python3-setuptools \
    cargo \
    libgtk-3-dev > /dev/null

# Install LLVM/Clang (try version 14 first)
if ! sudo apt-get install -y lld-14 llvm-14 llvm-14-dev clang-14 > /dev/null 2>&1; then
    sudo apt-get install -y lld llvm llvm-dev clang > /dev/null
fi

# Install GCC plugin dev packages
GCC_VERSION=$(gcc --version | head -n1 | awk '{print $NF}' | cut -d. -f1)
sudo apt-get install -y \
    gcc-${GCC_VERSION}-plugin-dev \
    libstdc++-${GCC_VERSION}-dev > /dev/null

# Print final output
echo "Installation complete"
echo ""
echo "Versions:"
llvm-config --version | xargs echo "LLVM:"
clang --version | head -n1 | cut -d' ' -f3- | xargs echo "Clang:"
python3 --version | xargs echo "Python:"
