echo running $1
export BBS_PINKY_SCRIPT=$1
export BBS_PROJECT_ID=$2
export BBS_PROJECT_CODE=$3


echo BBS PROJECT ID  : $BBS_PROJECT_ID
echo BBS PROJECT CODE: $BBS_PROJECT_CODE


echo Creating manifest dirs
mkdir -p /data/$BBS_PROJECT_CODE/manifests
mkdir -p /data/$BBS_PROJECT_CODE/manifests/discovery
mkdir -p /data/$BBS_PROJECT_CODE/manifests/hostdiscovery
mkdir -p /data/$BBS_PROJECT_CODE/manifests/wordlists
mkdir -p /data/$BBS_PROJECT_CODE/manifests/attack
mkdir -p /data/$BBS_PROJECT_CODE/manifests/osintel

echo Creating manifest yaml from template
export GENERATED_MANIFEST_FILE=`echo $BBS_PINKY_SCRIPT | sed -e "s/.template//" -e "s///"`
export FULL_MANIFEST_PATH="/data/$BBS_PROJECT_CODE/manifests/$GENERATED_MANIFEST_FILE"

echo full manifest file path is $FULL_MANIFEST_PATH

cp /pinky/templates/$BBS_PINKY_SCRIPT $FULL_MANIFEST_PATH

echo Building manifests
sed -i "s/TASK_NAME/${BBS_PROJECT_CODE}/g" $FULL_MANIFEST_PATH
sed -i "s/BBS_PROJECT_ID/${BBS_PROJECT_ID}/g" $FULL_MANIFEST_PATH
sed -i "s/BBS_PROJECT_CODE/${BBS_PROJECT_CODE}/g" $FULL_MANIFEST_PATH


echo Removing any previous jobs...
kubectl delete -f $FULL_MANIFEST_PATH

echo Running new job...
kubectl create -f $FULL_MANIFEST_PATH

echo All done son.
