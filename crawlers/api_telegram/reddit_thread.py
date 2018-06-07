class RedditThread:
    def __init__(self, title, upvotes, subreddit, url, comments_url):
        BASE_URL = 'https://www.reddit.com'

        self.title = title
        self.upvotes = int(upvotes)
        self.subreddit = subreddit
        self.url = BASE_URL + url
        self.comments_url = BASE_URL + comments_url

    def to_markdown(self):
        result = "[" + self.title +  "]("  + self.url + ") - " + str(self.upvotes) + " upvotes  \n"
        result += "*subreddit:* " + self.subreddit + "  \n"
        result += "[Go to comments](" + self.comments_url + ")  \n"
        return result