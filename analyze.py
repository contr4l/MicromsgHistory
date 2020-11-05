import jieba.analyse
import string
filename = r'C:\Users\ctrl\Desktop\chat_tk'


# 此模块用于分析文件中的字频，输出结果形如 词语 --- 权重频次
def AnalyzeData():
    """
    Returns a dictionary of all tags from the file.

    Args:
    """
    f = open(filename + '.txt', 'r', encoding='gb18030')
    fcontent = f.read()
    alpha = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    tags = jieba.analyse.extract_tags(fcontent, topK=250, withWeight=True)
    new_tags = {}
    for k in range(len(tags)):
        uchar = tags[k][0][0]
        if uchar not in alpha:
            new_tags[tags[k][0]]= int(tags[k][1]*10000)

    # 将词频-词语保存为文件，注意格式化对齐的方式
    with open(filename + '_Word.txt', 'w') as f:
        for i, j in tags:
            if i[0] not in alpha:
                f.write('{:15}\t{:15}'.format(i,int(j*10000))+'\n')
            # print('{:8}\t{:10}'.format(i,int(j*10000)))
        f.close()

    # 返回字典为wordcloud提供依据
    return new_tags

from wordcloud import WordCloud
from scipy.misc import imread
import wordcloud

def cloudplot():
    """
    Generate cloudplotlib.

    Args:
    """
    # 设置模板图像的路径
    target_coloring = imread(r'C:\Users\ctrl\Desktop\heart.jpg')
    # 以词频和背景模板为依据生成词云对象
    word_cloud = WordCloud(font_path = r'C:\Windows\Fonts\simhei.ttf',
                           background_color="white",max_words=2000,mask=target_coloring).generate_from_frequencies(AnalyzeData())
    # 生成颜色分布
    image_color = wordcloud.ImageColorGenerator(target_coloring)
    # image_color =

    import matplotlib.pyplot as plt
    # 仅按照词频、边界、默认颜色生成词云图像
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.figure()

    # 重新上色，按照图像色彩分布生成
    plt.imshow(word_cloud.recolor(color_func=image_color))
    plt.axis("off")
    plt.figure()

    # 绘制原始图像
    plt.imshow(target_coloring,cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()

    word_cloud.to_file(filename+'.png')
    
cloudplot()