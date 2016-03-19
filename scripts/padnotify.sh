#!/bin/bash

if [ $ACTION = "add" ]; then
    echo "/usr/local/bin/playerpad $DEVNAME > /dev/null 2>&1 " | at now
fi
