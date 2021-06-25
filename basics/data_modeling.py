playlist = {
    "title": "jam sessions",
    "author": "woody lucas",
    "songs": [
        {"title": "ocean views", "artist": ["nipsey hussle"], "duration": 3.5},
        {"title": "what it be like", "artist": ["stalley", "nipsey hussle"], "duration": 4.6},
        {"title": "i don't stress", "artist": ["nipsey hussle"], "duration": 4.2},
    ],
}
total_length = 0
for song in playlist["songs"]:
    total_length += song["duration"]

print(total_length)

# dicionaries comprehensions {__:__for__in__}
