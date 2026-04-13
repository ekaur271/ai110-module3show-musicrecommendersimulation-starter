# Profile Comparison Reflections

---

## High-Energy Pop vs. Chill Lofi

These two profiles are basically opposites and the results showed that clearly.

High-Energy Pop came back with Sunrise City, Gym Hero, and Neon Pulse — all fast, loud, and electronic. Chill Lofi came back with Midnight Coding, Library Rain, and Focus Flow — all slow, soft, and acoustic.

The reason they split so cleanly is that energy and acousticness are both pulling in completely opposite directions for these two profiles. High-Energy Pop has energy=0.90 and acousticness=0.05. Chill Lofi has energy=0.38 and acousticness=0.80. Those two features alone are enough to separate the entire catalog into two different worlds, which makes sense because that's basically how those genres feel in real life.

---

## Deep Intense Rock vs. High-Energy Pop

These two profiles are both high energy but point in different directions emotionally.

Deep Intense Rock has low valence (0.30) and targets slower, darker sounding music. High-Energy Pop has high valence (0.85) and targets bright, happy music. Both have energy around 0.90 so the top results for both include some of the same high-energy songs, but the valence difference pushes them apart. Rock got Storm Runner and Iron Curtain at the top. Pop got Sunrise City and Gym Hero.

This shows that energy alone isn't enough to define a vibe — valence is what separates "angry and intense" from "happy and pumped."

---

## Deep Intense Rock vs. Edge Case: Conflicting

Both profiles asked for high energy, but the conflicting profile also asked for melancholic mood and ambient genre, which created a contradiction.

Rock got exactly what it asked for — dark, high-energy songs that matched both numerically and by mood/genre bonus. The conflicting profile also got dark high-energy songs, but none of them matched the ambient genre or melancholic mood it actually wanted. Iron Curtain and Storm Runner showed up in both lists.

This comparison shows the biggest weakness in the system. When a user's mood and genre preferences don't match any high-energy songs in the catalog, the numeric features win and the mood/genre labels get ignored. The system has no way to say "nothing fits, try adjusting your preferences."

---

## Chill Lofi vs. Edge Case: Average User

Chill Lofi had a clear personality — low energy, high acousticness, specific genre. Average User had everything set to 0.5 with no strong preference.

Chill Lofi's results were tight and consistent, all 3 lofi songs scored 1.00. Average User's results were spread across r&b, lofi, jazz, and reggae with scores between 0.85 and 0.94 — decent matches but no clear winner.

This shows that the system works best when the user actually has a strong preference. A vague profile gets vague results. That's not a bug exactly, but it does mean the system doesn't do much to help a user who doesn't know what they want.

---

## Edge Case: Rare Genre (Reggae) vs. Chill Lofi

Both profiles are low-to-mid energy and acoustic-leaning, but Reggae only has 1 song in the catalog.

Reggae's #1 result was a perfect 1.00 because the profile was basically built around Island Breeze's exact values. After that, the remaining results crossed over into lofi, jazz, and r&b — genres that are numerically similar but not reggae at all.

Chill Lofi had 3 songs that all scored 1.00 because lofi is well-represented in the catalog.

The difference shows how catalog size directly affects result quality. Rare Genre users get one great match and then fall off a cliff. This is the same problem Spotify had early on with niche artists — not enough data means not enough variety.
