import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# I should start with reading the file
df_2014 = pd.read_csv('educationData-2014.csv')  # Skip the empty row

# now convert numeric columns
numeric_columns = ['Grade', 'Mean Scale Score', 'Percentage Standard Exceeded', 
                  'Percentage Standard Met', 'Percentage Standard Nearly Met', 
                  'Percentage Standard Not Met']

for col in numeric_columns:
    if col in df_2014.columns:
        df_2014[col] = pd.to_numeric(df_2014[col], errors ='coerce')

df_2014 = df_2014[df_2014['Grade'].notna()] #should filter data

 

plt.style.use('seaborn-v0_8')#using seaborn for style
plt.figure(figsize = (15, 8))

performance_cols = ['Percentage Standard Exceeded', 'Percentage Standard Met',
                'Percentage Standard Nearly Met', 'Percentage Standard Not Met']

grade_performance = df_2014.groupby('Grade')[performance_cols].mean() #1st calculation is mean based on grade performnce

colors = ['#2ecc71', '#3498db', '#f1c40f', '#e74c3c']
ax = grade_performance.plot(kind ='bar', stacked = True, color = colors, width = 0.8)

# Custom plot
plt.title('Student Performance Standards Distribution by Grade Level (2014)', pad = 20, size = 14)
plt.xlabel('Grade Level', size = 12)
plt.ylabel('Percentage of Students', size = 12)

#  legend
legend_labels = ['Standard Exceeded', 'Standard Met', 
        'Standard Nearly Met', 'Standard Not Met']
plt.legend(legend_labels, title = 'Performance Levels', 
          bbox_to_anchor = (1.05, 1), loc ='upper left')

for c in ax.containers:
    # Add labels
    ax.bar_label(c, fmt='%.1f%%', label_type='center')

 
plt.tight_layout()
plt.show()

   









# Print summary statistics
print("\
Mean Scale Score by Grade Level (2014):")
summary = df_2014.groupby('Grade')['Mean Scale Score'].agg(['mean', 'count', 'std']).round(2)
print(summary)