#!/usr/bin/env python3
# coding: utf-8

##########
# Desc: Read txt files.
# Author: WuBin
# Date: 2020.9.21

import os


# Read all txt files in the path.
def read_all_files(_path, _encoding):
    files = os.listdir(_path)
    text_list = []
    for file in files:
        file_name = _path + '\\' + file
        print(">>> file name:" + file_name)
        if os.path.isdir(file_name) is False:
            with open(file_name, "r", encoding=_encoding) as f:
                data = f.read()
                text_dict = {file_name: data}
                text_list.append(text_dict)

    return text_list


# main method.
if __name__ == '__main__':
    print(">>> start.")
    path = "D:\\corrector\\data\\prospectus"
    # encoding = "gbk"
    encoding = "utf-8"
    get_text_list = read_all_files(path, encoding)
