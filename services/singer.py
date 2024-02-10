from datetime import datetime

from flask import render_template, redirect
from models import Singer, Album, Comment
from database import db


def show_singers_service():
    singers = Singer.query.all()
    albums = Album.query.all()
    return render_template("singers.html", singers=singers, albums=albums)


def singer_details_service(singer_id):
    singer1 = Singer.query.get(singer_id)
    albums = Album.query.filter_by(singer_id=singer_id).all()
    comments = Comment.query.filter_by(singer_id=singer_id).all()
    return render_template("singer_details.html", singer=singer1, albums=albums, comments=comments)


def add_singer_service(name, photo, genre, birth_date, album1_name, album1_photo, album2_name,
                       album2_photo, album3_name, album3_photo, album4_name, album4_photo,
                       facebook_url, instagram_url, tiktok_url, active_since):
    singer_obj = Singer(name=name, photo=photo, genre=genre, birth_date=birth_date, facebook_url=facebook_url,
                        instagram_url=instagram_url, tiktok_url=tiktok_url, active_since=active_since)

    db.session.add(singer_obj)
    db.session.commit()

    album1_obj = Album(title=album1_name, photo=album1_photo, singer_id=singer_obj.id)
    album2_obj = Album(title=album2_name, photo=album2_photo, singer_id=singer_obj.id)
    album3_obj = Album(title=album3_name, photo=album3_photo, singer_id=singer_obj.id)
    album4_obj = Album(title=album4_name, photo=album4_photo, singer_id=singer_obj.id)
    db.session.add(album1_obj)
    db.session.add(album2_obj)
    db.session.add(album3_obj)
    db.session.add(album4_obj)
    db.session.commit()
    return redirect("/")
