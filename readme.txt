�����������°�װ��
1����װpython-3.6.8-amd64.exe
2����װjieba��
jieba-master.zip��ѹ��ִ�У� 
python setup.py build
python setup.py install
3����װNumpy�� pip install numpy
4����װNumpy�� pip install six
5����װpypinyin��pip install pypinyin
6����װkenlm��
kenlm-master.zip ��ѹ��ִ�У�
python setup.py build
python setup.py install

���windows��װȱ��microsoft visual c++ 14.0���谲װvisualcppbuildtools_full.exe

����ģ�ͺܴ���2.8G����code/Python/pycorrectorUB/data/lmĿ¼������޷���ȡ������ֱ�Ӵ�https://deepspeech.bj.bcebos.com/zh_lm/zh_giga.no_cna_cmn.prune01244.klm ���أ�Ȼ��ŵ���Ŀ¼��
����ѡ��144M������ģ�ͣ��ʼ����͡�Ĭ��ʹ�ø�����ģ�ͣ�������code/Python/pycorrectorUB/data/lmĿ¼��

�����ԣ�����ģ�Ϳ���ʹ��114M�����ַ���С����ģ�ͣ���ز����Ѿ�������PPLĬ����ֵ��Ϊ3800��
corrector.ppl_threshold_than_cur = 2800  # PPL��ѡ�ʵ���ֵ, for 2.8G����ģ��
corrector.ppl_threshold_than_cur = 3800  # PPL��ѡ�ʵ���ֵ, for 144M����ģ��
corrector.ppl_threshold_than_cur_one_word = 10000  # ���ӳ���С��4�������ʣ���PPL��ѡ�ʵ���ֵ, for 2.8G����ģ��
corrector.ppl_threshold_than_cur_one_word = 18000  # ���ӳ���С��4�������ʣ���PPL��ѡ�ʵ���ֵ, for 144M����ģ��

7��������в����õİٶ�APIʱ����ȱ��requests���������°�װ��pip install requests


���ԣ�
ִ�д��룺code/Python/CorrectTextByPycorrectorUB.py
�����ļ�������data/prospectusĿ¼��
������code/PythonĿ¼��
��������code/Python/pycorrectorUBĿ¼�£���Ϊ��׷��д������ǰ�ȰѸ�Ŀ¼���ļ�ɾ����

���ߵ���CorrectTextByPycorrectorUB.py��correct_text����������text�����ؾ����飬���ӣ�
text = "���з�Ѣ�����бm�ˣ��ڲߣ��m˾������������"
���أ�[['��Ѣ', '����', 2, 4], ['�m', '��', 7, 8], ['��', '��', 10, 11], ['�m˾', '��˾', 13, 15], ['����', '����', 16, 18]]

���߲���correct_text�����Ĵ������pycorrectorUB,ע���������ã�
corrector.enable_char_error(enable=False)  # ȡ���ַ�������,�������̫��.
logger.setLevel('ERROR')  # set log level.

����ʱ��text�����á��ָÿ�仰һ������
��ǰ�汾��ʹ��filter��������POSΪnr������˾�����ı��а�������˾��������ҵ���������š�������������ΪҪ�����й��������������Ҫȡ����filter���������ã�corrector.use_custom_filter = False��
��ǰPPL��ֵ���ýϸߣ������ٻ��ʽϵͣ������ֹ��޸Ĳ���ʱʹ�ý϶̵Ĵ��飬���־���ʹ����Ƨ�֡�

����й��������Ϊ�й��鱾����Ͻ��������ײ�����������ȱ�֤׼ȷ�ʡ�Ĭ��Ϊ��ģʽ�����÷�����corrected_sent, detail = corrector.correct(_text)��
�����ض�������������Ҫ����ٻ��ʣ���Ҫ����׼ȷ�ʣ�����ʹ��crafted_type=True��ģʽ�����÷�����
corrected_sent, detail = corrector.correct(_text, crafted_type=True) 
�ο�����������
"�������Ŀ��ϵĽ��ȣ��ѽ�����δ�깤��ϵ�ڽ���ͬ�ѽ���ļۡ�ʱ���ʣ�׼ȱ�ʣ����ƣ������ԣ���ҹ��֤��������ƣ����ʹ������⡣" 
��������[['���', '���', 6, 8], ['�ѽ�', '�ѽ�', 12, 14], ['ʱ��', 'ʶ��', 31, 33], ['׼ȱ��', '׼ȷ��', 35, 38], ['����', '����', 39, 41], ['������', '������', 42, 45], ['��ҹ', '��ҵ', 46, 48], ['֤���', '֤���', 49, 52], ['����', '����', 57, 59], ['����', '����', 61, 63]]


