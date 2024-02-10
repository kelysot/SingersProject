from flask import redirect, url_for, flash, session
from models import Comment
from database import db
from .user import get_user_by_id


def add_comment_service(singer_id, comment_text):
    if comment_text:
        user_id = session['user_id']
        current_user = get_user_by_id(user_id)
        comment1 = Comment(text=comment_text, singer_id=singer_id, username=current_user.username, user_id=user_id)
        db.session.add(comment1)
        db.session.commit()
    else:
        flash('Please enter a comment.', 'danger')

    return redirect(url_for('singer.singer_details', singer_id=singer_id))

