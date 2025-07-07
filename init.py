import bs4
import json
import sqlite3
import urllib.request
import os


def init():
    if not os.path.exists("movies.html"):
        print("Fetching data...")
        rq = urllib.request.Request(
            "https://www.imdb.com/list/ls599119586/",
            method="GET",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.166 Safari/537.36"
            },
        )
        rsp = urllib.request.urlopen(rq)
        with open("movies.html", "wb") as f:
            f.write(rsp.read())

    if not os.path.exists("movies.sqlite"):
        print("Initializing database...")
        with open("movies.html") as f:
            movies = bs4.BeautifulSoup(f.read(),features = "html.parser")

        scripts = movies.find_all("script")
        data = scripts[2]
        moviedata = json.loads(data.text)["itemListElement"]

        con = sqlite3.connect("movies.sqlite")
        con.execute(
            """
            create table if not exists movies (
                placement int primary key,
                name text,
                altname text,
                description text,
                bestrating int,
                worstrating int,
                rating real,
                ratings int,
                genre text,
                duration text,
                seen bool
            )
        """
        )

        for i, j in enumerate(moviedata):
            movie = j["item"]
            con.execute(
                """
                insert or replace into movies 
                (placement,name,altname,description,bestrating,worstrating,rating,ratings,genre,duration,seen)
                values
                (?        ,?   ,?      ,?          ,?         ,?          ,?     ,?      ,?    ,?       ,false)
            """,
                (
                    i + 1,
                    movie["name"],
                    movie.get("alternateName") or "",
                    movie["description"],
                    movie["aggregateRating"]["bestRating"],
                    movie["aggregateRating"]["worstRating"],
                    movie["aggregateRating"]["ratingValue"],
                    movie["aggregateRating"]["ratingCount"],
                    movie["genre"],
                    movie["duration"],
                ),
            )

        con.commit()
