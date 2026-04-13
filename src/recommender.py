import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: List[str]
    target_energy: float
    target_valence: float
    target_acousticness: float
    target_tempo_bpm: float

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs.csv and return a list of dicts with numeric fields cast to float/int."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a 0–1 similarity score and a list of human-readable reasons for the match."""
    reasons = []

    # normalize tempo to 0-1 scale (dataset range: 60–180 bpm)
    min_bpm, max_bpm = 60, 180
    song_tempo_norm = (song["tempo_bpm"] - min_bpm) / (max_bpm - min_bpm)
    user_tempo_norm = (user_prefs.get("target_tempo_bpm", 100) - min_bpm) / (max_bpm - min_bpm)

    # weighted feature distances
    d_energy       = abs(user_prefs.get("target_energy",       0.5) - song["energy"])
    d_valence      = abs(user_prefs.get("target_valence",      0.5) - song["valence"])
    d_acousticness = abs(user_prefs.get("target_acousticness", 0.5) - song["acousticness"])
    d_tempo        = abs(user_tempo_norm - song_tempo_norm)

    distance = (0.35 * d_energy) + (0.30 * d_valence) + (0.20 * d_acousticness) + (0.15 * d_tempo)
    score = 1.0 - distance

    reasons.append(f"energy match score: {1.0 - d_energy:.2f} (diff: {d_energy:.2f})")
    reasons.append(f"valence match score: {1.0 - d_valence:.2f} (diff: {d_valence:.2f})")
    reasons.append(f"acousticness match score: {1.0 - d_acousticness:.2f} (diff: {d_acousticness:.2f})")
    reasons.append(f"tempo match score: {1.0 - d_tempo:.2f} (diff: {d_tempo:.2f})")

    # categorical bonuses
    favorite_moods = user_prefs.get("favorite_mood", [])
    if isinstance(favorite_moods, str):
        favorite_moods = [favorite_moods]
    if song["mood"] in favorite_moods:
        score += 0.05
        reasons.append(f"mood match: '{song['mood']}' (+0.05)")

    if song["genre"] == user_prefs.get("favorite_genre", ""):
        score += 0.03
        reasons.append(f"genre match: '{song['genre']}' (+0.03)")

    score = min(score, 1.0)
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song against user preferences and return the top k ranked by similarity."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = " | ".join(reasons)
        scored.append((song, score, explanation))

    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return ranked[:k]
