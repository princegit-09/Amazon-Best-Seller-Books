import pandas as pd
df=pd.read_csv('Bestseller.csv')
df.drop_duplicates(inplace=True)
df.rename(columns={"brand":"Author","reviewsCount":"Reviews","stars":"Ratings","price/currency":"Currency","price/value":"Price"},inplace=True)
author_counts=df['Author'].value_counts()
avg_rating_by_genre = df[df['Author']=='Generic']["Ratings"].mean()
#print(author_counts)
author_counts.head(10).to_csv("Top_sellers.csv")
#print(author_counts.head(10))


import matplotlib.pyplot as plt
import seaborn as sns 

# top 10 amazon best selling books  
top_authors = author_counts.head(10)   # assuming author_counts is your Series
plt.figure(figsize=(10,6))
sns.barplot(x=top_authors.values, y=top_authors.index, palette="viridis")
plt.title("Top 10 Authors with Most Best-Seller Books")
plt.xlabel("Number of Books")
plt.ylabel("Author")

#Ratings distribution on the basis of NO. of counts of books 
plt.figure(figsize=(8,5))
sns.histplot(df['Ratings'], bins=20, kde=True, color="skyblue")
plt.title("Distribution of Book Ratings")
plt.xlabel("Ratings")
plt.ylabel("Count")

# Ratings VS Reviews(to give the social proof of the higher rating books have the more reviews)
plt.figure(figsize=(8,6))
sns.scatterplot(x="Ratings", y="Reviews", data=df, alpha=0.6)
plt.title("Ratings vs Reviews")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.show()










