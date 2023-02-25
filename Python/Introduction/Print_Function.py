# # Print_Function

# The included code stub will read an integer, n, from STDIN.

# Without using any string methods, try to print the following:
# 123...n


# Note that "..." represents the consecutive values in between.

# Example
# n==5 

# Print the string 12345.

# Constraints
# 1 <= n <= 150

# Output Format:
# Print the list of integers from 1 through n as a string, without spaces.

# Sample Input 0
# 3

# Sample Output 0
# 123

if __name__ == '__main__':
    n = int(input())
    string = ""
    for i in range(n):
        string = string + str(i+1)
    print(string)
    

# Alternate code
 
