# Generated by Django 3.1.12 on 2021-08-15 17:39

from django.db import migrations
from django.db.models import Q

from actor.models import Actor
from game.models import Game
from movie.models import Movie, Sport, Documental, Humor, Combo
from music.models import Author, Album, Concert, DVD, Collection
from offer.models import Offer
from serial.models import Serial


def update_image_path(apps, schema_editor):
    movies = Movie.objects.exclude(Q(photo=None) | Q(photo=''))
    for movie in movies:
        movie.photo = "peliculas/" + str(movie.photo)
        movie.save()
    print("Movies OK")
    actors = Actor.objects.exclude(Q(photo=None) | Q(photo=''))
    for actor in actors:
        actor.photo = "actores/" + str(actor.photo)
        actor.save()
    print("Actor OK")
    sports = Sport.objects.exclude(Q(photo=None) | Q(photo=''))
    for sport in sports:
        sport.photo = "deporte/" + str(sport.photo)
        sport.save()
    print("Sport OK")
    documentals = Documental.objects.exclude(Q(photo=None) | Q(photo=''))
    for doc in documentals:
        doc.photo = "documental/" + str(doc.photo)
        doc.save()
    print("Doc OK")
    humors = Humor.objects.exclude(Q(photo=None) | Q(photo=''))
    for humor in humors:
        humor.photo = "humor/" + str(humor.photo)
        humor.save()
    print("Humor OK")
    combos = Combo.objects.exclude(Q(photo=None) | Q(photo=''))
    for combo in combos:
        combo.photo = "combos/" + str(combo.photo)
        combo.save()
    print("Combo OK")
    games = Game.objects.exclude(Q(photo=None) | Q(photo=''))
    for game in games:
        game.photo = "juegos/" + str(game.photo)
        game.save()
    print("Game OK")
    offers = Offer.objects.exclude(Q(photo=None) | Q(photo=''))
    for offer in offers:
        offer.photo = "ofertas/" + str(offer.photo)
        offer.save()
    print("Offer OK")
    series = Serial.objects.exclude(Q(photo=None) | Q(photo=''))
    for serial in series:
        serial.photo = "series/" + str(serial.photo)
        serial.save()
    print("Series OK")
    authors = Author.objects.exclude(Q(photo=None) | Q(photo=''))
    for author in authors:
        author.photo = "discografia/" + str(author.photo)
        author.save()
    print("Disco OK")
    albums = Album.objects.exclude(Q(photo=None) | Q(photo=''))
    for album in albums:
        album.photo = "album/" + str(album.photo)
        album.photo_back = "album/" + str(album.photo_back)
        album.save()
    print("Album OK")
    concerts = Concert.objects.exclude(Q(photo=None) | Q(photo=''))
    for concert in concerts:
        concert.photo = "concierto/" + str(concert.photo)
        concert.save()
    print("Concert OK")
    dvds = DVD.objects.exclude(Q(photo=None) | Q(photo=''))
    for dvd in dvds:
        dvd.photo = "dvd/" + str(dvd.photo)
        dvd.photo_back = "dvd/" + str(dvd.photo_back)
        dvd.save()
    print("DVD OK")
    collections = Collection.objects.exclude(Q(photo=None) | Q(photo=''))
    for collect in collections:
        collect.photo = "coleccion/" + str(collect.photo)
        collect.save()
    print("Collection OK")


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0013_alter_license_expired'),
        ('movie', '0024_auto_20211105_0816'),
        ('game', '0018_auto_20211105_0816'),
        ('music', '0027_auto_20211105_0816'),
        ('offer', '0004_alter_offer_photo'),
        ('serial', '0008_alter_serial_photo'),
    ]

    operations = [
        migrations.RunPython(update_image_path)
    ]
