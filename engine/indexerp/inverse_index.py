class InvertedIndex:
    def __init__(self, path_) -> None:
        self.file_path = path_
        self.line_count = 1
        self.file_text = ''
        self.lines = []


    def set_file_text(self):
        """Store the text of the current file in file_text"""
        self.curr_file = open(self.file_path, 'r')
        self.file_text = self.curr_file.read()
        self.curr_file.close()


    def set_line_count(self):
        """Store the amount of lines inside the current file in line_count"""
        for line in self.file_text:
            if line == '\n':
                self.line_count += 1
    
    def store_lines(self):
        """Store each line of the file as an element of a list"""
        self.curr_file = open(self.file_path, 'r')
        for i in range(self.line_count):
            self.lines.append(self.curr_file.readline())
        self.curr_file.close()

    def set_index(self):
        """create inverted index"""
        self.ii = {}

        for i in range(self.line_count):
            for item in self.lines:
                if item not in self.ii:
                    self.ii[item] = []
                if item in self.ii:
                    self.ii[item].append(i+1) 
    
ii = InvertedIndex('/home/michael/dev/search-engine/test_file.txt')
ii.set_file_text()
ii.set_line_count()
ii.store_lines()
ii.set_index()
# print(ii.file_text)
# print(ii.lines)
print(ii.ii)


    
            
