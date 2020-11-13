#!/usr/bin/env python3
# coding: utf-8

##########
# Desc: Test pycorrectorUB for text correction.
# Author: WuBin
# Date: 2020.9.23

import jieba
from pycorrectorUB import corrector
import SegmentWord


def correct_sentence(_sentence, _crafted_type=False):
    corrector.enable_char_error(enable=False)  # 取消字符级纠错，误纠错率太高。
    # corrector.ppl_threshold_than_cur = 2800  # PPL候选词的阈值, for 2.8G语言模型
    # corrector.ppl_threshold_than_cur = 4100  # PPL候选词的阈值, for 144M语言模型
    # corrector.ppl_threshold_than_cur = 150
    # corrector.ppl_threshold_than_cur_one_word = 18000  # 纠错文本只有一个词（小于4个字）， PPL候选词的阈值
    # corrector.enable_word_error(False)  # 分词查找候选错误
    # corrector.use_custom_filter = False  # 是否使用定制的filter
    # corrector.segment_word_confusion = False  # 判断custom_confusion白名单词典时，是否先分词。默认是True。
    # corrector.ppl_threshold_one_word_crafted_type = 10000  # crafted_type人工设计的测试case的PPL阈值，短句子
    # corrector.ppl_threshold_crafted_type = 100  # crafted_type人工设计的测试case的PPL阈值
    print(">>> segment_word_confusion:", corrector.segment_word_confusion)
    # corrected_sent, detail = corrector.correct(_sentence)
    corrected_sent, detail = corrector.correct(_sentence, crafted_type=_crafted_type)
    print(">>> _sentence:", _sentence)
    print(">>> detail:", detail)

    # idx_errors = corrector.detect(_sentence)
    # print(">>> index of errors:", idx_errors)


