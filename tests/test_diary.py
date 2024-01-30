from lib.diary import *

def test_make_snippet():
    diary = Diary()
    result = diary.make_snippet('String should stop about here but it doesn\'t')
    assert result == 'String should stop about here...'

def test_count_words():
    diary = Diary()
    result = diary.count_words('Octopus Cat Dog Lizard Chimp')
    assert result == 5
    result = diary.count_words('')
    assert result == 0

# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text,
# assuming that I can read 200 words a minute.
def test_estimate_reading_time():
    diary = Diary()
    result = diary.estimate_reading_time('A string to be tested', 200)
    assert result == 'Time (in seconds): 0.025'

# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter 
# and ends with a suitable sentence-ending punctuation mark.
def test_punctuation_pass():
    diary = Diary()
    result = diary.punctuation('This string will pass.')
    assert result == 'Verify: Success!'

def test_punctuation_fail():
    diary = Diary()
    result1 = diary.punctuation('This string will fail')
    result2 = diary.punctuation('this string will fail.')
    result3 = diary.punctuation('this string will fail')
    assert result1 == 'Verify: Failed! This string is missing an initial capital or a final full stop'
    assert result2 == 'Verify: Failed! This string is missing an initial capital or a final full stop'
    assert result3 == 'Verify: Failed! This string is missing an initial capital or a final full stop'
