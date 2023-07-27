from newspaper import Article

url = 'https://en.wikipedia.org/wiki/Muhammad_Ali_Jinnah'
article = Article(url)
article.download()

article.parse()
article.text

print(article.text)