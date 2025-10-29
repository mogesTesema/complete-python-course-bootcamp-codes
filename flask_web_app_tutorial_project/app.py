from flask import Flask,render_template
app = Flask(__name__)

posts = {
    0:{
        'title':'hello,world',
        'content':'This is my first blog post!'
    }
}


@app.route("/")
def home():
    return "<h1>hello,Flask world</h1>"

@app.route("/post/<int:post_id>") # /post/0 <int:post_id> is place holder for post id that are coming from frontend.and
def posted(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template("404.html",message=f'A post with id{post_id} was not found.')
    return render_template("post.html",post=post)

if __name__ == "__main__":
    app.run(debug=True )