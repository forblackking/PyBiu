#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:Hieda no Chiaki <i@wind.moe>

import configparser
import getopt
import os
import sys
import hashlib
from src.init import usage
from src.id3 import getID3
from src.md5 import str_md5, file_md5
from src.sign import sign, uid
from src.post import post, post_biu, confirm

if len(sys.argv) == 1:
    """检察上传环境"""
    print("Checking System Environments...")
    try:
        import requests
    except:
        print('Please install requests. [pip install requests]')
        exit(1)
        # raise xxxException("Please install xxxx")

    try:
        print("Connect to Biu.moe...")
        r = requests.get('http://biu.moe', timeout=3)
        print("Success.")
    except:
        print("Fail. Please check your internet connection.")
        exit(1)


else:
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvf:", ["update"])
    except getopt.GetoptError:
        sys.exit()

    for argv, value in opts:
        if argv in "-f":
            file = value
            # file = "\""+file+"\""
            if not os.path.exists(file):
                # print(os.path.abspath(os.path.join(os.path.dirname(__file__))))
                # file = os.path.join(os.path.abspath(os.path.dirname(__file__)),os.path.dirname(__file__),files)
                # if file[0] == '\\':
                file = os.path.split(os.path.realpath(__file__))[0] + file
                print(file)
                # else:
                #     file = os.path.split(os.path.realpath(__file__))[0]+'\\'+file
                # print("File Path:" + file)
                if not os.path.exists(file):
                    print("找不到文件.请尝试用双引号将文件绝对路径包括起来.")
                else:
                    flag, token = post_biu(file)
                    sys.exit() if not flag else print("lol")
                    pass
            else:
                file = "\"" + file + "\""
                flag, token = post_biu(file)
                if not flag:
                    sys.exit()
                else:
                    confirm(file,file_md5(file), token)
                pass
                # sys.exit() if not post_biu(file) else True
                # pass

        elif argv in "-v":
            config = configparser.ConfigParser()
            config.read_file(open('./.env'))
            version = config.get("Environment", "VERSION")
            print(version)
        elif argv in "-h":
            usage()
            sys.exit()
        else:
            pass

    for argv in args:
        if argv in "update":
            print("update")
        elif argv in "test":
            print("test.")
        else:
            pass



# elif len(sys.argv) == 2:
#     argv = sys.argv[1]
#     if argv == "-v":
#         print("version alpha 0.1")
#     elif argv == "-h":
#         usage()
#     else:
#         pass









# if __name__ == "__main__":