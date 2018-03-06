def palindrome(string):
    # Get the length of the string and store it in variable
    n = len(string)
    # Construct an nxn table/matrix consisting of 0's
    # table where we will calculate palindrome substrings in right top corner
    table = [[0 for column in range(n)] for row in range(n)]
    # Populate the diagonal with our word
    for i in range(n):
        table[i][i] = string[i]

    for sub_len in range(2, n+1):
        for row in range(n-sub_len+1):
            # we need to populate table along diagonal first
            # and then work our way to right top corner
            column = row+sub_len-1
            if string[row] == string[column] and sub_len == 2:
                table[row][column] = string[row] + string[column]
            elif string[row] == string[column]:
                table[row][column] = string[row] + table[row+1][column-1] + string[column]
            else:
                if len(table[row][column-1]) > len(table[row+1][column]):
                    table[row][column] = table[row][column-1]
                else:
                    table[row][column] = table[row+1][column]
    return table[0][n-1]


if __name__ == '__main__':
    the_string = str(raw_input('Please enter the word whose largest palindrome sub-sequence you want to find\n'))
    # Call the function that will find the largest sequence with Palindrome
    print('The largest Palindrome sub-sequence for \'%s\' is \'%s\'' % (the_string, palindrome(the_string)))
