# Claude Session Notes

**Always read this file at the start of every session.**

## About the User

- Complete beginner learning vibe coding
- Spends 30–45 minutes per day on learning sessions

## Session Guidelines

- Start each session by reading this file
- Keep explanations beginner-friendly — avoid jargon or explain it when used
- Break tasks into small, approachable steps
- Be encouraging and patient

## What We've Built

### dashboard.html
A personal daily dashboard webpage with a dark, modern design. Contains:

- **Date** — shows today's full date and day of the week
- **Weather · Oslo** — live current conditions fetched from Open-Meteo (free, no API key needed): temperature, feels like, humidity, wind speed, and a weather emoji. Uses Oslo coordinates (lat 59.9139, lon 10.7522).
- **Latest News · VG.no** — fetches VG's RSS feed via allorigins.win proxy (needed to avoid browser CORS restrictions) and displays the 3 most recent headlines as clickable links with publish times.
- **To-Do List** — add tasks by typing and pressing Enter or clicking +, check off completed items, remove with ✕
- **Motivational Quote** — randomly selected from a built-in list of 8 quotes, with a "New quote" button to cycle through them

All functionality is in a single self-contained HTML file — no installs or build tools needed.
