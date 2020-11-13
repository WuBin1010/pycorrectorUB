#!/usr/bin/env python3
# coding: utf-8

##########
# Desc: Test baidu API for text correction.
# Author: WuBin
# Date: 2020.9.25

import jieba
import jieba.posseg as pos


# get segment words list.
def segment_words(text):
    word_list = jieba.lcut(text)
    return word_list


# get pos list of words.
def segment_pos_words(text):
    get_pos_list = pos.cut(text)
    return get_pos_list


# text include person name or other special name.
def include_special_pos(text):
    # special_pos = ["nr", "ns", "nt", "nz"]
    special_pos = ["nr"]
    _include_person_name = False
    _pos_list = segment_pos_words(text)
    for _pos in _pos_list:
        get_pos = str(_pos.flag)
        if get_pos in special_pos:
            _include_person_name = True
    return _include_person_name


# text include company or not.
def include_company(text):
    _include_company = False
    company_word_list = ["公司", "企业", "集团"]
    for company_word in company_word_list:
        # if text.endswith(company_word):
        if company_word in text:
            _include_company = True
            break
    return _include_company

# main method.
if __name__ == '__main__':
    print(">>> start.")
    test_text = "保荐机构（主承销商）：安信证券股份有限公司,法定代表人,王连志,住所,深圳市福田区金田路4018号安联大厦35层、28层A02单元"  # 金田路 也被判别为人名nr
    test_text = "沈思"
    '''
    pos_list = segment_pos_words(test_text)
    for pos_str in pos_list:
        print(pos_str)
        print(">>> pos:", pos_str.flag)
    '''
    print(">>> include person name:", include_special_pos(test_text))

    test_text2 = "HuyaBioscienceInternationalLLC，中文名为沪亚生物国际有限责任公司，注册于美国的公司"
    print(">>> include company:", include_company(test_text2))



