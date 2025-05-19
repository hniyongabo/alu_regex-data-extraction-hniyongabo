Regex Data Extraction Script

OVERVIEW

This Python script reads the content of a text file and uses regular expressions (regex) to extract different types of data, such as:

Email addresses

URLs

Phone numbers

Credit card numbers

HTML tags

Hashtags

The script prints each category’s matches found in the text file.


HOW IT WORKS

The script opens and reads the entire content of Text_sample.txt.

It defines regex patterns tailored to match:

Emails (like example@word.com)

URLs starting with http:// or https://

Phone numbers in common formats (with or without parentheses, dashes, spaces)

Credit card numbers are formatted as groups of 4 digits separated by spaces or dashes

HTML tags (anything inside < >)

Hashtags (words starting with #)

It searches the file content for each pattern using Python’s re.findall().

Finally, it prints out all the matched results grouped by their categories.

USAGE INSTRUCTIONS

1. Place the file Text_sample.txt in the same directory as the script. This file should contain the text data for extraction.

2. Execute the script using Python 3

3. The output will display lists of extracted emails, URLs, phone numbers, credit card numbers, HTML tags, and hashtags.
