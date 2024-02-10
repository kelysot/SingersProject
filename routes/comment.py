from flask import Blueprint, render_template, request,session, redirect, url_for, flash
from services.comment import add_comment_service

comment_bp = Blueprint('comment', __name__)


@comment_bp.route('/singer/<int:singer_id>/add_comment', methods=['POST', 'GET'])
def add_comment(singer_id):
    user_id = session.get('user_id')

    if user_id is None:
        # User is not logged in - redirect to the login page.
        flash('To comment you need to login to the website.', 'danger')
        return redirect(url_for('user.login'))

    if request.method == "POST":
        comment_text = request.form.get('comment_text')
        return add_comment_service(singer_id, comment_text)
    else:
        return render_template("singer_details.html", singer_id=singer_id)
