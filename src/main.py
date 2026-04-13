"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
from recommender import load_songs, recommend_songs

# resolve path relative to this file so it works from any directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "songs.csv")


def main() -> None:
    songs = load_songs(CSV_PATH)

    # Starter example profile
    user_prefs = {
        "favorite_genre":        "pop",
        "favorite_mood":         ["happy"],
        "target_energy":         0.8,
        "target_valence":        0.8,
        "target_acousticness":   0.2,
        "target_tempo_bpm":      120,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  Top 5 Recommendations")
    print(f"  Profile: {user_prefs['favorite_genre']} / {user_prefs['favorite_mood']} / energy {user_prefs['target_energy']}")
    print("=" * 50)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}")
        print(f"    Score: {score:.2f}")
        print("    Why:")
        for reason in explanation.split(" | "):
            print(f"      - {reason}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