# main method.
if __name__ == '__main__':
    print(">>> start.")
    crafted_type = False
    '''
    # sentence = '少先队员因该为老人让坐'
    # sentence = "硫酸粘杆菌素和浸提液的使用，纯华技术和进化工序。"
    # sentence = "我的喉咙发炎了要买点阿莫细林吃"
    sentence = "2、发行人股东、董事及高级管理人员 沈思、钱文杰、唯美南瓜、汉富满达、冬瓜科技、新疆正和、嘉德盈、龚小萍、君利联合及公司董事、高级管理人员承诺，如在启动股价稳定措施的前提条件满足时本人/本企业持有公司的股票，将在审议股份回购议案的股东大会中就相关股份回购议案投赞成票"
    sentence = sentence + " 优兔 领英 久邦"
    sentence = "本招股说明书签署日有效的《深圳清溢光电股份有限公司章程》"
    sentence = "战略性新兴产业的培育和发展，数万亿元的投资规模，给位于产业链上游的掩膜版产业提供了前所未有的创新发展空间"
    sentence = "香港光膜股权对应的遗产受益人为唐翔千先生的四名子女唐英敏、唐英年、唐庆年、唐圣年，该股权的受益权由四名子女平分,我的喉咙发炎了要买点阿莫细林吃,深圳清溢光电股份有限公司章程"
    
    sentence = "《通知》确定了国家重点支持的集成电路涉及领域包括重点集成电路设计领域：一、高性能处理器和FPGA芯片,台弯,波澜,情你寮解"
    sentence = "监事会提议召开时,保证记录的准确性,持有至到期投资"
    sentence = "但节点的设置应为取得阶段性成果或在某方面的技术取得突破，且不宜超过三个,"
    sentence = "国家级新型平板显示基地和全国最大的家电制造基地,郑加强"
    sentence = "本公司膜技术应用业务主要系根据客户的差异化需求"
    sentence = "由缺氧和好氧两部分反应组成的污水身物处理系统."
    sentence = "配副眼睛,高梁"
    sentence = "少先队员因该为老人让坐"
    sentence = "主要系根据财政部"
    # sentence = "元材料价格较高的风险"
    # sentence = "我的喉咙发炎了要买点阿莫细林吃"
    # sentence = "纯华技术和进化工序"
    '''
    sentence = "第二区（预反应区）和第三区（主反应区）,而京、津、冀地区,长账龄应收账款规模有所扩大、睿创微纳、艾睿光电近三年的收入毛利率如下"
    sentence = "备料、打胶,西达本胺，爱谱沙，西达本胺片，四组间比较F值为，苏陟"

    # sentence = "铝源,晶化，成胶槽,晶化罐,高堆重"
    sentence = "跨越了传统的电域(数字传送)和光域(模拟传送)"   # "是管理电域和光域的统一标准"
    sentence = "价芷，风藓, 网信办,插损小,汉广段"
    sentence = "《通知》确定了国家重点支持的集成电路涉及领域包括重点集成电路设计领域"  # 测试判断custom_confusion白名单词典时，是否先分词。
    sentence = "进入国际市场；“润百颜®”注射用修饰透明质酸钠凝胶2012年获得CFDA批准上市,华熙御美"

    sentence = "国医改办发,陌陌,润致,爆款"
    sentence = "氘代度,利用手性柱,反相手性柱,柱前,照像用还原剂,和信验字"
    sentence = "价芷,风藓,凸焊"
    sentence = "原由青岛海尔提名的周云杰由海尔集团提名,汽车车箱制造,银保监办发"
    sentence = "董事会应当做出详细说明"
    sentence = "地方铮策，招股拱司，炡策，宮司"
    # sentence = "点子业务，元材料"
    sentence = "赵金隨,犇创空间（武汉）云计算有限公司"  # customer_filter 需要针对整段文本处理，这个是测试case，每个符号都会拆分block。
    sentence = "烟财教指"
    sentence = "科睿唯安Cortellis数据库,依度沙班"
    sentence = "框梁,陕中庆验字"
    sentence = "具体信用政策系根据对不同类型客户的合作历史,但膜浓,自耗重熔"
    sentence = "做到专料专放,浙江鸿图航天,董事会应当做出详细说明,和信验字"
    sentence = "Li+从正极脱嵌,配碱,包覆装钵,盒厚，朱宏亮，棣环罚字"
    # sentence = "3、进一步完善利润分配郑策，优化投资者回报机制。工司负责人和主管会计工作的负责人。"
    # sentence = "棣环罚字,常州久日因车间废气散逸,交待给施工单位后"
    # sentence = "公经券中会程招据票效预之者正招书决据"
    sentence = "工司负责人和主管会计工作的负责人。"
    sentence = "其直接下游行业主要为FPC行业，产品价格在竞争对手同类产品价格的基础上适当下浮"
    sentence = "网络诈骗等安全威胁"
    sentence = "将掩膜版正"
    # sentence = "股票价芷，股市风藓。地方铮策，招股拱司，炡策，宮司"  # 2.8G语言模型默认配置可以纠错6个。 144M基于字符的语言模型可以纠错4个。
    sentence = "股票市腸，股市风藓。地方怔策，招股拱司，炡策，宮司"  # 20M基于字符的语言模型，默认配置可以纠错6个。144M基于字符的语言模型可以纠错4个。
    sentence = "壁障修补机,蒸镀掩膜版,移相掩模"
    sentence = "详参本节之,专户专储,海康威视,恒丰正泰验字"
    sentence = "缺芯少屏,噻唑烷二酮,锰酸锂,贮氢合金粉等。混料装钵，氟氯烃类"
    sentence = "公经券中会程招据票效预之者正招书决据"
    sentence = "津新关缉违,釜残液,异丁酰苯,环已基苯基甲酮,环已基苯基甲酮"
    sentence = "渤溢新天,Baylor医学院等机构陆续报导了很多适用于DEL化合物库合成的化学反应,称为公钥,,2018年受白城市海绵成市改造,端筑筑切试"
    sentence = "丸芯是盐酸纳曲酮,实勘，匀色，熔覆，芳烃，逢河必污,铝锂合金,和铌三锡,陕国税稽罚,纯铝,即使在急刹时也不易脱落,矽力杰"
    sentence = "遇水不塌缩,但遇水塌缩,人钙抑肽,端筑筑切试,下图展示了建成有孔的一层结构所需的步骤和设备,串焊,叠瓦机等,蓝宝石开方"

    sentence = "血虱,溢锡,钨化钛,创芯"
    # sentence = "将籽晶浸入,经张利国,积矽航,固矽优,钨化钛"
    # sentence = "发行人承租江苏新秀电器有限公司的厂房主要用于发行人材料及成品存储使用"
    sentence = "股市风癣，上市眒核，炡策，宮司。测拭用例。"  # 这些case，使用144M基于字符的语言模型可以完成5个纠错。PPL=3800,([['风藓', '风险', 2, 4], ['貢司', '公司', 7, 9], ['炡', '政', 10, 11], ['宮司', '公司', 13, 15], ['测拭', '测试', 16, 18]])。使用2.8G语言模型，可以完成后4个纠错，第一个不行。
    sentence = "正构烷烃,仑伐替尼等,克唑替尼,斜板沉淀除镍,禾裕科贷,磺达肝癸钠，叠瓦机等,蓝宝石开方，铝锂合金，逢河必污，银保监办发"
    sentence = "款项按照项目完诚的进度；已节算尚未完工款系在建合同已结算的价。"   # for crafted_type
    sentence = "征策，功司，钨化铝，检督，文因互联，赵进隨，固矽优，工司，郑策"
    sentence = "双鞭甲藻和裂殖壶菌,新猪毒OZK/93,胱抑素C,超华覆铜箔板,JX日矿，单毛锂电铜箔，5-四氟苯，胺解生产哌嗪，中欣氟材"
    sentence = "丝材和锻坯等,法匹拉韦,头孢呋辛酯分散片,不同人体大小以及不同场景下实现超过87%的识别率和低于3%的误识率"
    sentence = "款项按照项目完诚的进度；已节算尚未完工款系在建合同已结算的价。时别率，准缺率，功浩，流东性，企夜。证检会审查机制，保帐股民利意。"  # for crafted_type
    # sentence = "晶晨开曼,友邦恒誉"
    crafted_type = True  # 是不是人工设计的Case
    correct_sentence(sentence, crafted_type)

    # words = jieba.lcut(sentence)
    # print(">>> jieba segment words:", words)
    SegmentWord.test_segment_word(sentence)

