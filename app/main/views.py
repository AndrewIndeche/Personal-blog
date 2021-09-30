from flask import render_template,request,redirect,url_for,abort
from ..models import User, Quote,Quotes, Comments
from ..requests import get_quotes
from flask_login import login_required, current_user
from .. import db,photos
from . import main
from ..models import User,Quote,Comments
from .forms import QuoteForm,EditProfile,CommentForm

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quotes()

    quotes=Quotes.query.all()
    id = Quotes.user_id
    posted_by = User.query.filter_by(id=identification).first()
    user = User.query.filter_by(id=current_user.get_id()).first()

    recent_post = Quotes.query.order_by(desc(Pitches.id)).all()

    return render_template('quotes.html', quote=quotes, posted_by=posted_by, user=user, recent_post=recent_post)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_quote():
    form = QuoteForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_quote_object = Quote(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_quote_object.save_p()
        return redirect(url_for('main.index'))

    return render_template('new_quote.html', form = form)

@main.route('/user/<uname>',methods=['GET','POST'])
@login_required
def profile(uname):
  user = User.query.filter_by(username=uname).first()
  quotes=Quote.query.filter_by(user_id=user.id)
  if user is None:
    abort(404)
  title = f'{user.username}'
  return render_template('profile/profile.html',title=title,user = user,quotes=quotes)

@main.route('/delete_post/<int:quote_id>', methods=['GET','POST'])
@login_required
def delete_post(quote_id):
    quote = Quotes.query.filter_by(id=quote_id).first()

    db.session.delete(quote)
    db.session.commit()
    return redirect(url_for('.home', quote_id=quote.id))

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/updateprofile.html',form =form)

@main.route('/delete_comments/<int:comments_id>', methods=['GET','POST'])
@login_required
def delete_comment(comments_id):
    comments = Comments.query.filter_by(id=comments_id).first()

    db.session.delete(comments)
    db.session.commit()
    return redirect(url_for('.home', comments_id=comments.id))

@main.route('/comments/<int:quote_id>', methods=['GET','POST'])
@login_required
def quote_comments(quote_id):
    comments = Comment.get_comments(quote_id)

    quote = Quote.query.get(quote_id)
    quote_posted_by = quote.user_id
    user = User.query.filter_by(id=quote_posted_by).first()

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.quote_comment.data
        new_comment = Comment(comment=comment, quote_id=quote_id, user_id=current_user.get_id())
        new_comment.save_c()
        return redirect(url_for('main.quote_comments',quote_id = quote_id))

    return render_template('comments.html',form=form, comments=comments, quote = quote, user=user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

    return render_template('new_quote.html',form =form)
