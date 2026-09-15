# Obstacle Jump — Endless Runner

## 1. Goal
A browser-based endless runner (Chrome Dino-style) for Jordan: a character auto-runs and the player times jumps to clear a continuous stream of obstacles, difficulty ramps up over time, and the goal is beating your own local high score.

## 2. Scope

**In scope (v1):**
- Single-player, single-screen endless runner, playable directly by opening `index.html` (no server, no build step)
- Auto-running character; jump via keyboard (spacebar/up arrow) and tap/click (touch/mobile)
- Procedurally spawning obstacles, 2-3 varied shapes/sizes, with increasing speed/frequency over time
- Collision detection that ends the run
- Score = survival time/distance; high score saved via `localStorage`
- Start screen and game-over screen with restart flow (no page reload needed)

**Out of scope (v1):**
- Backend, accounts, or cross-device/shared leaderboards
- Duck/slide, double-jump, power-ups, multiple characters/skins
- Sound/music
- Sprite art/animation (plain canvas-drawn shapes only)
- Actual deployment/hosting (site is built deploy-ready as static files, but publishing it — e.g. GitHub Pages — is a manual follow-up for Jordan, not part of this build)

Cutting scope note: no framework, no bundler, no backend — intentional, so the game is instantly playable and trivially shareable as a handful of static files.

## 3. Tech stack
- **HTML5 Canvas + vanilla JavaScript** — no framework/build step needed for a game this size; runs in any browser by opening the file.
- **CSS** — minimal, just for layout and start/game-over overlay styling.
- **localStorage** — zero-infrastructure client-side persistence for high score.
- No package manager, no bundler, no backend.

## 4. Architecture
- `index.html` — canvas element, start/game-over overlay markup, script includes.
- `style.css` — page/canvas/overlay layout and styling.
- `game.js` — main loop (`requestAnimationFrame`), state machine (start → playing → game-over), input handling (keydown, click/touch), ties other modules together.
- `player.js` — player entity: position, velocity, gravity, jump physics, draw method.
- `obstacles.js` — obstacle spawner (randomized timing, 2-3 shape/size variants), movement, off-screen cleanup, draw method.
- `collision.js` — AABB collision check between player and obstacles.
- `score.js` — live score tracking (time/distance-based), difficulty-ramp values (speed/spawn rate), `localStorage` read/write for high score.

## 5. Milestones / task list
1. Scaffold `index.html` + `style.css`: sized/centered canvas, static start and game-over overlays (no logic yet).
2. `game.js` loop skeleton: `requestAnimationFrame` loop, clear/redraw each frame, state machine (start/playing/game-over) with no transitions wired yet.
3. `player.js`: draw a static player shape resting on the ground line.
4. Add jump physics to player: gravity, velocity, jump trigger on keydown, clamp to ground level.
5. `obstacles.js`: spawn one obstacle type at a fixed interval, move left at constant speed, remove when off-screen.
6. `collision.js`, wired into `game.js`: end run (switch to game-over state) on player-obstacle overlap.
7. `score.js`: increment score by survival time/distance; render live score on canvas/HUD during play.
8. Difficulty ramp: obstacle speed and/or spawn frequency increases as score/time increases.
9. High score persistence: read/write `localStorage`; display current high score on start and game-over screens.
10. Restart flow: input on game-over screen resets game state and returns to playing (no reload).
11. Touch/mobile input: tap-anywhere-on-canvas triggers jump; verify canvas layout is usable on small screens.
12. Obstacle variety: add 2-3 distinct shapes/sizes with weighted random spawning in place of the single placeholder obstacle.
13. Polish pass: clear visual distinction between start/playing/game-over states, short on-screen instructions, tidy overlay show/hide transitions.

## 6. Definition of done
- Opening `index.html` directly in a browser (no server/build step) shows a start screen.
- Pressing spacebar/up-arrow or tapping/clicking starts the run; player auto-runs and jumps on input.
- Obstacles (2-3 varied shapes/sizes) spawn continuously and move toward the player; touching one ends the run and shows a game-over screen with that run's score.
- Game speed/difficulty visibly increases the longer a run lasts.
- High score persists across page reloads via `localStorage` and is displayed on the start and game-over screens.
- Player can restart immediately from the game-over screen without reloading the page.
- Playable via both keyboard (desktop) and tap/click (touch) input.
- All files are static (`index.html`, `style.css`, `.js` files) — playable by opening `index.html` with no build/install step, and ready to drop onto any static host later.

## 7. Risks / open questions
- Canvas responsiveness across varied mobile screen sizes can be fiddly (sizing, tap target accuracy near screen edges) — flag for extra Tester attention.
- Difficulty-ramp tuning (how fast speed/spawn-rate increase) is a feel/balance judgment call, not a hard spec — Coder should pick reasonable starting values and this should be explicitly playtested, not just unit-verified.
- Obstacle variety is capped at 2-3 shapes per Jordan's answer; if collision boxes differ meaningfully by shape, confirm `collision.js` handles per-obstacle bounding boxes rather than one fixed size.
