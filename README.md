# File Tracking
##### Coding Task: File Tracking for in-toto

Given two "snapshots" of a file structure -- 'before' and 'after' -- determine which files have been added, which have been removed, which have been modified, and which have remained unchanged.

The 'before' and 'after' metadata is provided as Python dictionaries.  The keys in the dictionary are filepaths, and the values are hexadecimal strings representing the hashes of the corresponding files.  The output should be in the form of four lists of filepaths: 'unchanged', 'modified', 'added', and 'removed'.

Your code should be readable and roughly follow these lab guidelines.  Don't worry too much about style, but write code that is easy to read: provide comments that explain why things were done one way or another -- comments that focus on 'why' more than 'what'.  I'll judge the code based on whether or not it works for some sample sets, and whether or not it makes sense, is well organized, and is well commented.  You can send me the code in response, or provide it on GitHub.

Input Example:

before = {

  'one.tgz': '1234567890abcdef',

  'foo/two.tgz': '0000001111112222',

  'three.txt': '1111222233334444'

  'bar/bat/four.tgz': '6677889900112233'

}

after = {

  'five.txt': '5555555555555555',

  'one.tgz': '1234567890abcdef',

  'foo/two.tgz': 'ffffffffffffffff',

  'bar/bat/four.tgz': '6677889900112233',

  'baz/six.tgz': '6666666666666666'

}

Output Example:

unchanged = ['one.tgz', 'bar/bat/four.tgz']

modified = ['foo/two.tgz']

added = ['five.txt', 'baz/six.tgz']

removed = ['three.txt']

Bonus : You can write your code to optionally take a before and an after archive (zip, tar.gz, etc. -- your choice) and calculate the 'before' and 'after' metadata yourself by calculating hashes of the files provided.
