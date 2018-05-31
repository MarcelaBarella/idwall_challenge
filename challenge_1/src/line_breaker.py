import textwrap

class LineBreaker:
    
    @staticmethod
    def to_lines(text, max_length=40):
        return textwrap.wrap(text, max_length)

    @staticmethod
    def justify(text, max_length=40):
        if len(text) >  max_length or not text:
            raise ValueError

    @staticmethod
    def justify_lines(lines, max_length=40):
        pass