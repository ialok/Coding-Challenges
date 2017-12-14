#!/usr/bin/env python

"""
Winning Ticket!

Your favorite uncle, Morty, is crazy about the lottery and even crazier about how he picks his 'lucky' numbers. And even though his 'never fail' strategy has yet to succeed, Uncle Morty doesn't let that get him down.

Every week he searches through the Sunday newspaper to find a string of digits that might be potential lottery picks. But this week the newspaper has moved to a new electronic format, and instead of a comfortable pile of papers, Uncle Morty receives a text file with the stories.

Help your Uncle find his lotto picks. Given a large series of number strings, return each that might be suitable for a lottery ticket pick. Note that a valid lottery ticket must have 7 unique numbers between 1 and 59, digits must be used in order, and every digit must be used exactly once.

For example, given the following strings:

[ '569815571556', '4938532894754', '1234567', '472844278465445']

Your function should return:

4938532894754 -> 49 38 53 28 9 47 54
1234567 -> 1 2 3 4 5 6 7
"""

TICKET_SIZE = 7
MAX = 59
MIN = 1

def _generate_possible_combinations(lottery_ticket, low, high, combination, all_combinations):
  """
  Private method behind the magic. Generate a recursion tree, each time choosing either 1 or 2 digits from the numeric string
  
  123  ->   Root   
            /  \
           1    12
          / \   /
         2  23 3
        /
       3
  Permutes and finds all possible combinations(valid/invalid) that can be made from choosing 
  either only 1, only 2 or (1 and 2) characters from numeric string
  
  Args:
    lottery_ticket (str): input string made of numbers
    low (int): starting index of the input sring. Each time we increase by +1 or +2 depending on char choice
    hight (int): length of string
    combination (list(str)): temporary list that is used to hold the permutation state across each recursive call
    all_combinations (list(list(str))): 
    
  Returns:
    Nothing: Since python mutable method params persists across each call, we use this to return 
    all the possible combinations from the input string
  """
  
  if low == high:
    all_combinations.append(combination)
  else:
    if low<high:
      _generate_possible_combinations(lottery_ticket, low+1, high, combination+[lottery_ticket[low:low+1]], all_combinations)
      if high-low >= 2:
        _generate_possible_combinations(lottery_ticket, low+2, high, combination+[lottery_ticket[low:low+2]], all_combinations)


def _find_valid_combination(possible_combinations):
  """
  Private method that takes a list of possible lotto ticket number(s) and returns
  a list containing the valid tickets
  
  Args:
    possible_combinations (list(list(str))): list made of lists of strings, each sublist may denote
                                             a possible(valid/invalid) lotto ticket
  Returns:
    list(list(str)): valid lotto tickets. Empty list if no valid lotto ticket was found
  """
  
  if possible_combinations is None:
    return []
  
  def is_valid_combination(combination):
    if len(combination) != TICKET_SIZE:
      return False
    if len(combination) != len(set(combination)):
      return False
    if any(number.startswith('0') for number in combination):
      return False
    if any(int(number) > MAX for number in combination):
      return False
    
    return True
    
  valid_combinations = []
  for combination in possible_combinations:
    if is_valid_combination(combination):
      valid_combinations.append(combination)
  return valid_combinations
    
def _pretty_print(valid_ticket):
  """
  Private method that takes a list containing valid lottery ticket numbers and pretty print it
  valid_ticket = ['1', '2', '3', '4', '50', '6', '7']
  Output: 12345067 -> 1 2 3 4 50 6 7
  
  Args:
    valid_ticket (list(str)): list of strings denoting a valid lotto combination
  Returns:
    Nothing: displays the text on terminal
  """
  
  print "".join(valid_ticket), "->", " ".join(valid_ticket) 


def find_winning_combination(numeric_string):
  """
  This method returns generates valid lottery ticket(s) from a string of number.
  Adheres to the constraint(Range, Length) of the game.
  
  Args:
    numeric_string (str): input string that may consist of possible lotto combination
  Returns:
    list: all possible valid lottery tickets generated from the numberic string.
          Empty List if no valid ticket could be generated
  """
  
  if numeric_string is None or len(numeric_string) == 0:
    return []
    
  possible_combinations = []
  _generate_possible_combinations(numeric_string, 0, len(numeric_string), [], possible_combinations)
  return _find_valid_combination(possible_combinations)


if __name__ == "__main__":
  input_strings = [ "569815571556", "", "4938532894754", "1234567", "12345067", "12314567", "472844278465445"]
  
  for numeric_string in input_strings:
    for ticket in find_winning_combination(numeric_string):
      _pretty_print(ticket)
    if numeric_string:
        print
