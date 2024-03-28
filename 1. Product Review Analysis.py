# Task 1: Keyword Highlighter

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def review_emphasizer(review_list):
    keywords = [
        "good",
        "excellent",
        "bad",
        "poor",
        "average"
    ]

    modified_reviews = []

    for review in review_list:
        for word in keywords:
            # print(word)
            word_index = review.find(word)
            # print(word_index)
            if word_index != -1:
                print(review.replace(word, word.upper()))

review_emphasizer(reviews)

# Task 2: Sentiment Tally

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally_counter(reviews, pos_words, neg_words):
    # positive_count = 0
    # negative_count = 0
    
    for review in reviews:
        positive_count = 0
        negative_count = 0
        for word in pos_words:
            positive_count += review.lower().count(word)
        for word in neg_words:
            negative_count += review.lower().count(word)
            
        print(f"Word counts for this review:\n - {review}")
        print(f" - Positive words: {positive_count}")
        print(f" - Negative words: {negative_count}")

tally_counter(reviews, positive_words, negative_words)


# Task 3: Review Summary

def make_summary(reviews):
    for review in reviews:
        word_list = review.split()
        character_count = 0
        word_index = 0
        for word in word_list:
            if character_count < 31:
                character_count += len(word)
                word_index += 1
        print(' '.join(word_list[:word_index]) + "...")

make_summary(reviews)