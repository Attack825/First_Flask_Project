import json
import jieba
import time
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import operator
import os
import pickle


# word 是要查找的关键字
def top5(word):
    time_start = time.time()
    content = []
    # 将json文件打开并转化为字符串的形式
    with open('D:\\pythonProject\\tfidf_cooperate\\tf_idf\\data_20k(1).json', 'r', encoding='utf-8') as f:
        # 逐行将数据加入列表
        for line in f:
            # 将str类数据转换城字典类
            json_data = json.loads(line)
            content.append(json_data)
    dataset = content

    list = []
    with open('D:\\pythonProject\\tfidf_cooperate\\tf_idf\\data_a3.txt', 'r', encoding='utf-8') as f:
        for line in f:
            list.append(line)
        word_lists = list

    fenci_word = " ".join(jieba.cut(word))
    word = fenci_word

    vectorizer = TfidfVectorizer()
    if os.path.exists('D:\\pythonProject\\tfidf_cooperate\\tf_idf\\train_fit_path.dat'):
        train_fit = pickle.load(open('D:\\pythonProject\\tfidf_cooperate\\tf_idf\\train_fit_path.dat', 'rb'))
    else:
        train_fit = vectorizer.fit(word_lists)
        pickle.dump(train_fit, open('D:\\pythonProject\\tfidf_cooperate\\tf_idf\\train_fit_path.dat', 'wb'))

    if os.path.exists('D:\\pythonProject\\tfidf_cooperate\\tf_idf\\train_path.dat'):  # 判断这个路径是否存在
        train_matrix = pickle.load(open('D:\\pythonProject\\tfidf_cooperate\\tf_idf\\train_path.dat', "rb"))
    else:
        train_matrix = vectorizer.transform(word_lists)  # 训练集
    test_matrix = train_fit.transform([word])  # 测试集

    res = cosine_similarity(test_matrix, train_matrix)
    pickle.dump(train_matrix, open('D:\\pythonProject\\tfidf_cooperate\\tf_idf\\train_path.dat', "wb"))
    i = 0
    for x in res:
        for a in x:
            i = i + 1

    recommend_dict = {}
    id = 0
    # 创立字典，将id与其对应的相似度存入其中
    for x in res:
        while (id < (len(x))):
            recommend_dict[id] = x[id]
            id = id + 1
    # print(recommend_dict)
    a = []
    # 用列表排序，再将最大的前10为序号存入列表a
    recommendation_id = sorted(recommend_dict.items(), key=operator.itemgetter(1), reverse=True)

    # 获得相关度最高的前五个的位置
    for i in range(0, 5):
        a.append(recommendation_id[i][0])

    final_list = []
    for x in a:
        for k, v in dataset[x].items():
            if k == 'fullText':
                final_list.append(v)

    time_end = time.time()
    time_c = time_end - time_start  # 运行所花时间
    return final_list


if __name__ == '__main__':
    print(top5('盗窃'))
