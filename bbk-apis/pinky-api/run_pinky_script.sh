echo running $1
export BBS_PINKY_SCRIPT=$1
export BBS_PROJECT_ID=$2
export BBS_PROJECT_CODE=$3
export BBS_INPUT_LIST=$4

echo BBS PROJECT ID  : $BBS_PROJECT_ID
echo BBS PROJECT CODE: $BBS_PROJECT_CODE
echo             LIST: $BBS_INPUT_LIST


echo Creating manifest dirs
mkdir -p /bbk-app/project-data/$BBS_PROJECT_CODE/manifests/scanner/urlscan/
mkdir -p /bbk-app/project-data/$BBS_PROJECT_CODE/manifests/scanner/domainscan/


echo Creating manifest yaml from template
export GENERATED_MANIFEST_FILE=`echo $BBS_PINKY_SCRIPT | sed -e "s/.template//" -e "s///"`
export FULL_MANIFEST_PATH="/bbk-app/project-data/$BBS_PROJECT_CODE/manifests/$GENERATED_MANIFEST_FILE"

echo full manifest file path is $FULL_MANIFEST_PATH

echo copying manifest template
cp /bbk-app/process-manifests/$BBS_PINKY_SCRIPT $FULL_MANIFEST_PATH

echo Building manifests
sed -i "s/TASK_NAME/${BBS_PROJECT_CODE}/g" $FULL_MANIFEST_PATH
sed -i "s/BBS_PROJECT_ID/${BBS_PROJECT_ID}/g" $FULL_MANIFEST_PATH
sed -i "s/BBS_PROJECT_CODE/${BBS_PROJECT_CODE}/g" $FULL_MANIFEST_PATH
sed -i "s/BBS_INPUT_LIST/${BBS_INPUT_LIST}/g" $FULL_MANIFEST_PATH




echo Removing any previous jobs...
kubectl delete -f $FULL_MANIFEST_PATH

echo Running new job...
kubectl create -f $FULL_MANIFEST_PATH

echo All done son.
