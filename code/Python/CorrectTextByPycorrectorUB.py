#!/usr/bin/env python3
# coding: utf-8

##########
# Desc: Test pycorrectorUB for text files correction. Use UTF-8 for all text.
# Author: WuBin
# Date: 2020.9.25

from pycorrectorUB import corrector
import ReadFiles
import Util
from pycorrectorUB.utils.logger import logger

corrector.enable_char_error(enable=False)  # 取消字符级纠错,误纠错率太高.


# Use pycorrectorUB for text files, write result in output file.
def pycorrectorUB_write(_input_file_name, _text, _output_path, _block_index):
    print(">>> pycorrectorUB:")

    # 以下设置建议使用默认值，如有特殊需要，再做修改：
    # corrector.ppl_threshold_than_cur = 2800  # PPL候选词的阈值, for 2.8G语言模型。
    # corrector.ppl_threshold_than_cur_one_word = 10000  # 纠错文本只有一个词（小于4个字）， PPL候选词的阈值
    # corrector.enable_word_error(False)  # 分词查找候选错误，默认是True。
    # corrector.use_custom_filter = False  # 是否使用定制的filter，默认是True。
    # corrector.segment_word_confusion = False  # 判断custom_confusion白名单词典时，是否先分词。默认是True。
    # corrector.ppl_threshold_than_cur = 3800  # PPL候选词的阈值, for 144M语言模型, default value.
    # corrector.ppl_threshold_than_cur_one_word = 18000  # 纠错文本只有一个词（小于4个字）， PPL候选词的阈值

    # Use pycorrectorUB:
    count = 0
    corrected_sent, detail = corrector.correct(_text)

    print(">>> get result:" + str(detail))
    count = count + len(detail)
    output_file1 = _output_path + "result_all_" + _input_file_name
    output_f1 = open(output_file1, 'a+', encoding="utf-8")  # 追加写，重新测试要删除原文。
    output_f1.write(">>> block " + str(_block_index) + "\n")
    # write output file1 with all result by Json.

    output_f1.write(_text + "\n")
    output_f1.write(str(detail) + "\n\n")
    output_f1.close()
    return count


# Read text files and correct. for part text files, start n , end n.
def correct_files(_file_list, _output_path, start_n, end_n):
    i = 0
    # start_n = 8
    # end_n = 8  # for part text files
    correct_sum = 0
    for file_dict in _file_list:
        file_name = str(list(file_dict.keys())[0]).split("\\")[-1]
        i = i + 1
        if start_n <= i <= end_n:
            block_list = Util.cut_text_stop(str(list(file_dict.values())[0]))
            print(">>>>>> file name:", file_name)
            print(">>> block list size:", len(block_list))
            block_index = 0
            for block in block_list:
                block_text = str(block)
                # print(">>> block: ", str(block_text))
                print(">>> block index:", block_index)
                print(">>> block size: ", len(block.encode("utf-8")))  # Byte size

                # correct:
                count = pycorrectorUB_write(file_name, block_text, _output_path, block_index)
                correct_sum = correct_sum + count

                block_index = block_index + 1
    print(">>> correct sum:", correct_sum)


# correct text by pycorrectorUB, text is a sentence, use utf-8 encoding. 调用时，text建议用。分割，每句话一次请求。
def correct_text(_text, _crafted_type=True):
    corrected_sent, detail = corrector.correct(_text, crafted_type=_crafted_type)

    return str(detail)


# main method.
if __name__ == '__main__':
    print(">>> start.")

    logger.setLevel('ERROR')  # set log level.

    # correct files:
    input_path = "../../data/prospectus"
    # input_path = "../../data/prospectus2/"
    encoding = "utf-8"
    file_list = ReadFiles.read_all_files(input_path, encoding)
    output_path = "./output/pycorrectorUB/"
    # for part text files, start n , end n.
    file_start_n = 1
    file_end_n = 2
    correct_files(file_list, output_path, file_start_n, file_end_n)

    # correct text, 采用招股书的默认模式:
    test_text = "股市风藓，上市眒核，炡策，宮司。测拭用例。"
    print(">>> correct_text get result:", correct_text(test_text))
    # 对于新的测试用例使用新的模式：
    sentence = "款项按照项目完诚的进度；已节算尚未完工款系在建合同已结算的价。征策，功司。"
    print(">>> correct_text get result:", correct_text(sentence, _crafted_type=True))

