import pandas as pd 
import matplotlib.pyplot as plt

# Load the Excel file named GITHUBEXCELCSV from documents folder 
excel=pd.read_csv('~/Documents/Python/GITHUBEXCELCSV.csv')


# Group of words to search for red flags
red_flags = ["LEONGRILL" ]

# Group of words to search for green flags
green_flags = ["ECS","CBSL" ]

# Search words into regular expression patterns without spaces
red_flags_pattern = '|'.join(fr'\b{word}\b' for word in red_flags)
green_flags_pattern = '|'.join(fr'\b{word}\b' for word in green_flags)

# Classify words as "RED FLAGS" or "GREEN FLAGS" and count the occurrences
excel['red_flags_count'] = excel['Narration'].str.count(red_flags_pattern)
excel['green_flags_count'] = excel['Narration'].str.count(green_flags_pattern)

# Store the counts in variables
red_flags_count = excel['red_flags_count'].sum()
green_flags_count = excel['green_flags_count'].sum()

 

# Sum the entries in the "DEBIT AMOUNT" column for "RED FLAGS" and "GREEN FLAGS"
red_flags_sum = excel.loc[excel['red_flags_count'] > 0, 'Debit Amount'].sum()
green_flags_sum = excel.loc[excel['green_flags_count'] > 0, 'Debit Amount'].sum()

# Display the results

print("Red Flags Count:", red_flags_count)
print("Red Flags Sum:", red_flags_sum)
print("Green Flags Count:", green_flags_count)
print("Green Flags Sum:", green_flags_sum)



# Plotting bar graph
fig, ax = plt.subplots()

# Bar heights
red_flags_data = [red_flags_count, red_flags_sum]
green_flags_data = [green_flags_count, green_flags_sum]

# Bar positions
bar_positions = range(2)

# Bar labels
bar_labels = ['Count', 'Sum']

# Plotting red flags
ax.bar([pos - 0.2 for pos in bar_positions], red_flags_data, width=0.4, label='Red Flags', color='red')
# Plotting green flags
ax.bar([pos + 0.2 for pos in bar_positions], green_flags_data, width=0.4, label='Green Flags', color='green')

# Adding labels and title
ax.set_xticks(bar_positions)
ax.set_xticklabels(bar_labels)
ax.set_ylabel('Value')
ax.set_title('Red and Green Flags Analysis')

# Adding legend
ax.legend()

# Show the plot
plt.show()
