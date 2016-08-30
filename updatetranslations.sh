#!/usr/bin/env bash
cd djangocms_maps
django-admin.py makemessages -l en
tx push -s -l en
tx pull -f -a
django-admin.py compilemessages
