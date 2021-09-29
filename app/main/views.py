from flask import render_template,request,redirect,url_for

@app.route('/')
def index(id):

    '''
    View root page function that returns the index page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('index.html')
