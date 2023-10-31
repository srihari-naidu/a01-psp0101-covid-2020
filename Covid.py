# Some of the common imports (you can add more here)
import random
import string
# Import from psphelper.py file
import psphelper


# 1. How to read quotes from "quotes.txt"
quotes = psphelper.readQuotesFromFile("quotes.txt");
print("List of quotes");
no = 1;
for q in quotes:
	print("{0}. {1}".format(no, q));
	no += 1;
	
# 2. Quote Screen
myQuote = "Practice Makes Perfect";
width = 15
psphelper.showQuoteScreen(myQuote, width);

# 3. How about a title at the centre?
title = "## Title ##";
width = 25;
borderWidth = 4;
print(title.center(width + borderWidth));
psphelper.showQuoteScreen(myQuote, width);


