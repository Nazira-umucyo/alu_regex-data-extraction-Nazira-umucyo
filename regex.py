import re

# Sample text (this would normally come from an API or web scraping result)
text = """
Contact me at user@example.com 
Visit https://www.example.com or https://subdomain.example.org/page.
Call (123) 456-7890 or 123-456-7890 or 123.456.7890.
Credit card: 1234 5678 9012 3456, 1234-5678-9012-3456.
Price: $19.99, $1,234.56, and $1234567.89 are listed.
"""

# Clean up the text using string methods
clean_text = text.replace("\n", " ").strip()

# Define regular expression patterns for each data type
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
url_pattern = r'https?://[^\s]+'
phone_pattern = r'(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'
card_pattern = r'(\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4})'
currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

# Use regex to find all matches in the cleaned text
emails = re.findall(email_pattern, clean_text)
urls = re.findall(url_pattern, clean_text)
phones = re.findall(phone_pattern, clean_text)
cards = re.findall(card_pattern, clean_text)
currencies = re.findall(currency_pattern, clean_text)

# Display the results
print("Emails found:", emails)
print("URLs found:", urls)
print("Phone numbers found:", phones)
print("Credit card numbers found:", cards)
print("Currency amounts found:", currencies)
