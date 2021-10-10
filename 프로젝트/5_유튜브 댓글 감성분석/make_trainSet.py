# 학습 데이터 구성을 위함
import numpy as np
import pandas as pd
import json
import re

txts = []
with open('YouTubeResult.txt','r',encoding='UTF8') as f:
    string = f.readlines()
    for li in string:
        try:
            if np.random.rand()<0.05:
                txts.append(json.loads(li)['text'])
        except:
            pass
        

pd.Series(txts).apply(lambda x:re.sub(r'[^ ㄱ-ㅣ가-힣]+'," ",x)).to_excel('training.xlsx',index=False)
