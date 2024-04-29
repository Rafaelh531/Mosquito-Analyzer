#!/bin/sh
# launcher.sh

cd /home/admin/mosquito_project/MosquitoDL
echo "Starting classifier"
python tester.py -m resnet50 -t "mosquitos_lab_test/" -w "resnet50_aug_pt2.pth"
echo "Classified"

echo "Calling mqtt cliente"
cd /home/admin/mosquito_project/cron/mosqcron
node index.js
echo "Sent to server"
