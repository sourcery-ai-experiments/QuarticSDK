#!/usr/bin/env sh

echo $NODE_NAME
echo $PIPELINE_NODE
echo $NODE_LABELS
echo $RESERVE
echo $PWD
set -ex
echo "$BRANCH_NAME"


# Obfuscate all branches.
# make obfuscate command creates a new directory deming-core-obfuscated with obfuscated code.
# To disable obfuscation comment the make obfuscate and cd ../deming-core-obfuscated statements
git clone https://$GIT_USER:$GIT_TOKEN@github.com/Quarticai/quartic-licenses.git
pip install pyarmor==6.2.8
pyarmor register quartic-licenses/pyarmor-regfile-1.zip
pip install pip==20.2.3
pip install -r requirements.txt
make obfuscate
rm -rf quartic-licenses
make build

NAME=quartic_sdk
VERSION=$(awk '$1 == "__version__" {print $NF}' ./quartic_sdk/_version.py | sed "s/'//g")
OS=none
CPU_ARCH=any

WHEEL_FILENAME="$NAME-$VERSION-py3-$OS-$CPU_ARCH.whl"
CODE=$(curl -sS -w '%{http_code}' -F package="@dist/$WHEEL_FILENAME" -o output.txt "https://$GEMFURY_AUTH_TOKEN@push.fury.io/quartic-ai/")
cat output.txt && rm -rf output.txt
if [[ "$CODE" =~ ^2 ]]; then
    echo "$WHEEL_FILENAME Package published successfully"
else
    echo "ERROR: server returned HTTP code $CODE"
    exit 1
fi
