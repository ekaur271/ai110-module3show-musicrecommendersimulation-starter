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


def print_recommendations(label: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Print top k recommendations for a given profile in a formatted layout."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print("\n" + "=" * 55)
    print(f"  Profile: {label}")
    print(f"  Genre: {user_prefs['favorite_genre']}  |  Mood: {user_prefs['favorite_mood']}")
    print(f"  Energy: {user_prefs['target_energy']}  |  Valence: {user_prefs['target_valence']}  |  Tempo: {user_prefs['target_tempo_bpm']} BPM")
    print("=" * 55)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}")
        print(f"    Score: {score:.2f}")
        print("    Why:")
        for reason in explanation.split(" | "):
            print(f"      - {reason}")

    print("\n" + "=" * 55)


def main() -> None:
    songs = load_songs(CSV_PATH)

    # --- Profile 1: High-Energy Pop ---
    high_energy_pop = {
        "favorite_genre":      "pop",
        "favorite_mood":       ["happy", "energized"],
        "target_energy":       0.90,
        "target_valence":      0.85,
        "target_acousticness": 0.05,
        "target_tempo_bpm":    130,
    }

    # --- Profile 2: Chill Lofi ---
    chill_lofi = {
        "favorite_genre":      "lofi",
        "favorite_mood":       ["chill", "focused"],
        "target_energy":       0.38,
        "target_valence":      0.58,
        "target_acousticness": 0.80,
        "target_tempo_bpm":    78,
    }

    # --- Profile 3: Deep Intense Rock ---
    intense_rock = {
        "favorite_genre":      "rock",
        "favorite_mood":       ["intense", "angry"],
        "target_energy":       0.95,
        "target_valence":      0.30,
        "target_acousticness": 0.08,
        "target_tempo_bpm":    160,
    }

    # --- Profile 4 (Edge Case): Conflicting — high energy but sad mood ---
    conflicting = {
        "favorite_genre":      "ambient",
        "favorite_mood":       ["melancholic"],
        "target_energy":       0.90,
        "target_valence":      0.20,
        "target_acousticness": 0.50,
        "target_tempo_bpm":    140,
    }

    # --- Profile 5 (Edge Case): Perfectly average across all features ---
    average_user = {
        "favorite_genre":      "jazz",
        "favorite_mood":       ["relaxed"],
        "target_energy":       0.50,
        "target_valence":      0.50,
        "target_acousticness": 0.50,
        "target_tempo_bpm":    100,
    }

    # --- Profile 6 (Edge Case): Genre that has only one song in catalog ---
    rare_genre = {
        "favorite_genre":      "reggae",
        "favorite_mood":       ["peaceful"],
        "target_energy":       0.55,
        "target_valence":      0.79,
        "target_acousticness": 0.63,
        "target_tempo_bpm":    85,
    }

    print_recommendations("High-Energy Pop",          high_energy_pop, songs)
    print_recommendations("Chill Lofi",               chill_lofi,      songs)
    print_recommendations("Deep Intense Rock",        intense_rock,    songs)
    print_recommendations("Edge Case: Conflicting",   conflicting,     songs)
    print_recommendations("Edge Case: Average User",  average_user,    songs)
    print_recommendations("Edge Case: Rare Genre",    rare_genre,      songs)


if __name__ == "__main__":
    main()
