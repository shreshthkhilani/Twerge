# From the python package flask, import the "Flask" constructor, and request library
from flask import Flask, request, render_template, url_for
import tweepy

# Create an app from the Flask constructor
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('twerge_home.html')

auth = tweepy.OAuthHandler("W0QmxWkFn04vUQKCVll1Q", "2K0GaTvDEFYnKKjxg2b2VWUZblblONIFOaXeVU7K9ZE")
auth.set_access_token("81589905-7SuMFGvkWuP4S0oJaN012Fqubp3yKwu2tWWDR3nM", "TZUx2MHO1mlJzPE30tdbB8owEsg4ZnqkY5jaZ8d3vvo")
user = tweepy.API(auth)
    
@app.route('/combined', methods=['POST'])
def recieve_form():
    tweet_a = user.user_timeline(request.form['one'])[0].text
    tweet_b = user.user_timeline(request.form['two'])[0].text
    new_tweet = tweet_a[:65] + " " + tweet_b[:65] # merge tweet_a and tweet_b
    print new_tweet
    # if twitter handles don't exist, return failiure
    return render_template('twerge_combined.html', new_tweet=new_tweet)

@app.route('/combined/done', methods=['POST'])
def form_done():
    # user.update_status(request.form['twerge'])
    return render_template('twerge_complete.html', new_tweet=request.form['twerge'])

# When file is executed, listen on the default port
if __name__ == "__main__":
    app.run()