Usage of all the programs and files have been mentioned below for the reference.

main.py:
* Initiates xapp api, sends subscription request to Subscription Mgr
* Upon timer event expiry of every 1 minute triggers PRB_PRED_REQ towards prbpred xApp
* once PRB_PRED_RESP is received, it allocates PRB based on the predicted PRB utilisation and sends policy update to RAN

Note: Need to implement the code for sending policy update to RAN


How to build prbpred xApp
docker build -t prbpredxapp:3.0 -f  Dockerfile .
docker run -d --net=host -e USE_FAKE_SDL=1 prbpredxapp:3.0
docker tag alloc:3.0 nexus3.o-ran-sc.org:10002/o-ran-sc/ric-app-prbpredxapp:0.0.2

How to onboard xApp in RIC platform
cd xapp-descriptor
dms_cli onboard --config_file_path=config.json --shcema_file_path=/root/appmgr/xapp_orchestrater/dev/docs/xapp_onboarder/guide/embedded-schema.json
dms_cli install --xapp_chart_name=prbpred --version=0.0.2 --namespace=ricxapp

Uninstall xApp
dms_cli uninstall prbpred ricxapp
