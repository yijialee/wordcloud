# --*-- coding:utf-8 --*--
__author__ = 'licha'
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
__author__ = 'licha'

import matplotlib
from wordcloud import WordCloud  # 词云包
import re
import jieba  # 分词包
import pandas as pd
import numpy  # numpy计算包
import os,sys
from PIL import Image

path = os.path.dirname(os.path.realpath(__file__))



def processChinese(text):
    seg_generator = jieba.cut(text)  # 使用结巴分词，也可以不使用
    stopwords = pd.read_csv( path +"/stop_words_zh_UTF-8.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                            encoding='utf-8')  # quoting=3全不引用
    seg_list = [i for i in seg_generator if i not in stopwords]
    seg_list = [i for i in seg_list if i != u' ']
    seg_list = r' '.join(seg_list)
    print seg_list
    return seg_list
def savePic(seg_lisg):
    wc = WordCloud( font_path= path + '/simhei.ttf',#设置字体
                background_color="black", #背景颜色
                max_words=2000,# 词云显示的最大词数
                 width=800, height=480,
                #max_font_size=100, #字体最大值
                random_state=42,
                )
    # 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
    wc.generate(seg_lisg)
    # wc.generate_from_frequencies(txt_freq)
    # txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
    # 从背景图片生成颜色值
    #  wc.to_file("b.png")
    img = wc.to_image()
    return img
    #html = wc.to_html()
    #print html

def cleanStopWords(cleaned_comments):
    segment = jieba.lcut(cleaned_comments)
    words_df = pd.DataFrame({'segment': segment})
    stopwords = pd.read_csv("stop_words_zh_UTF-8.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                            encoding='utf-8')  # quoting=3全不引用

    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    print words_df
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})

    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
    # print words_stat
    return words_stat

def mergeData(commit_list_all):
    comments = ''
    for c in commit_list_all:
        comments = comments + (str(c)).strip()

    cleaned_comments = ''.join(re.findall(u'[\u4e00-\u9fff]+', comments.decode("utf-8")))


def main():
    #commit_list_all = []
    #comments = mergeData(commit_list_all)
    d = "地理地理地理地理地理地理地理投资投资投资投资投资会议指出，发展健康服务业这一战略性产业，是推进供给侧结构性改革的重要内容，事关全体人民特别是老年人切身福祉，需求巨大且迫切。2013年以来，各地各相关部门贯彻建设健康中国战略部署，推动健康服务业快速发展，医疗机构床位数、医师数大幅增长，社会办医占比达45%。会议要求，下一步，一是要制定健康产业发展行动纲要，建立长效支持机制。二是深化“放管服”改革。发展改革委要抓紧出台社会办医疗、养老机构设置跨部门全流程综合审批办法，破除发展制约。推动二级及以下医疗机构设置审批与执业登记两证合一。对养老机构内设诊所实行备案制。三是卫生计生委要牵头建立综合监管制度，运用“双随机、一公开”方式，加强事中事后监管，做到包容、审慎、有效，营造公平公正的发展环境。四是加大短缺人才培养，发展重大创新药物、短缺药物、康复辅助器具等健康产品。五是鼓励社会力量发展体检、专科医疗等服务。放宽外资投资诊所股比限制。开展居家和社区养老改革试点，扶持专业或其他机构和志愿者为老年人提供服务。六是财税部门要抓紧调整社会办医疗、养老企业所得税政策，加大支持力度。推动健康服务业规范有序发展。"
    words_stat = processChinese(d)
    savePic(words_stat)
    print d

def getWordCloud(text):
    words_stat = processChinese(text)
    return savePic(words_stat)

if __name__ == "__main__":
    print("你好")

    main()
