#!/bin/sh
COUNTER=0
while read apps_list
do 
	gplaycli -d $apps_list
    	mv $apps_list.apk /home/budi/adblocker_project/apps_list/test
	let COUNTER=COUNTER+1
	sleep 10

done < add_list.txt
