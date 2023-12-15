fig1, ax1 = plt.subplots(figsize=(10, 4), dpi=100)

# Improved color scheme
colors = ['skyblue', 'salmon', 'lightgreen']
barh = plt.barh(y=new_sum.index, width=new_sum.values, height=0.2, color=colors)

plt.yticks(fontsize=13)
plt.xlabel("Pounds", size=12)
plt.title("Total Releases Petroleum, 2022", size=15)
plt.xlim(0, max(new_sum.values) + 5000000)

# Add gridlines
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Formatting bar labels
for bar in barh:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
             f'{bar.get_width():,.0f}', 
             va='center', ha='left')

# Styling titles and labels
plt.ylabel("Categories", size=12)
plt.xticks(rotation=45, fontsize=10)

# Hide the right and top spines
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

# Save the figure
plt.savefig("png_output/Fig4_prettier.png")
plt.show()