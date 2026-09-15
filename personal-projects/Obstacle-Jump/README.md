# 🕹️ Obstacle Jump

A browser-based endless runner (Chrome Dino-style) — time your jumps to clear a continuous stream of obstacles as the game speeds up, and try to beat your own local high score.

## 📂 What's Inside

- `index.html` — canvas element, start/game-over overlay markup, script includes
- `style.css` — page/canvas/overlay layout and styling
- `game.js` — main loop, state machine (start → playing → game-over), input handling
- `player.js` — player entity: position, gravity, jump physics, rendering
- `obstacles.js` — obstacle spawning, movement, and variety
- `collision.js` — collision detection between player and obstacles
- `score.js` — live score tracking, difficulty ramp, `localStorage` high score
- `PLAN.md` — original build plan (goal, scope, milestones, definition of done)
- `CHANGELOG.md` — full build history from the dev-team build

## 🚀 How to Play

No install, no server, no build step — just open `index.html` in a browser.

- **Desktop:** press spacebar or the up arrow to jump
- **Mobile:** tap anywhere on the canvas to jump
- Clear obstacles to survive as long as possible — speed and spawn rate ramp up the longer you last
- Your high score is saved locally and shown on the start and game-over screens
- Restart instantly from the game-over screen, no reload needed

## 🏗️ Tech Stack

- **HTML5 Canvas + vanilla JavaScript** — no framework or build step
- **CSS** — layout and overlay styling
- **localStorage** — client-side high score persistence

## 🤖 AI-Assisted Development

Built end-to-end with my personal dev-team agents (Architect, Coder, Tester, Manager): the Architect scoped the plan, Coder implemented it milestone by milestone, Tester actively tried to break each piece, and Manager reviewed the full build before sign-off. I reviewed and confirmed the plan and final report throughout.

## 📈 Status

v1 complete — all planned milestones and definition-of-done items verified. Next up: a real playtest on desktop and mobile, and possibly GitHub Pages deployment.

---

**Jordan Fitzgerald**  
Computer Science | Morehouse College
