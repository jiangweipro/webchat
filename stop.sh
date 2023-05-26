#!/bin/bash

ps -ef | grep app | grep python | grep -v grep | xargs kill -9

