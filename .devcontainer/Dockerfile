# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Install necessary packages including docker
RUN apt-get update && \
    apt-get install -y \
    curl \
    gnupg \
    ca-certificates \
    docker.io && \
    # Install Google Cloud SDK
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    echo "deb http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    apt-get update -y && \
    apt-get install -y google-cloud-sdk && \
    #Clean up
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Add current user to docker group to run docker cli commands
RUN groupadd -g 999 docker && usermod -aG docker vscode

USER vscode
