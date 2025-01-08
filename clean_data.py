import re

with open("data_group.csv", "r", encoding="utf-8") as file:
    content = file.read()

cleaned_content = re.sub(r'[^A-Za-z0-9\s.,?!:]', '', content)

with open("cleaned_data_group.csv", "w", encoding="utf-8") as file:
    file.write(cleaned_content)

