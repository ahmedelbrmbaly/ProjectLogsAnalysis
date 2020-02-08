#!/usr/bin/env python3

import psycopg2

# Open a connection with database
DBNAME = "news"     # Database Name
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# Most popular three articles of all time
articleViews = "select * from articlesviews limit 3;"
c.execute(articleViews)     # Get results from database
results = c.fetchall()
print("\nMost popular three articles of all time: ")
for row in results:     # Print results in seperated lines
    print('"', row[0], '"', "  __  ", row[1], "Views")

# Most popular author
authorsViews = "select * from authorsviews limit 1;"
c.execute(authorsViews)     # Get results from database
results = c.fetchall()
print("\nMost popular author:")
for row in results:     # Print results in seperated lines
    print(row[0], "  __  ", row[1], "Views")

# Days with more than 1% errors
errors = "select * from failpercent where percent > 1;"
c.execute(errors)       # Get results from database
results = c.fetchall()
print("\nDays with more than 1% errors:")
for row in results:     # Print results in seperated lines
    print(row[0], "  __  ", row[1], "% errors")
db.close()      # Close connection
