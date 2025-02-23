import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# first have to  CSV file
df = pd.read_csv('2021-2022.csv')
# Split  single column to mult columns
df = df['sb_ca2022_1_csv_v1'].str.split('^', expand=True)
df.columns = ['County_Code', 'District_Code', 'School_Code', 'Filler', 'Test_Year', 'Student_Group_ID', 'Test_Type', 'Total_Tested_Reporting_Level',
'Total_Tested_with_Scores_Reporting_Level', 'Grade', 'Test_ID',
              'Students_Enrolled', 'Students_Tested', 'Mean_Scale_Score',
              'Percentage_Standard_Exceeded', 'Percentage_Standard_Met',
              'Percentage_Standard_Met_Above', 'Percentage_Standard_Nearly_Met',
              'Percentage_Standard_Not_Met', 'Students_with_Scores',
              'Area1_Above_Standard', 'Area1_Near_Standard', 'Area1_Below_Standard',
              'Area2_Above_Standard', 'Area2_Near_Standard', 'Area2_Below_Standard',
              'Area3_Above_Standard', 'Area3_Near_Standard', 'Area3_Below_Standard',
              'Area4_Above_Standard', 'Area4_Near_Standard', 'Area4_Below_Standard',
              'Type_ID']

# try to convert
numeric_columns = ['Percentage_Standard_Exceeded', 'Percentage_Standard_Met','Percentage_Standard_Nearly_Met', 'Percentage_Standard_Not_Met']




for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove header 
df = df[df['Test_Year'] == '2022']

#work on graph now
plt.figure(figsize=(12, 6))
performance_data = df[numeric_columns].mean()
sns.barplot(x=performance_data.index, y=performance_data.values)
plt.title('Average Performance Distribution (2021-2022)')
plt.xticks(rotation=45)
plt.ylabel('Percentage')
plt.tight_layout()
plt.show()


df = df[(df['Test_Year'] == '2022') & (df['Grade'] != 13)]

plt.style.use('seaborn-v0_8')
plt.figure(figsize=(15, 8))
performance_cols = ['Percentage_Standard_Exceeded', 'Percentage_Standard_Met',
                   'Percentage_Standard_Nearly_Met', 'Percentage_Standard_Not_Met']

# Calculating mean
grade_performance = df.groupby('Grade')[performance_cols].mean()
colors = ['#2ecc71', '#3498db', '#f1c40f', '#e74c3c']
ax = grade_performance.plot(kind='bar', stacked=True, color=colors, width=0.8)
# Customizing, look nice
plt.title('Student Performance Standards Distribution by Grade Level (2022)', pad=20, size=14)
plt.xlabel('Grade Level', size=12)
plt.ylabel('Percentage of Students', size=12)
legend_labels = ['Standard Exceeded', 'Standard Met', 
                'Standard Nearly Met', 'Standard Not Met']
plt.legend(legend_labels, title='Performance Levels', 
          bbox_to_anchor=(1.05, 1), loc='upper left')
# dont forget labels
for c in ax.containers:
    ax.bar_label(c, fmt='%.1f%%', label_type='center')

plt.tight_layout()
plt.show()
# summary 
print("\
Performance Summary Statistics:")
for category in numeric_columns:
    print(f"\
{category.replace('Percentage_', '').replace('_', ' ')}:")
    print(f"Mean: {df[category].mean():.1f}%")
    print(f"Median: {df[category].median():.1f}%")
    print(f"Standard Deviation: {df[category].std():.1f}%")