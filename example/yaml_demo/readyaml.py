#!/usr/bin/env python3
import yaml
import requests

with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

        for section in cfg:
            if section == 'mysql':
                print("this is mysql region.")
                print("the host: %s; pwd: %s " % (cfg[section]['host'], cfg[section]['passwd']))
            elif section == 'other':
                print("this is other region.")
        else:
            print('----------------------')
        print("mysql\n:" + str(cfg['mysql']))
        print("other\n:" + str(cfg['other']))
