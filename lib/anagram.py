# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # normalize to lowercase
        self.sorted_word = sorted(self.word)

    def match(self, candidates):
        matches = []
        for candidate in candidates:
            candidate_lower = candidate.lower()
            # Check if candidate is not exactly the same word (case insensitive)
            if candidate_lower != self.word:
                if sorted(candidate_lower) == self.sorted_word:
                    matches.append(candidate)
        return matches
