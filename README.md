# Udacity-Full-Stack-Development-log-analysis-project
# Log analysis

This is the project required for the Udacity Nanodegree for Full Stack Web development. We are given a database and asked to extract specific information. The database includes three tables:

1. The **articles** table includes information about articles.
2. The **authors** table includes information about authors.
3. The **log** table table includes one entry for each time a user has accessed the site.

Questions we need to answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

## Instructions
1. Install vagrant and virtual box and start the virtual machine by the order vagrant up and vagrant ssh.

2. Set up the database: psql -d news -f newsdata.sql

3. Create views.
  * CREATE VIEW article_views AS SELECT title, count(\*) AS views FROM articles, log WHERE articles.slug=subtr(log.path from 10) GROUP BY artiles.title ORDER BY view_num DESC;
 
 * CREATE VIEW author_article AS SELECT authors.name,authors.id,articles.title from authors, articles where author.id=article.author;
 
 * CREATE VIEW error_request AS SELECT  date(time), count(\*) AS error_num FROM log WHERE status !='200 OK' GROUP BY date(time); 
 
 * CREATE VIEW total_request AS SELECT date(time), count (\*) AS total_num from log GROUP BY date(time);
 
 * CREATE OR REPLACE VIEW error_rates AS SELECT error_request.date, (error_request.error_num::float/total_request.total_num\*100) AS error_ratio FROM error_request, total_request WHERE error_request.date=total_request.date ORDER BY error_ratio DESC;
 
 4. Run python log_analysis.py in the terminal.
 
 ## Outputs
1. What are the most popular three articles of all time?
The top 3 articles are:
<br> Candidate is jerk, alleges rival - 338647 views
<br>Bears love berries, alleges bear - 253801 views
<br>Bad things gone, say good people - 170098 views

2. Who are the most popular article authors of all time?
<br>Ursula La Multa - 507594 views
<br>Rudolf von Treppenwitz - 423457 views
<br>Anonymous Contributor - 170098 views
<br>Markoff Chaney - 84557 views

3. On which days did more than 1% of requests lead to errors? 
<br>2016-07-17 : 2.26%

