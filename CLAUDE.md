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
A unified single-page app deployed on Netlify with three sections (Home, Cookbook, Workouts). The Home section contains:

- **Date** — shows today's full date and day of the week
- **Weather · Oslo** — live current conditions fetched from Open-Meteo (free, no API key needed): temperature, feels like, humidity, wind speed, and a weather emoji. Uses Oslo coordinates (lat 59.9139, lon 10.7522).
- **Latest News · NRK** — fetches NRK's RSS feed directly in the browser (NRK sends Access-Control-Allow-Origin: * so no proxy needed) and displays the 3 most recent headlines as clickable links with publish times.
- **To-Do List** — add tasks by typing and pressing Enter or clicking +, check off completed items, remove with ✕
- **Motivational Quote** — randomly selected from a built-in list of 8 quotes, with a "New quote" button to cycle through them

### Workout Tracker (inside dashboard.html)
A lifting and running log accessible from the Workouts tab. Features:

- **Log new workout** — modal form for either a lifting session (exercises with sets/reps/weight) or a run (distance, time, auto-calculated pace)
- **Session history** — all past workouts shown as cards with date, type badge, and full exercise details
- **Permanent storage via Supabase** — workouts are saved to a real database (not localStorage), so data persists across devices and browser clears
- **Supabase project:** https://mkqslgtjbshsmsdhoovg.supabase.co — table: `workouts`
- **Delete** — remove any session with the ✕ button

### Live URL
**https://haakonsdashboard.netlify.app** — this is the primary way to use the dashboard. No local server needed for daily use.

### Running locally (optional)
Double-click launch.command to start server.py on port 8080 and open the dashboard in the browser. Only needed if you want to run it on your Mac without internet access. Press Ctrl+C in Terminal to stop.

### Files
- dashboard.html — the full dashboard UI, deployed to Netlify
- server.py — local Python server (for offline/local use only)
- launch.command — double-clickable macOS launcher (for offline/local use only)

### cookbook.html
A personal cookbook app in the same warm 60s/70s brown theme as the dashboard. Features:

- **Add recipes** — title, category (Breakfast / Lunch / Dinner / Snacks), ingredients (one per line), steps (one per line)
- **Search** — filters by title or ingredient instantly as you type
- **Category filter tabs** — All, Breakfast, Lunch, Dinner, Snacks
- **Recipe detail view** — opens in a modal with numbered steps and a bullet list of ingredients
- **Delete** — remove a recipe from the detail view
- **Recipe of the Day** — a built-in high-protein healthy recipe shown at the top, changes daily
  - Heart ♡ button = taste signal (like recipes you enjoy to train personalisation)
  - "Add to my cookbook" button — always visible, saves the recipe to your list instantly
  - "Remove" link — undoes an accidental add
  - **Learning period (first 30 days):** cycles through all 14 built-in recipes, shows countdown to personalisation
  - **After 30 days + 3 likes:** scores all recipes by similarity to liked ones (matching category + ingredients) and picks the best match each day for variety
  - Liked/added state and first-used date are stored in localStorage under `cookbook_rotd_state`

Recipes are saved in `localStorage` — no server needed. Open cookbook.html directly in the browser.
