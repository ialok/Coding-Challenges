
Language:
	Python

Execute:
	$python DialpadCodingChallenge.py

While I have written doc-string for most methods, this does not adhere to PEP 8
Does not follow the 80,120 column limit for this script

Thought Process:
	This problem translates to generating all possible combinations of the 
	given string, then ignoring the invalid combination(lottery ticket). 
	We can solve it recursively, where we can either break it by 1 char
	or 2 char. 

	Think of it like a recursion tree or any tree where every single node
	is either one digit or two digit and we need to print all root to leaf path
	Ends up with a possible O(n!) solution. 	

            Root   
            /  \
           1    12
          / \   /
         2  23  3
        /
       3

Enhancements:
	Break early. We need not store all possible combinations. 
	For example if a node is larger than acceptable range break and don't check it's children

	Another enhancement can be that we can know the number of possible double digit and single 
	digit numbers in a string. (string of length 7 can have no 2 digit valid ticket). We can
	break on that

	For a input there can be multiple possible valid output. If we just need one, we need not 
	generate all or store all.
