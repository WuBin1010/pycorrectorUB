#!/usr/bin/env python3
# coding: utf-8

##########
# Desc: Util method for all python.
# Author: WuBin
# Date: 2020.9.21

# cut text by block size.
def cut_text(_text, _block_size):
    return [_text[i:i + _block_size] for i in range(0, len(_text), _block_size)]


# cut text by 。
def cut_text_stop(_text):
    return _text.split("。")


# main method.
if __name__ == '__main__':
    print(">>> start.")
    test_text = "明书不存在虚假记载、误导性陈述或重大遗漏，并对其真实性、准确性、完整性承担个别和连带的法律责任。公司负责人和主管会计工作的负责人、会计机构负责人保证招股说明书中财务会计资料真实、完整。发行人及全体董事、监事、高级管理人员、发行人的控股股东、实际控制人以及保荐人、承销的证券公司承诺因发行人招股说明书及其他信息披露资料有虚假记载、"
    print(cut_text_stop(test_text))
