import requests
from bs4 import BeautifulSoup

from reddit_thread import RedditThread
from utils import numerize, get_random_user_agent

class RedditCrawler:
    def get_threads(self, subreddit):
        response = requests.get(
            'https://www.reddit.com/r/{}/top/?t=week'.format(subreddit),
            headers=get_random_user_agent()
        ).text

        soup = BeautifulSoup(response, 'html.parser')
        threads = soup.find_all('div', class_='Post')
        print(subreddit.upper() + ' - crawled ' + str(len(threads)) + ' threads')

        result = []
        for thread_soup in threads:
            upvotes = thread_soup.find('div', class_='s1kggl1x-1 dhcHrX').get_text()
            upvotes = numerize(upvotes)
            is_promoted = thread_soup.select_one('.s1p3f9iv-0')
            
            if is_promoted or int(upvotes) < 5000:
                continue

            thread_title = thread_soup.find('h2').get_text()

            thread_url = thread_soup.find('a', class_='SQnoC3ObvgnGjWt90zD9Z').get('href')
            comments_url = thread_soup.find('a', class_="jb5xhx-4").get('href')
            result.append(RedditThread(thread_title, upvotes, subreddit, thread_url, comments_url))

        return result