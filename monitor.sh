#!/bin/bash
while :
do
ps -ef | grep python | grep app | grep -v grep
if [ $? -ne 0 ]
then 
	sh /opt/webchat/run.sh
fi
sleep 3
done

