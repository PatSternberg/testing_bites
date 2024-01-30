def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char != ' ':
            counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1],reverse=True)[0][0]
    return letter