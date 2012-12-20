from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from datetime import datetime
import csv

debug = False
wp = Client('http://SITE/xmlrpc.php', 'USERNAME', 'PASSWORD')

def add_post(wp, title, body, category, date):
  date = datetime.strptime("%s 12:00:00 AM" % date, "%d-%b-%y %I:%M:%S %p")

	post = WordPressPost()
	post.title = title
	post.content = body
	post.terms_names = { 'category': [category,] }
	post.date = date
	post.post_status = 'publish'
	wp.call(NewPost(post))


c = csv.reader(open("FILE", "rU"))
counter = 0
for row in c:
	title = row[0]
	body = row[1]
	when = row[2]
	if debug:
		print "Title: %s" % title
		print "Body: %s" % body
		print "Date: %s" % when
		print ""
	
	add_post(wp, title, body, "CATEGORY", when)
	
	counter += 1
	if counter % 10 == 0:
		print "imported %s rows" % counter
