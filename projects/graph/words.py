"""
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
"""

from graph import Graph

def transform_words(beginning_word, end_word):
  # initialize graph
  word_graph = Graph()
  # Check edge case
  if len(beginning_word) != len(end_word):
    return None
  else:
  # get union of both words, from which we'll use to determione valid words
    valid_letters = set(beginning_word) | set(end_word)
  # open file and make set of all words of same length
    text_file = open('words.txt')
    valid_words = [word.lower() for word in text_file.read().split() if len(word) == len(beginning_word)]

  # add vertex for each word
    for word in valid_words:
        word_graph.add_vertex(word)
  # add edge if there's a one letter difference
    for word in valid_words:
        for reviewed in valid_words:
            if word != reviewed and sum(a!=b for a,b in zip(word, reviewed)) == 1:
                word_graph.add_edge(word, reviewed)
  # return BFS
    return word_graph.bfs(beginning_word, end_word)
        
print(transform_words("sail", "boat"))
print(transform_words("hit", "cog"))
print(transform_words("hungry", "happy"))