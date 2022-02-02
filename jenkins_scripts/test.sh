# #!/usr/bin/env sh

# echo $NODE_NAME
# echo $PIPELINE_NODE
# echo $NODE_LABELS
# echo $RESERVE
# echo $PWD
# set -ex

# rand=$(shuf -i 1000000000-9999999999 -n 1)
# pip install pip==20.2.3

# make test

# echo "end....."
# echo "$UNAME"
credentialsId='dockerHub'
docker login -u $user -p $pass

