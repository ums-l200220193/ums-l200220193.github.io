from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

with open("cleaned_data_group.csv", "r", encoding="utf-8") as file:
    data = file.readlines()

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data)
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
df.to_csv("scaled_data.csv", index=False)

