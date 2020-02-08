# Log Analysis
This is a reporting tool that prints out  reports based on the data in the "news" database.  This reporting tool is  a `python3`  program using `pscopg2` module to connect to database.

## Prerequisites
* Python version 2.7
* Python 3 versions from 3.4 to 3.8
* PostgreSQL server versions from 7.4 to 12
* PostgreSQL client library version from 9.1
* Psycopg2


## SQL created views

   ###  1. _**articlesviews**_:
 this view consists of two columns :
   * _title_ : includes articles titles.
   * _views_ : includes number of views per article.   

```
create view articlesviews as
 select articles.title, count(*) as views
from articles join log
on log.path  like concat('%',articles.slug)
group by articles.title
order by views desc ;
```

  ### 2.  _**authorsviews**_:
 this view consists of two columns :
* _name_ : includes names of authors.
* _views_ : includes number of views per author.

   ```
   create view authorsviews as
   select authors.name,
   sum (articlesviews.views ) as views
   from articles ,  articlesviews, authors  
   where  articles.title = articlesviews.title
   and authors.id = articles.author  
   group by authors.name
   order by views desc;
   ```
  ### 3.   _**failpercent**_:
 this view consists of two columns :
* _date_ : includes dates.
* _percent_ : includes the percent of non-successful requests.

   ```
    create view failpercent as
    select cast(time as date) as date,
    round(((cast(count(case status when '200 OK' then null  else 1 end) as decimal) /
    cast(count (status) as decimal)) * 100),2) as percent
    from log
    group by date
    order by date;
    ```


## How it works
1. Open terminal
2. Go to the containing directory
3. Make sure That you have ` newsdata.sql` installed
4. Type this commnad line
    `python3 LogsAnalysis.py`  


## The result
```
    Most popular three articles of all time:
    " Candidate is jerk, alleges rival "   __   338647 Views
    " Bears love berries, alleges bear "   __   253801 Views
    " Bad things gone, say good people "   __   170098 Views

    Most popular author:
    Ursula La Multa   __   507594 Views

    Days with more than 1% errors:
    2016-07-17   __   2.26 % errors
```
## License
**_Log Analysis_** is free open source script .
# ProjectLogsAnalysis
