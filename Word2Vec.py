from gensim.models import Word2Vec

# 加载Word2Vec模型
model = Word2Vec.load("test2.word2vec.model")

# 使用模型进行相关操作
# 获取单词的向量
vector1 = model.wv["Russia"]
print(vector1)

vector2 = model.wv["Ukraine"]
print(vector2)

print(model.wv.similarity('Russia', 'Ukraine'))