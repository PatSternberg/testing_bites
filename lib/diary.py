

class Diary():

    def __init__(self) -> None:
        pass

    def make_snippet(self, long_string):
        result = long_string.split()
        return f'{result[0]} {result[1]} {result[2]} {result[3]} {result[4]}...'
    
    def count_words(self, long_string):
        result = long_string.split()
        return len(result)
    
    def estimate_reading_time(self, long_string, wpm):
        string_words = long_string.split()
        return f'Time (in seconds): {(len(string_words)) / wpm}'
    
    def punctuation(self, long_string):
        if long_string[0].isupper() == True and long_string[-1] == '.':
            return 'Verify: Success!'
        else:
            return 'Verify: Failed! This string is missing an initial capital or a final full stop'