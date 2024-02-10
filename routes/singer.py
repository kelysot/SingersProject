from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import Singer, Album, Comment
from database import db
from services.singer import show_singers_service, singer_details_service, add_singer_service

singer_bp = Blueprint('singer', __name__)


@singer_bp.route("/")
def show_singers():
    return show_singers_service()


@singer_bp.route("/singer_details/<singer_id>")
def singer_details(singer_id):
    return singer_details_service(singer_id)


@singer_bp.route("/add_singer/", methods=["POST", "GET"])
def add_singer():
    if request.method == "POST":
        name = request.form.get("name")
        photo = request.form.get("photo")
        genre = request.form.get("genre")
        birth_date = request.form.get("birth_date")
        album1_name = request.form.get("album1_name")
        album1_photo = request.form.get("album1_photo")
        album2_name = request.form.get("album2_name")
        album2_photo = request.form.get("album2_photo")
        album3_name = request.form.get("album3_name")
        album3_photo = request.form.get("album3_photo")
        album4_name = request.form.get("album4_name")
        album4_photo = request.form.get("album4_photo")
        facebook_url = request.form.get("facebook_url")
        instagram_url = request.form.get("instagram_url")
        tiktok_url = request.form.get("tiktok_url")
        active_since = request.form.get("active_since")

        return add_singer_service(name, photo, genre, birth_date, album1_name, album1_photo, album2_name,
                                  album2_photo, album3_name, album3_photo, album4_name, album4_photo,
                                  facebook_url, instagram_url, tiktok_url, active_since)
    else:
        return render_template("add_singer.html")

