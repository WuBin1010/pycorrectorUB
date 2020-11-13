#!/usr/bin/env python3
# coding: utf-8

##########
# Desc: Test baidu API for text correction.
# Author: WuBin
# Date: 2020.9.21

from baidu.aip import AipNlp


# Get Baidu API client.
def get_baidu_api_client():
    app_id = '******'
    api_key = '******'
    secret_key = '******'

    client = AipNlp(app_id, api_key, secret_key)
    print(">>> get API client.")

    return client


# Test Baidu API by SDK.
def test_baidu_api_corrector(_client):
    print(">>> test corrector API:")
    # text = "测试百度的文本纠错接口是否OK，比如则些错误，是否能够使别？四别的效果一般。"  # 百度API无法纠错？
    # text = "测思白度的文本纠错接口是否OK，比如则些错误，是否能够使别？"
    text = "硫酸粘杆菌素和浸提液的使用，纯华技术和进化工序。"  # result: >>> ori_frag: 华技术 , correct_frag: 化技术

    # Use baidu corrector API:
    result = _client.ecnet(text)
    print(">>> get result:" + str(result))

    item = result["item"]
    frag_list = item["vec_fragment"]
    count = len(frag_list)
    print(">>> corrector result count:" + str(count))
    for i in range(count):
        frag = frag_list[i]
        ori_frag = frag["ori_frag"]
        correct_frag = frag["correct_frag"]
        print(">>> ori_frag: %s , correct_frag: %s" % (ori_frag, correct_frag))


# main method.
if __name__ == '__main__':
    print(">>> start.")
    get_client = get_baidu_api_client()
    test_baidu_api_corrector(get_client)
