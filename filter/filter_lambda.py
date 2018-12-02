# By Krishnan Parameswaran

# Filter vowels

def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if (letter in vowels):
        return True
    else:
        return False

print('\nFiltering vowels using filter() method')
chars = ['a', 'b', 'c', 'd', 'e', 'f']
filteredChars = filter(filterVowels, chars)
print(f'The filtered letters are {list(filteredChars)}')

print('\nFiltering numbers using filter() and lambda')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filteredNums = filter(lambda x:(x % 2 == 0), nums)
print(f'The filtered numbers are {list(filteredNums)}')
