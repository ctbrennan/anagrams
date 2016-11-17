Uses python3
Design choices:
My algorithm works by making input words lowercase, and them sorting them alphabetically. Then, we add a mapping from the sorted word to a sorted tuple of all the input words which have the same sorted word (they're all anagrams of eachother). Returning the anagrams for a given input is thus a matter of sorting the input string, hashing it, and returning the words in the tuple, which are already sorted. This means performance in the offline step is okay, while the online step is pretty good (see actual analysis below).

Another approach I briefly considered was adding a mapping from every permutation of a word to the actual input word. For example: an input word of 'abc' from the text file would mean that the word hashtable would add the following mappings:
'abc' -> ('abc')
'bac' -> ('abc')
'cab' -> ('abc')
'cba' -> ('abc')
'acb' -> ('abc')
'bca' -> ('abc')
This would make the online step happen in constant time (just hash in input word and return the values found there), but would make the offline step happen in O(N* n!) time, where N is the number of words, and n is the length of each word. I decided to avoid this factorial/exponential solution, because this could potentially be incredibly slow for long words. I ran this with a dictionary of ~500k words and it was still running after two minutes before I stopped execution. This would also take O(N * n!) space, as there is an entry for every permutation of each input word. 

Offline:
define N as the number of words, n as the length of the words
the offline portion runs in O(N*(n*log(n) + N*log(N))) time
for each word, we sort the word, and hash it (hashing takes constant time).
After adding the word to the bucket, we have to pull the words currently in the bucket for that sorted word, and sort that list. However, if most of the words in the dictionary are not anagrams (resonable assumption, probably), then the sorting within each bucket that leads to the O(N*log*(N)) bound on adding a word to the bucket is unlikely to impact performance. 

Online:
Define n as the length of the input word
The program runs in O(n*log(n)) time.
The n*log(n) comes from sorting the word, and we ignore the constant from hashing the word. The tuple that is returned is already sorted, so we just return those words in the order we have them stored. Note: if we consider adding spaces between the x number of words in the tuple, this takes O(n*log(n) + x) time.

If we have N words in our input dictionary, our program uses O(N) space in memory. This is because we store each word once in the hashtable.

Extra credit:
Instead of using one hashtable, we could have a different hashtable for words that when sorted, start with certain ranges of letters. For example, a hashtable for sorted words that start with letters in the range [a, f], [g, l], [l, z]. We would have to figure out how to make the ranges to balance the number of words in each separate hashtable. Then, during the online step, we would pull the correct hashtable (stored as JSON) from a PostreSQL database, and perform the same steps from there.