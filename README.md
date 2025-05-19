The code begins by importing the regular expressions, which is essential for pattern matching within text. A block of sample text is provided, which includes email addresses, URLs, phone numbers in different formats, credit card numbers, and currency amounts. Before applying regex patterns, the code first cleans the text using the string method replace() to remove newlines and strip() to eliminate any extra spaces at the beginning and end of the text. This ensures that the data is well-formatted for accurate pattern matching.
Next, the code defines separate regex patterns for each type of data it wants to extract. These patterns match the expected format of emails, URLs, phone numbers, credit card numbers, and currency amounts. Each regex is written to handle variations where necessary like phone numbers.
Once the patterns are defined, I use the re.findall() function to search through the cleaned text and extract all matches for each pattern. Each type of extracted data is stored in its own list for easy organization. This step makes it possible to isolate only the relevant information from the larger block of text without manual searching.
After extracting the data, the code applies the string method .strip() to further refine the results by removing any leftover spaces around each match. Though the sample data is already clean, this step ensures consistency, especially when working with messy real-world text.
Finally, the code uses the print() function to display the results in a clean, organized way. It prints out all the email addresses, URLs, phone numbers, credit card numbers, and currency amounts it found in the text. This makes it easy for a developer or user to quickly see the relevant information extracted from a large block of unstructured text.




# alu_regex-data-extraction-Nazira-umucyo
