import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix.csv")

print("Columns in dataset:")
print(df.columns.tolist())

# -----------------------------
# Plot 1: Line plot (Titles per release year)
# -----------------------------
year_counts = (
    df["release year"]
    .dropna()
    .astype(int)
    .value_counts()
    .sort_index()
)

fig1, ax1 = plt.subplots()
ax1.plot(year_counts.index, year_counts.values)

ax1.set_xlabel("Release Year")
ax1.set_ylabel("Number of Titles")
ax1.set_title("Netflix Titles Released per Year")
plt.tight_layout()

# -----------------------------
# Plot 2: Horizontal bar chart (Top 10 ratings)
# -----------------------------
rating_counts = df["rating"].value_counts().head(10)

fig2, ax2 = plt.subplots()
ax2.barh(rating_counts.index.astype(str), rating_counts.values)

ax2.set_xlabel("Count")
ax2.set_ylabel("Rating")
ax2.set_title("Top 10 Netflix Content Ratings")
plt.tight_layout()

# -----------------------------
# Plot 3: Scatter plot (User rating score vs rating size)
# -----------------------------
scatter_df = df[["user rating score", "user rating size"]].dropna()

fig3, ax3 = plt.subplots()
ax3.scatter(
    scatter_df["user rating size"],
    scatter_df["user rating score"]
)

ax3.set_xlabel("User Rating Size")
ax3.set_ylabel("User Rating Score")
ax3.set_title("User Rating Score vs Rating Size")
plt.tight_layout()

# Show all plots
plt.show()
