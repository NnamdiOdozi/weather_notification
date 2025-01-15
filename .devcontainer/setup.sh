#!/bin/bash
# .devcontainer/setup.sh

# Start docker in docker container
# the image includes all neccessary things to run docker and no sudo needed
docker run -d --privileged --name dind -p 2375:2375 --restart=always docker:dind

# Create a docker context
docker context create dind --docker "host=tcp://localhost:2375"

# Activate the docker context
docker context use dind

# Install jupyter lab and some useful libraries
pip install jupyterlab numpy pandas matplotlib seaborn
# Add auth using a service account - assumes user adds key to secrets
#echo "${GOOGLE_APPLICATION_CREDENTIALS}" > /tmp/key.json  # Commenting out GCloud stuff until i sort out authentication
#export GOOGLE_APPLICATION_CREDENTIALS=/tmp/key.json        # Commenting out GCloud stuff until i sort out authentication
# Clean up key
chmod 400 /tmp/key.json
