import pandas as pd
import jieba
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_excel("DragCrab-UserFeedback.xlsx")
feedbacks = df['用户反馈简述'].dropna().tolist()

stopwords = set(["了", "的", "不", "太", "每次", "都", "无法", "时候", "有些", "比较"])
all_words = [word for feedback in feedbacks for word in jieba.cut(feedback) 
             if word not in stopwords and len(word.strip()) > 1]

word_freq = Counter(all_words).most_common(10)
keywords_df = pd.DataFrame(word_freq, columns=['Keyword', 'Frequency'])

translation_dict = {
    "功能": "Feature", "设置": "Settings", "页面": "Page",
    "复杂": "Complex", "说明": "Explanation", "提示": "Prompt",
    "跳转": "Redirect", "加载": "Loading", "保存": "Save", "状态": "Status"
}

keywords_df['Keyword_EN'] = keywords_df['Keyword'].map(translation_dict)

plt.bar(keywords_df['Keyword_EN'], keywords_df['Frequency'])
plt.xlabel('High-frequency Keywords')
plt.ylabel('Frequency')
plt.title('Top 10 High-frequency User Feedback Keywords')
plt.show()