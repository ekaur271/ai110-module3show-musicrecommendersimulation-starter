# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeCheck**

---

## 2. Intended Use  

VibeCheck is a content-based music recommender designed for exploring how AI recommendation systems work. 

It takes in account a user's taste profile, like their prefered genre, mood, energy level, valence, acousticness, and tempo, and scores every song in a small catalog by how closely it matches those preferences. It then returns the top results with an explanation for each pick. 

It assumes the user can be represented by a single fixed profile with no history showing that this is not built for real users or production use and is very much a simulation. 

---

## 3. How the Model Works  

VibeCheck looks at 4 things about every song: 
    - Energy: How intense it feels. 
    - Valence: How happy or sad it sounds.
    - Acousticness: Whether its acoustic or electronic.
    - Tempo: How fast it is. 

On the user's side, it sstores your target values for each of these 4 things, plus favorite genre and mood. 

When you run it, the system goes through every song in the catalog and measures how far each one is from the user's targets. The closer a song's numbers are to the targets, the higher it scores. 

Energy matters the most in the math, followed by valence, than acousticness, then tempo. 

Also, if a song matches your mood or genre it gets a small bonus to nudge it further up. 

The final score is just 1 minus the total distance, so a perfect match scores 1 and a complete mismatch scores closer to 0. 

The starter logic only checked genre, mood, and energy in a basic way with no weighting or explanation. The updated version added valence, acousticness, and tempo as real scoring features, assigned each feature a specific weight based on how much it actually affects musical vibe, normalized tempo so it's comparable to the other features, and made the system return a reason for every score so you can see exactly why a song was recommended.

---

## 4. Data

The catalog has 20 songs total.

The starter file came with 10 songs covering these genres:
  - pop, lofi, rock, ambient, jazz, synthwave, indie pop

And these moods:
  - happy, chill, intense, relaxed, focused, moody

10 additional songs were added to improve diversity, bringing in:
  - r&b, hip-hop, classical, reggae, metal, folk, electronic

And new moods:
  - romantic, melancholic, energized, dreamy, angry, peaceful

No songs were removed from the original dataset.

Parts of musical taste that are still missing:
  - No country, latin, gospel, or world music genres
  - Very few truly low-valence songs, so melancholic or sad users are underserved
  - No songs represent slow, high-valence energy (like a soft romantic ballad with big emotion)
  - Lyrics, language, and cultural context are completely absent from the scoring

---

## 5. Strengths

The system works best for users with a clear, consistent vibe.

For example:
  - A chill lofi user got all 3 lofi songs ranked 1.00 at the top, which felt exactly right
  - A high energy pop user got pop and energized tracks first, with the mood bonus correctly separating happy songs from intense ones
  - A deep rock user got Storm Runner and Iron Curtain in the top 2, which matched intuition perfectly

The scoring also does a good job of explaining itself. Every recommendation comes with a breakdown of which features matched and by how much, so it never feels like a black box.

The energy + valence combination captures musical vibe pretty well. Songs that feel happy and intense score high together, and songs that feel calm and warm score high together, which lines up with how most people actually describe music they like.

---

## 6. Limitations and Bias

The system has a few places where it struggles or behaves unfairly.

Features it does not consider at all:
  - Lyrics or language
  - Artist popularity or cultural context
  - Time of day or listening context (like working out vs. studying)
  - How songs sound next to each other in a playlist

Genres and moods that are underrepresented:
  - Romantic, peaceful, and angry moods each only have 1 song, so users with those preferences get very little variety
  - No country, latin, or world music exists in the catalog
  - Very few low-valence songs exist, so melancholic users consistently get recommendations that don't fully match

Cases where the system overfits to one preference:
  - Energy carries the most weight (0.35), so a high-energy user will almost always get high-energy songs even if their mood or genre preference points somewhere else
  - The conflicting profile test showed this clearly — asking for ambient and melancholic but getting metal and rock because the energy numbers were closer

Ways the scoring might unintentionally favor some users:
  - Users whose taste matches the most common genres (lofi, pop) get better results because those genres have more songs in the catalog
  - The fixed weights assume everyone cares about energy the most, which is not true for all listeners
  - A user who only cares about tempo has no way to express that — the system will still weight energy and valence more heavily regardless

---

## 7. Evaluation

To check if the system was working right, 6 different user profiles were tested.

The profiles were:
  - High-Energy Pop
  - Chill Lofi
  - Deep Intense Rock
  - Edge Case: Conflicting (high energy but melancholic mood)
  - Edge Case: Average User (all features set to 0.5)
  - Edge Case: Rare Genre (reggae, only 1 song in catalog)

For each one, the top 5 results were checked to see if they matched what you would actually expect to hear.

The chill lofi and high energy pop profiles felt the most accurate. The results matched the vibe right away.

The most surprising one was the conflicting profile. It asked for ambient and melancholic but kept returning metal and rock songs. That showed that energy is weighted so heavily that it can override everything else when there are no songs that match all the preferences at once.

The average user profile was also interesting. With everything set to 0.5, the results were kind of all over the place, which makes sense but also shows the system has no way to handle a user who doesn't have strong preferences.

---

## 8. Future Work

There are a few things that would make VibeCheck a lot better.

The biggest one would be letting users adjust the weights themselves. Right now everyone gets the same energy-first formula, but some people care way more about tempo or mood than energy. Letting a user say "I care more about vibe than speed" would make the results feel way more personal.

A bigger catalog would also help a lot. A lot of the edge case problems came from only having 1 or 2 songs in certain genres and moods. More songs would give the system more to work with.

Other things that would improve it:
  - Add support for multiple saved profiles so you could switch between a "gym mode" and a "study mode"
  - Build in diversity so the top 5 results aren't all from the same genre every time
  - Add lyrics or language as a feature so the system understands what a song is actually saying
  - Let the profile update based on skips or replays, which is basically how Spotify learns over time

---

## 9. Personal Reflection

I never knew how recommender systems worked before this. What was really cool to learn is that it all starts with pretty basic machine learning concepts — things like measuring distance between points, clustering similar items together, and finding nearest neighbors in a data space. Those same fundamentals are what scale up into something like collaborative filtering, where Spotify is essentially clustering millions of users by behavior and finding your nearest neighbors in that space to surface what they listened to. It was fascinating to see how far those simple ideas go.

The most interesting thing I discovered was how that connects to vector databases. I keep hearing about vector DBs because of LLMs, but this project made me realize the same idea shows up in music recommendations too — songs and users both get represented as vectors, and the whole system is just finding what's closest. That made me want to learn more about it.

And honestly I didn't realize how complex it all was. I always just thought the recommendations kind of happened. Now knowing there's weights, distances, feature scoring, and tradeoffs behind every single suggestion — that's actually really cool.
