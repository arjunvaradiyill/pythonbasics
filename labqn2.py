# Number of rows
rows = 5

# Loop through each row
for i in range(1, rows + 1):
    # Initialize an empty string for each row
    line = ''
    
    # Loop to append characters from 'A' to the ith character
    for j in range(i):
        line += chr(65 + j)
    
    # Print the current row
    print(line)
