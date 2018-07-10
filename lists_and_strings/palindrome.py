# https://adriann.github.io/programming_problems.html
# Write a function that tests whether a string is a palindrome.

class Palindrome():
    
    def _check_word_len_even(self, word):
        if len(word) % 2 == 0:
            return True
        else:
            return False

    def check_palindrome(self, word):
        '''
        determines if a given word is a Palindrome

        Args:
            a string

        Return:
            a boolean

        '''
        if self._check_word_len_even(word):
            for i in range(0, int((len(word)/ 2 ) - 1)):
                print(word[i], word[-(i + 1)])
                if word[i] != word[-(i + 1)]:
                    return False
        else:
            for i in range(0, int((len(word) - 1) / 2)):
                print(word[i], word[-(i + 1)])
                if word[i] != word[-(i + 1)]:
                    return False
        return True

