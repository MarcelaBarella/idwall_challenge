
def json_formater(json):
    upvotes = "upvotes:" + json["upvote"] + "\n"
    subreddit = "subreddit:" + json["subreddit"] + "\n"
    #with the the link fot the title
    title = "upvotes:" + json["upvote"] + "\n"


def subreddits_limiter(subreddits):
    subreddits = subreddits.split(';')
    
    if len(subreddits) > 5:
        return True
         
