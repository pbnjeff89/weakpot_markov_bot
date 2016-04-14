# Using PyMarkovChain by TehMillhouse
# https://github.com/TehMillhouse/PyMarkovChain
# and praw, found at
# https://github.com/praw-dev/praw
#
# From the description of /r/Weakpots:
#
# /r/weightroom and /r/powerlifting got you down? 
# Can't deadlift 406 441 446? Are you proud of your 135lb. bench? 
# This sub is for you.Feel free to post 
# images/discussions/videos revolving around 
# how you are a failure of an athlete and 
# whether or not you should even.
#
# If you need someone else to make 
# you feel bad, you've not been paying attention.
# For most of us, the longer you lift,
# the stronger you realize you could be, and 
# the weaker you realize you are.

import praw
import os.path
from pymarkovchain import MarkovChain
import re

def writeComments(f, commentList):
	
	for comment in commentList:
		
		commentBody = comment.body
		
		links = re.findall('\[.*?\]\(.*?\)', commentBody)
		
		for link in links:
		
			commentBody = commentBody.replace(link,
					link[link.find("[") + 1:link.find("]")])

		try:
			f.write(commentBody + '\n')
		except UnicodeEncodeError:
			continue

comments_path = "c:/users/jeff/dropbox/weakpots_legion_bot/comments.txt"
user_agent = "Comment-Gatherer for Markov Chain by /u/pbnjeff"

comment_limit = 20

r = praw.Reddit(user_agent)

weakpots = r.get_subreddit('weakpots')
comments = weakpots.get_comments(limit=comment_limit)

if os.path.exists(comments_path):
	with open(comments_path,'a') as f:
		writeComments(f, comments)
else:
	with open(comments_path,'w') as f:
		writeComments(f, comments)
		
# update database
comments = ''
with open(comments_path,'r') as f:
	for line in f:
		comments = comments + str(line)
		
# testing
mc = MarkovChain('c:/users/jeff/dropbox/weakpots_legion_bot')
mc.generateDatabase(comments)