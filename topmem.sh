#!/bin/bash
echo %MEM   PID COMMAND
ps -eo pmem,pid,args | sort -k1rn | head -n 10

