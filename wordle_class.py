class Word:
    def __init__(self):
        self.answer = {}
        self.out_set = set()
        self.in_set = set()
        self.guess_count = 0
    
    def accept_response(self, response):
        for i in response:
            color = response[i]['color']
            letter = response[i]['letter']
            if color == 'green':
                self.answer[i] = letter
            if color == 'yellow':
                self.in_set.add(letter)
            if color == 'black':
                self.out_set.add(letter)
        self.guess_count += 1