'''
Created on May 27, 2017

@author: ayush
    A uniform string is a string consisting of a single character repeated zero or more times. For example, ccc and a are uniform strings, but bcb and cd are not (i.e., they consist of more than one distinct character).

Given a string, , let be the set of weights for all possible uniform substrings (contiguous) of string . You have to answer queries, where each query consists of a single integer, . For each query, print Yes on a new line if ; otherwise, print No instead.

Note: The symbol denotes that is an element of set .

Input Format

The first line contains a string denoting (the original string).
The second line contains an integer denoting (the number of queries).
Each line of the subsequent lines contains an integer denoting (the weight of a uniform subtring of that may or may not exist).

Constraints

    will only contain lowercase English letters.

Output Format

Print lines. For each query, print Yes on a new line if ; otherwise, print No instead.

Sample Input 0

abccddde
6
1
3
12
5
9
10

Sample Output 0

Yes
Yes
Yes
Yes
No
No

Explanation 0

The weights of every possible uniform substring in the string abccddde are shown below:

image

We print Yes on the first four lines because the first four queries match weights of uniform substrings of . We print No for the last two queries because there are no uniform substrings in that have those weights.

Note that while de is a substring of that would have a weight of , it is not a uniform substring.

Note that we are only dealing with contiguous substrings. So ccc is not a substring of the string ccxxc.
'''
#we can apply the given method since it is given they are continuous substrings
def weighted_string(st,x):
    uniform_sub_lengths = set()
    prev_letter = ""
    weight = 0

    for letter in st:
        if letter == prev_letter:
            weight += ord(letter) - 96
        else:
            prev_letter = letter
            weight = ord(letter) - 96
        uniform_sub_lengths.add(weight)
        
    if x in uniform_sub_lengths:
        print('Yes')
    else:
        print('No')

weighted_string('abccddde',6)
weighted_string('abccddde',10)