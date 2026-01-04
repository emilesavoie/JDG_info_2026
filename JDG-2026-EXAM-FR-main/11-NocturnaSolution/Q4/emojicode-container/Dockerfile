FROM ubuntu:18.04

# Install prerequisites
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    g++ \
    clang \
    && rm -rf /var/lib/apt/lists/*

# Download and install Emojicode
WORKDIR /tmp
RUN curl -o emojicode.tar.gz -L https://github.com/emojicode/emojicode/releases/download/v1.0-beta.2/Emojicode-1.0-beta.2-Linux-x86_64.tar.gz \
    && tar -xzf emojicode.tar.gz \
    && cd Emojicode-1.0-beta.2-Linux-x86_64 \
    && find . -type f -executable -name "emoji*" -exec cp {} /usr/local/bin/ \; \
    && find . -name "*.so*" -exec cp {} /usr/local/lib/ \; \
    && find . -name "*.h" -o -name "*.hpp" | xargs -I {} cp --parents {} /usr/local/ 2>/dev/null || true \
    && mkdir -p /usr/local/EmojicodePackages \
    && if [ -d "packages" ]; then cp -r packages/* /usr/local/EmojicodePackages/; fi \
    && ldconfig \
    && cd .. \
    && rm -rf Emojicode-1.0-beta.2-Linux-x86_64 emojicode.tar.gz

# Set working directory for user files
WORKDIR /workspace

# Set C++ compiler environment variable
ENV CXX=g++

CMD ["/bin/bash"]
