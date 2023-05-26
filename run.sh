#!/bin/bash
conda run -n webchat nohup python app.py >/dev/null 2>&1 &

