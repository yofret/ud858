#!/usr/bin/env python

"""settings.py

Udacity conference server-side Python App Engine app user settings

$Id$

created/forked from conference.py by wesc on 2014 may 24

"""

# dev_appserver.py app.yaml
# gcloud app deploy app.yaml --project pythoncourse-168613 --version 1
# 
# Replace the following lines with client IDs obtained from the APIs
# Console or Cloud Console.
WEB_CLIENT_ID = '950159804578-fv97sh9i29l0jpi889j7td8n1k0n036g.apps.googleusercontent.com'
ANDROID_CLIENT_ID = 'replace with Android client ID'
IOS_CLIENT_ID = 'replace with iOS client ID'
ANDROID_AUDIENCE = WEB_CLIENT_ID
