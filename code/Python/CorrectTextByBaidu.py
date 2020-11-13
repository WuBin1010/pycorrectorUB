#!/usr/bin/env python3
# coding: utf-8

##########
# Desc: Test baidu API for text correction.
# Author: WuBin
# Date: 2020.9.21

import TestBaiduApi
import ReadFiles
import Util


# Use Baidu text corrector API by SDK, write result in output file.
# _text size limit 511 Byte.
def baidu_api_corrector_write(_client, _input_file_name, _text, _output_path, _block_index):
    print(">>> baidu corrector API:")

    # Use baidu corrector API:
    count = 0
    try:
        result = _client.ecnet(_text)

        # print(">>> get result:" + str(result))
        output_file1 = _output_path + "result_all_" + _input_file_name
        output_f1 = open(output_file1, 'a+', encoding="utf-8")  # 追加写，重新测试要删除原文。
        output_f1.write(">>> block " + str(_block_index) + "\n")
        # write output file1 with all result by Json.

        output_f1.write(str(result) + "\n\n")
        output_f1.close()

        if "item" in result:
            item = result["item"]
            frag_list = item["vec_fragment"]
            count = len(frag_list)
            print(">>> corrector result count:" + str(count))

            # write output file2 with only correct result .
            output_file2 = _output_path + "result_correct_" + _input_file_name
            output_f2 = open(output_file2, 'a+', encoding="utf-8")
            output_f2.write(">>> block " + str(_block_index) + "\n")

            for i in range(count):
                frag = frag_list[i]
                ori_frag = frag["ori_frag"]
                correct_frag = frag["correct_frag"]
                correct_str = ">>> ori_frag: %s , correct_frag: %s" % (ori_frag, correct_frag)
                print(correct_str)
                output_f2.write(correct_str + "\n\n")

            output_f2.close()

    except UnicodeEncodeError:  # 遇到该异常是GBK字符集比较小的问题，可以继续执行。
        print(">>> UnicodeEncodeError: 'gbk' codec can't encode character.")

    return count


# Read text files and correct.
def correct_files(_client, _file_list, _output_path):
    block_size = 170  # block size 511 Byte for Baidu API. utf-8, one Chinese <= 3 Byte
    i = 0
    start_n = 1
    end_n = 1  # for part text files
    correct_sum = 0
    for file_dict in _file_list:
        file_name = str(list(file_dict.keys())[0]).split("\\")[-1]
        i = i + 1
        if start_n <= i <= end_n:
            # text_gbk = str(file).encode("gbk", 'ignore')  # 'ignore' for some error code.
            # block_list = re.findall(r'.{' + str(block_size) + '}', str(file))
            block_list = Util.cut_text(str(list(file_dict.values())[0]), block_size)
            print(">>>>>> file name:", file_name)
            print(">>> block list size:", len(block_list))
            block_index = 0
            for block in block_list:
                block_text = str(block)
                # print(">>> block: ", str(block_text))
                print(">>> block index:", block_index)
                print(">>> block size: ", len(block.encode("utf-8")))  # Byte size

                # correct:
                count = baidu_api_corrector_write(_client, file_name, block_text, _output_path, block_index)
                correct_sum = correct_sum + count

                block_index = block_index + 1

    print(">>> correct sum:", correct_sum)


# main method.
if __name__ == '__main__':
    print(">>> start.")
    get_client = TestBaiduApi.get_baidu_api_client()

    input_path = "D:\\corrector\\data\\prospectus\\"
    encoding = "utf-8"
    file_list = ReadFiles.read_all_files(input_path, encoding)
    output_path = "D:\\corrector\\code\\Python\\output\\"
    correct_files(get_client, file_list, output_path)
