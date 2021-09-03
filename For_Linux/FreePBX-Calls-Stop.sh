#!/bin/bash
#######################################
#Script FreePBX0 Stop
#######################################
# by kal1gh0st

kill $(ps aux | grep -v grep | grep "/opt/Python-FreePBX/automate.py" | awk '{print $2}')
#questo script dovra essere schedulato nel cron, ha l'utilità di cercare il processo appeaso e killarlo basandosi sul path

