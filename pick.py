import sqlite3


def pick(con):
    con = sqlite3.connect("movies.sqlite")
    titles = [
        "Placement",
        "Name",
        "Alt. Name",
        "Description",
        "Rating",
        "Genre",
        "Duration",
    ]
    longest_title = max([len(t) for t in titles])

    seenit = True
    wantto = False
    while seenit or not wantto:
        c = con.cursor()
        c.execute(
            "select placement,name,altname,description,rating,genre,duration,seen from movies where seen==0 order by random() limit 1"
        )
        m = c.fetchone()
        for k, v in zip([t.ljust(longest_title) for t in titles], m[:-1]):
            print(f"{k}: {v}")

        answer = ""
        while answer not in ["y", "n"]:
            print("seenit?")
            answer = input(">>> (y/n) ")

        seenit = answer == "y"
        if seenit:
            c.execute("update movies set seen=true where placement==?", (m[0],))
            con.commit()
            continue

        answer = ""
        while answer not in ["y", "n"]:
            print("wantto?")
            answer = input(">>> (y/n) ")
        wantto = answer == "y"
