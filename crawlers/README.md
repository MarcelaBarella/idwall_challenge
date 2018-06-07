# Crawler Challenge
Simple crawler to get thrending threads of Reddit.

## Techonologies 

This solution is written in Python 3.6.5 using the following technologies:
- [scrapy](https://scrapy.org/) - Framework to extract data from websites.
- [argparse](https://docs.python.org/3/library/argparse.html?highlight=argparse) - Built-in library that makes receive arguments easier.
- [halo](https://github.com/ManrajGrover/halo) - Beautiful spinners for terminal.

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
You can extract data of Reddit passing the subrredits that you want to take the number of upvotes, comments link, the name of the subreddit, posts url and their titles.  

To do that, navigate to project folder:
> $ cd crawlers/reddit_crawler

Then call *run.py* passing subreddits desired as parameters:
> $ python run.py --subreddits cats worldnews

It will also generate an *output.json* file with all data crawled.

## Curiosities
- The name of my crawler spider is [*Ungoliant*](http://lotr.wikia.com/wiki/Ungoliant), which is a reference to the fictional spider created by J.R.R Tolkien on his book, The Silmarillion. 
