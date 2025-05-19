import re
with open("Text_sample.txt") as file:
    X =file.read()
# Define regex patterns
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
url_pattern = r'\bhttps?:\/\/(?:www\.)?[a-z0-9.-]+\.[a-z]{2,}(?:\/\S*)?\b'
phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
credit_card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
html_tags = r'<[^>]+>'
hashtags = r'#\w+'

# Read the file content
emails = re.findall(email_pattern, X)
urls = re.findall (url_pattern, X)
phones = re.findall(phone_pattern, X)
credit_cards = re.findall(credit_card_pattern, X)
html_tags = re.findall(html_tags, X)
hashtags = re.findall(hashtags, X)

# Print the results
print("Emails:\n", emails)
print("URLs:\n ", urls)
print("Phone numbers:\n ", phones)
print("Credit Card numbers:\n ", credit_cards)
print("HTML Tags:\n ", html_tags)
print("Hashtags:\n ", hashtags)

