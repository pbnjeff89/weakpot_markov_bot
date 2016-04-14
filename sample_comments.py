from pymarkovchain import MarkovChain
import re

comments_path = "c:/users/jeff/dropbox/weakpots_legion_bot/comments.txt"
comments = ''

# establish a list of regular expressions
regExpressions = [ re.compile(r'\[(.*?)\]') ]

with open(comments_path,'r') as f:
	for line in f:
	
		# TODO: for each line, break up string into
		# smaller strings and test if they fulfill the
		# regular expressions in the list above
		
		comments = comments + str(line)
		
# testing
mc = MarkovChain('c:/users/jeff/dropbox/weakpots_legion_bot')
mc.generateDatabase(comments)
for i in range(50):
	print(mc.generateString())