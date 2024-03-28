1. Product Review Analysis
Objective:
The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

Task 1: Keyword Highlighter

Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
2. User Input Data Processor
Objective:
The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator
Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

Task 2: Password Complexity Checker
Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

Task 3: Email Formatter
Implement a script that ensures all user email addresses are in a standard format

3. Interactive Help Desk Bot
Objective:
The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.

Task 1: Command Parser
Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

Task 2: Issue Categorizer
If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.

