#!/usr/bin/python
import yaml

"""read the pocket's conf."""

if __name__ == "__main__":
    readconf("conf.yaml")

def readconf(conffile):
    conf = yaml.load(file('conf.yaml'))
    print conf
