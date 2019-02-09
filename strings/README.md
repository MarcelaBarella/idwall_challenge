# Strings Challenge
Simple console line text formatter that has capability to break text into lines or justify it if you want it.

## Techonologies 

This solution is written in Python 3.6.5 using the following technologies:
- [unittest](https://docs.python.org/3/library/unittest.html) - Built-in and most used test framework for python.
- [argparse](https://docs.python.org/3/library/argparse.html?highlight=argparse) - Built-in library that makes receive arguments easier.
- [assertpy](https://github.com/ActivisionGameScience/assertpy) - Simple library that beautifies assertions on tests.

## Running Solution
The two ways that you can run this solution is locally or using docker, for both cases follow the given steps:

### Locally
In order to run this solution script you must have Python 3.6, PIP and this project dependencies installed. To install Python and PIP, please refeer to their official documentation.

To install all dependencies, simple run:
> $ pip install -r requirements.txt

### With Docker
Also this solution was built using docker. You will only need docker installed (please refeer to [official docker docs](https://docs.docker.com/install/)). If you want to use docker in order to prevent install anything in your machine, you can use the Dockerfile and docker-compose.yml of this project.

This solution image contains only the minimal necessary to solve this challenge. Because of that I choose to use Python3.6 image with Linux Alpine 3.7.

To need this image, go to root of this project:
> $ cd ../

Build the image, this will already download all dependencies listed on requirements.txt
> $ docker-compose build

Run the container
> $ docker-compose up

To access the container bash, you must list all containers running and get your container id:
> $ docker ps

Then connect to this terminal:
> $ docker exec -it 5324 ash

## Usage
You can only break-lines or justify them to. To do that simple execute the command below with necessary arguments:
> $ python run.py

You can see a full list of accepted arguments by running:
> $ python run.py -h

### Accepted Arguments
All bold arguments with (*) are mandatory:

- **--input***: path of a valid and accessible file that will be processed.
- **--action {break-lines, justify}***: what action do you want to do .
- --output: desired name of yout output file. If this argument is ommited, the output will be input file name concatenated with _ouput sufix. Example: *some_file_output.txt*.
 - --line-length: Specifies the ammount of characters per line of the output file. Default is 40 characters.

### Examples of usage
**Justify input content:**
> $ python run.py --input file_name.extension --action justify


**Justify input content to specific output file:**
> $ python run.py --input file_name.extension --action justify --output desired_output_name.extension
