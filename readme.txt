在外网环境下安装。
1，安装python-3.6.8-amd64.exe
2，安装jieba，
jieba-master.zip解压后执行： 
python setup.py build
python setup.py install
3，安装Numpy， pip install numpy
4，安装Numpy， pip install six
5，安装pypinyin，pip install pypinyin
6，安装kenlm，
kenlm-master.zip 解压后执行：
python setup.py build
python setup.py install

如果windows安装缺少microsoft visual c++ 14.0，需安装visualcppbuildtools_full.exe

语言模型很大，有2.8G，在code/Python/pycorrectorUB/data/lm目录，如果无法获取，可以直接从https://deepspeech.bj.bcebos.com/zh_lm/zh_giga.no_cna_cmn.prune01244.klm 下载，然后放到该目录。
可以选用144M的语言模型，邮件发送。默认使用该语言模型，放在在code/Python/pycorrectorUB/data/lm目录。

经测试，语言模型可以使用114M基于字符的小语言模型，相关参数已经调整，PPL默认阈值改为3800。
corrector.ppl_threshold_than_cur = 2800  # PPL候选词的阈值, for 2.8G语言模型
corrector.ppl_threshold_than_cur = 3800  # PPL候选词的阈值, for 144M语言模型
corrector.ppl_threshold_than_cur_one_word = 10000  # 句子长度小于4（单个词），PPL候选词的阈值, for 2.8G语言模型
corrector.ppl_threshold_than_cur_one_word = 18000  # 句子长度小于4（单个词），PPL候选词的阈值, for 144M语言模型

7，如果运行测试用的百度API时报错，缺少requests，可以重新安装，pip install requests


测试：
执行代码：code/Python/CorrectTextByPycorrectorUB.py
数据文件放在在data/prospectus目录下
代码在code/Python目录下
输出结果在code/Python/pycorrectorUB目录下，因为是追加写，测试前先把该目录的文件删除。

或者调用CorrectTextByPycorrectorUB.py的correct_text方法，输入text，返回纠错建议，例子：
text = "股市风癣，上市眒核，炡策，宮司。测拭用例。"
返回：[['风癣', '风险', 2, 4], ['眒', '审', 7, 8], ['炡', '政', 10, 11], ['宮司', '公司', 13, 15], ['测拭', '测试', 16, 18]]

或者参照correct_text方法的代码调用pycorrectorUB,注意以下设置：
corrector.enable_char_error(enable=False)  # 取消字符级纠错,误纠错率太高.
logger.setLevel('ERROR')  # set log level.

调用时，text建议用。分割，每句话一次请求。
当前版本，使用filter对人名（POS为nr），公司名（文本中包含“公司”，“企业”，“集团”）不做纠错，因为要减少招股书的误纠错，如果需要取消该filter，可以设置：corrector.use_custom_filter = False。
当前PPL阈值设置较高，导致召回率较低，建议手工修改测试时使用较短的词组，错字尽量使用生僻字。

针对招股书纠错，因为招股书本身很严谨，很容易产生误纠错，优先保证准确率。默认为该模式，调用方法：corrected_sent, detail = corrector.correct(_text)。
对于特定测试用例，需要提高召回率，又要保障准确率，可以使用crafted_type=True的模式，调用方法：
corrected_sent, detail = corrector.correct(_text, crafted_type=True) 
参考测试用例：
"款项按照项目完诚的进度；已节算尚未完工款系在建合同已结算的价。时别率，准缺率，功浩，流东性，企夜。证检会审查机制，保帐股民利意。" 
纠错结果：[['完诚', '完成', 6, 8], ['已节', '已结', 12, 14], ['时别', '识别', 31, 33], ['准缺率', '准确率', 35, 38], ['功浩', '功耗', 39, 41], ['流东性', '流动性', 42, 45], ['企夜', '企业', 46, 48], ['证检会', '证监会', 49, 52], ['保帐', '保障', 57, 59], ['利意', '利益', 61, 63]]


