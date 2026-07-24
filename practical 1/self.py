import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("NetFlix.csv")

# Clean comma-separated genres
genres = df['genres'].dropna().str.split(', ').explode()
genre_counts = genres.value_counts()

top_10_genres = genre_counts.head(10)
bottom_10_genres = genre_counts.tail(10)
most_popular = genre_counts.idxmax()
least_popular = genre_counts.idxmin()

print("--- Top 10 Genres ---")
print(top_10_genres)

print("\n--- Bottom 10 Genres ---")
print(bottom_10_genres)

print(f"\nMost Popular Genre: {most_popular} ({genre_counts.max()} titles)")
print(f"Least Popular Genre: {least_popular} ({genre_counts.min()} titles)")

# Visualization
plt.figure(figsize=(10, 5))
top_10_genres.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Netflix Genres')
plt.xlabel('Genre')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
