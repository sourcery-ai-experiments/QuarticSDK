# #!/usr/bin/env sh

# echo $NODE_NAME
# echo $PIPELINE_NODE
# echo $NODE_LABELS
# echo $RESERVE
# echo $PWD
# set -ex
# echo "$BRANCH_NAME"

# export PUBLISH_PYPI=true
# export GITHUB_TOKEN="$GIT_TOKEN"

# pip install -r requirements.txt

docker login -u $DOCKER_USER -p $DOCKER_PASS
docker build -t quarticai/quarticsdk:base -f Dockerfile_base .
docker push quarticai/quarticsdk:base
