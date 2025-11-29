# Import libraries
from collections import Counter

import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Sample text dataset
text_data = [
    "Data science is fun",
    "Python is used for data analysis",
    "Machine learning and data science",
    "Visualization is important in data science",
]

# Combine all text into a single string
all_text = " ".join(text_data).lower()

# Split words and count frequencies
words = all_text.split()
word_counts = Counter(words)

# Display word frequencies (optional)
print("Word Frequencies:\n", word_counts)

# --- Visualization using WordCloud ---
wordcloud = WordCloud(
    width=800, height=400, background_color="white"
).generate_from_frequencies(word_counts)

# Plot the WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Frequency Visualization")
plt.show()

# --- Alternative: Bar Plot for Top Words ---
top_words = word_counts.most_common(10)  # Top 10 words
words, counts = zip(*top_words)

plt.figure(figsize=(10, 5))
plt.bar(words, counts, color="skyblue")
plt.title("Top 10 Word Frequencies")
plt.xlabel("Words")
plt.ylabel("Counts")
plt.show()
