from flask import render_template,request,redirect,url_for
from ..models import User, Quotes, Comments

@app.route('/')
def index(id):

    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quote(id)

    quotes=Quotes.query.all()
    id = Quotes.user_id
    posted_by = User.query.filter_by(id=identification).first()
    user = User.query.filter_by(id=current_user.get_id()).first()

    recent_post = Quotes.query.order_by(desc(Quotes.id)).all()

    return render_template('quotes.html', quote=quote, posted_by=posted_by, user=user, recent_post=recent_post)


    return render_template('index.html')
