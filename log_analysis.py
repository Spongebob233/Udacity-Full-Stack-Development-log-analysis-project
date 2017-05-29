import psycopg2

DBNAME = "news"
db = psycopg2.connect(dbname=DBNAME)
c = db.cursor()

def getMostPopularArticles():
    c.execute("SELECT * from article_views ORDER BY views DESC LIMIT 3;")
    return c.fetchall()

def getMostPopularAuthors():
	c.execute("""
		SELECT author_article.name, SUM(article_views.views) AS author_views
		FROM author_article, article_views
		WHERE article_views.title = author_article.title
		GROUP BY author_article.name 
		ORDER BY author_views DESC;
		""")
	return c.fetchall()

def getErrorRates():
	c.execute("""
		SELECT * 
		FROM error_rates
		WHERE error_ratio > 1
		ORDER BY error_ratio DESC
		""")
	return c.fetchall()

mostPopularArticles = getMostPopularArticles()
mostPopularAuthors = getMostPopularAuthors()
errorRates = getErrorRates()

print("The top 3 articles are:")
for article in mostPopularArticles:
	print('{0} - {1} views'.format(article[0], article[1]))

print("The most popular author are:")
for author in mostPopularAuthors:
    print('{0} - {1} views'.format(author[0], author[1]))

print("On which days did more than 1% of requests lead to errors?")
for errorRate in errorRates:
	print ('{0} : {1}%'.format(errorRate[0], round(errorRate[1],2)))

db.close()

