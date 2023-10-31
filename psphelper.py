import os

## Helpful Functions

# Read a list of quotes from a file
# 	filename - the name of the file from which quotes are read. 
def readQuotesFromFile(filename):
	quotes = list();
	f = open(filename, "r");
	for line in f:
		quotes.append(line.strip().upper());
	return quotes;

# Convert an alphabet to underscore. Non-alphabets are ignored.
# 	letter - the letter to convert
# 
# * this function assumes letter to be a single character.
def alphaToUnderscore(letter):
	if (letter.isalpha()):
		return '_'
	else:
		return letter;

# Clear the command prompt screen
def clearScreen():
	if os.name == "nt":
		os.system("cls");
	else:
		os.system("clear");

# Show the quote screen
# 	quote - the quote string to be displayed on the quote screen
#	limit - the width of quote screen (excluding borders)
def showQuoteScreen(quote, limit):

	# Constants
	SPACE = "   ";
	SPACE_LENGTH = len(SPACE);
	STAR_LINE = "".ljust(limit + 2, '-');
	
	# Insert space to the quote
	q = quote.split();
	q1 = [" ".join(word) for word in q];
	quoteSpaced = SPACE.join(q1);

	# Top border
	print("+{0}+".format(STAR_LINE));

	start = 0;
	while True:
		remaining = len(quoteSpaced) - start;
		
		# Haven't cover last letter (i.e. not last line)
		if limit < remaining:
			
			# Find the last occurrence of SPACE within the subquote in [start:start+limit]
			# End should point to the letter after the last SPACE.
			end = start + limit;
			if quoteSpaced[end:end+SPACE_LENGTH] != SPACE:
				end = SPACE_LENGTH + quoteSpaced.rfind(SPACE, start, end);
			
			# Print
			print("| {0:<{1}} |".format(quoteSpaced[start:end], limit));
			
			# Update start
			start = end;
			if quoteSpaced[end:end+SPACE_LENGTH] == SPACE:
				start += SPACE_LENGTH;
		# Last line
		else:
			print("| {0:<{1}} |".format(quoteSpaced[start:], limit));
			break;

	# Bottom border
	print("+{0}+".format(STAR_LINE));
	
#  Test
if __name__ == "__main__":

	quote = str(input("Enter quote: "));
	limit = int(input("Enter limit: "));

	showQuoteScreen(quote, limit);