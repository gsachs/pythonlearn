# Simple string match function using brute force
def string_match(given,pattern):

	given_len = len(given)
	pattern_len = len(pattern)
	pattern_count = 0
	pos = -1

	for i in range(given_len):
		for j in range(pattern_len):
			if given[i+j] == pattern[j]:
				pattern_count = pattern_count + 1
				if j == pattern_len - 1: 
					pos = i 	
			else:
				break			
			
	print(pos)

given = "quickbrownfoxjumpedoverthelazydog"
#	"012345678901234567890123456789012"
pattern = "lazy"
string_match(given,pattern)
