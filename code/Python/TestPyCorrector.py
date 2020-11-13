#!/usr/bin/env python3
# coding: utf-8

##########
# Desc: Test pycorrector for text correction.
# Author: WuBin
# Date: 2020.9.23

import pycorrector


def correct_sentence(_sentence):
    corrected_sent, detail = pycorrector.correct(_sentence)
    print(">>> corrected_sent:", corrected_sent)
    print(">>> detail:", detail)

    idx_errors = pycorrector.detect(_sentence)
    print(">>> index of errors:", idx_errors)


# main method.
if __name__ == '__main__':
    print(">>> start.")
    # sentence = '少先队员因该为老人让坐'
    # sentence = "硫酸粘杆菌素和浸提液的使用，纯华技术和进化工序。"
    sentence = "我的喉咙发炎了要买点阿莫细林吃"
    sentence = "配副眼睛,高梁"
    sentence = "元材料价格较高的风险"
    correct_sentence(sentence)

