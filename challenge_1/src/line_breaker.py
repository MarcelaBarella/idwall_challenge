import textwrap

class LineBreaker:
    
    @staticmethod
    def to_lines(text, max_length=40):
        return textwrap.wrap(text, max_length)

    @staticmethod
    def justify(text, max_length=40):
        if len(text) > max_length or not text:
            raise ValueError

        if len(text) == max_length:
            return text

        words = text.split()
        
        while len(text) < max_length:
            for i in range(len(words) - 1):
                words[i] = words[i] + ' '
                text = ' '.join(words)

                if len(text) == max_length:
                    return text

    @staticmethod
    def justify_lines(lines, max_length=40):
        justified_lines = []

        for line in lines:
            justified_lines.append(LineBreaker.justify(line))
        return justified_lines


