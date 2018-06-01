import argparse

parser = argparse.ArgumentParser(description='Simple text processor')

parser.add_argument('--input', type=argparse.FileType('r'),
    help='File that contains text that will be processed',
    required=True)

parser.add_argument('--action', choices=['break-lines', 'justify'], required=True)
parser.add_argument('--output', type=argparse.FileType('w'))

arguments = parser.parse_args()

if not arguments.output:
    input_extension = arguments.input.name.split('.')[-1]
    input_name = '.'.join(arguments.input.name.split('.')[:-1])
    output_name = input_name + '_output.' + input_extension
    arguments.output = open(output_name, 'w')


input_text = arguments.input.read().replace('\r\n', ' ').replace('\n', ' ')
arguments.input.close()

output_lines = LineBreaker.to_lines(input_text)

if(arguments.action == 'justify'):
    output_lines = LineBreaker.justify_lines(output_lines)
    
output_text = '\n'.join(output_lines)

arguments.output.write(output_text)
arguments.output.close()