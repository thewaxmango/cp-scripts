from difflib import SequenceMatcher

# returns named tuple Match(a, b, size)
# where a, b are starting indices and size is length
LCSubstr = lambda a, b: SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b))