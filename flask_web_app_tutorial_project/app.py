from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

posts = {
    0:{ 'post_id':0,
        'title':'hello,world',
        'content':'This is my first blog post!'
    }
}


@app.route("/")
def home():
    discribe = "this is awesome Flask web app for education purpose"
    return render_template("home.html",description=discribe)

@app.route("/post/<int:post_id>") # /post/0 <int:post_id> is place holder for post id that are coming from frontend.
def posted(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template("404.html",message=f'A post with id {post_id} was not found.')
    return render_template("post.html",post=post)

@app.route("/post/form")
def form():
    return render_template("create.jinja2")

#127.0.0.1:5000/post/create?title=something&content=something_else
@app.route("/post/create", methods=["GET","POST"])
def create():
    # title = request.args.get("title")
    # content = request.args.get("content")
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        post_id = len(posts)
        posts[post_id] = {"post_id":post_id, "title":title, "content":content}
        return redirect(url_for("posted",post_id=post_id))
    return render_template("create.jinja2")

if __name__ == "__main__":
    app.run(debug=True )