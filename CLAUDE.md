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
- **Latest News · NRK** — fetches NRK's RSS feed directly in the browser (NRK sends Access-Control-Allow-Origin: * so no proxy needed) and displays the 3 most recent headlines as clickable links with publish times.
- **To-Do List** — add tasks by typing and pressing Enter or clicking +, check off completed items, remove with ✕
- **Motivational Quote** — randomly selected from a built-in list of 8 quotes, with a "New quote" button to cycle through them

The dashboard is a single self-contained HTML file — no server needed. It can be deployed directly to Netlify (or any static host) by uploading dashboard.html.

### How to run locally
Double-click launch.command. It starts server.py on port 8080 and opens the dashboard in the browser. Press Ctrl+C in the Terminal to stop. (server.py is only needed when opening from a local file:// URL in Safari — not required when hosted online.)

### Files
- dashboard.html — the full dashboard UI, works as a standalone file online
- server.py — local Python server for running on your Mac without deploying
- launch.command — double-clickable macOS launcher

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
