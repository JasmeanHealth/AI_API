import pandas as pd
import sys

df = pd.read_excel('F:/JasmeanHealth/AI_API/data/211225_data_summary_v1.xlsx')
doc_list = df['clincal_imp'].to_list()

from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

embeddings = model.encode(doc_list, convert_to_tensor=True)

def getTS(word = '갑자기 배가 아파요'):
    word2vec = model.encode(word, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(word2vec, embeddings)
    df['score'] = scores[0]
    
    results = df.sort_values("score", ascending=True).head(10)

    js = results.to_json(orient='records')
    print(js)
    
    # js = df.to_json(orient='records')
    # print(js)
    # scores = scores[0]

    # for col in df.columns:
    #     print(col, end='\t')
    # print('score')
    # for i in scores.argsort(descending=True)[0:10]:
    #     for col in df.columns:
    #         print(df[col][df.clincal_imp == doc_list[i]].values[0], end = '\t')
    #     print(f"{scores[i]:.4f}")


if __name__ == '__main__':
    getTS(sys.argv[1]) if len(sys.argv) >= 2 else getTS()