# Changelog

## Pass 1 — Milestones 1-4 (2026-09-15)

Implemented:

1. **`index.html` + `style.css` scaffold** (milestone 1)
   - 800x300 canvas (`#game-canvas`), centered via a flex body layout, scales
     responsively with `width: 100%` + `aspect-ratio: 800 / 300` on the
     container so the internal coordinate system stays 800x300 regardless of
     display size (relevant later for milestone 11 mobile work, harmless now).
   - Static `#start-screen` overlay (visible by default) and `#game-over-screen`
     overlay (`hidden` by default via CSS class), both plain markup/CSS with no
     JS logic driving them yet, per milestone 1's scope.
   - `#game-over-screen` includes an inert `<span id="final-score">` placeholder
     for the run's score — not wired to anything yet; reserved for `score.js`
     (milestones 7/9). Flagging this as a small deviation from "no logic yet"
     in spirit — it's static markup only, but it is scaffolding slightly ahead
     of milestone 1's literal scope, done for convenience since the DOM element
     will be needed anyway.

2. **`game.js` loop + state machine skeleton** (milestone 2)
   - `requestAnimationFrame` loop with delta-time computed from timestamps
     (clamped to 0.05s max to avoid a physics "spiral of death" after a
     dropped/backgrounded frame), clears and redraws the canvas every frame.
   - Three-state machine: `start` / `playing` / `game-over`, with overlay
     show/hide driven by `setState()`.
   - **Deviation from milestone 2's literal wording**: milestone 2 says "no
     transitions wired yet," but this pass's own acceptance criteria requires
     being able to actually see the player jump in a browser, which requires
     reaching the `playing` state. Wired the minimal transition needed for
     that: pressing Space/Up-Arrow on the start screen calls `startGame()`
     (resets the player, transitions to `playing`). Nothing sets the
     `game-over` state yet — that stays unreachable until collision detection
     (milestone 6) exists. Restart-from-game-over input handling explicitly
     deferred to milestone 10, noted as a comment in the code.

3. **`player.js` static shape** (milestone 3)
   - `Player` class with `x`, `y`, `width`/`height` (40x40), drawn as a filled
     dark rectangle resting on the ground line.

4. **Jump physics** (milestone 4)
   - `GRAVITY = 1800 px/s^2`, `JUMP_VELOCITY = -600 px/s` (up is negative y).
   - Traced by hand before committing to these numbers: peak height =
     v^2/(2g) = 600^2/(2*1800) = 100px; time to peak = v/g = 600/1800 ≈ 0.33s;
     full hang time (up + down) ≈ 0.67s. With `GROUND_Y = 250` and a 300px-tall
     canvas, a 100px jump leaves the player's top at y=110 — well clear of the
     canvas top, and the ~0.67s hang time reads as a quick arcade jump rather
     than floaty. These are starting values; PLAN.md's own risks section
     flags difficulty/feel tuning as a playtest concern, not a hard spec, so
     these may need adjustment once obstacles exist and timing can be judged
     against real gameplay.
   - Jump only triggers when `onGround` is true (no double/mid-air jump, per
     PLAN.md's explicit out-of-scope list).
   - Ground clamp: if the player's resting-position Y would go below the
     ground line, snap to it and zero out vertical velocity, flip
     `onGround = true`.
   - Input: `keydown` listener on `window` for `event.code === "Space"` or
     `"ArrowUp"`, with `preventDefault()` so Space/Up don't scroll the page.

### Verification performed

- `node --check game.js` and `node --check player.js` — both pass (no syntax
  errors).
- Cross-checked every DOM id and CSS class referenced in `game.js` against
  what's actually defined in `index.html`/`style.css` (`game-canvas`,
  `start-screen`, `game-over-screen`, `hidden`) — all consistent, load order
  in `index.html` puts `player.js` before `game.js` (required, since `game.js`
  constructs a `Player` instance at load time).
- Since no headless browser or `jsdom` was available in this environment (npm
  registry access returned 403), wrote a throwaway Node script
  (`/tmp/.../scratchpad/smoke_test.js`, not part of the project) that stubs
  just enough of `document`/`window`/canvas context to load the *actual*
  `player.js` + `game.js` files in a `vm` context and exercise them:
  - Confirmed both files load with zero thrown errors.
  - Confirmed initial overlay visibility matches `index.html` (start visible,
    game-over hidden).
  - Simulated a Space keydown in the `start` state and confirmed it flips to
    `playing` (start overlay becomes hidden).
  - Drove the real `requestAnimationFrame` callback across ~60 simulated
    frames (~1s), captured the player's real `y` value each frame via its own
    `ctx.fillRect(x, y, ...)` draw call (non-invasive — no test-only code
    added to the game files), and confirmed: starts at resting y=210, rises
    to a minimum y=115 after a jump (95px measured peak height vs. 100px
    theoretical — the small gap is expected discrete-timestep Euler
    integration error, not a bug), and returns to y=210 (landed, clamped)
    before the 1s window ends — consistent with the ~0.65-0.67s hang time
    traced by hand above.
  - Confirmed `render()` is called every frame (clearRect/fillRect/stroke
    call counts scale exactly with frame count, 6 draw calls/frame as
    expected: 1 clearRect + 4 ground-line calls + 1 player fillRect).

### Open / not done in this pass

- Obstacles, collision detection, scoring, difficulty ramp, high-score
  persistence, restart flow, and touch input are all still open
  (milestones 5-13), as planned — not started.
- `obstacles.js`, `collision.js`, `score.js` do not exist yet; `index.html`
  intentionally does not `<script>`-include them yet.
- The `#final-score` element in the game-over overlay is present but inert
  until `score.js` (milestone 7/9) wires it up.
- Jump/gravity feel values are a first pass and explicitly flagged (per
  PLAN.md's risks section) as needing a real playtest once obstacles exist to
  judge timing against, not just a physics-correctness check.

**Ready for testing.** Open `index.html` directly in a browser: you should
see the start screen with the player resting on the ground line. Pressing
Space or Up-Arrow starts the run (start overlay disappears); pressing
Space or Up-Arrow again while playing makes the player jump and fall back
to the ground under gravity. These are two separate keypresses, not one. No
obstacles, scoring, or game-over flow yet — by design, out of scope for this
pass.

## Pass 2 — Milestones 5-7 + Tester nit fixes (2026-09-15)

### Tester feedback addressed first

Tester confirmed no blockers on milestones 1-4 (no double-jump, correct load
order, sound key handling) and raised two low-priority, non-blocking nits:

1. **CHANGELOG wording nit** — the pass 1 closing paragraph read as if one
   keypress both starts the run and makes the player jump. Fixed to say
   explicitly that these are two separate presses. See the paragraph
   immediately above this section.
2. **Theoretical dt=0 edge case** — on the very first frame (or any
   synthetic/scripted scenario where two keydowns fire synchronously before
   an animation frame has run), `player.update(dt)` would run with `dt=0`
   right after a fresh `jump()`. Since `y` hasn't moved yet (dt=0 means the
   integration step is a no-op), the ground-clamp check `y >= restingY`
   would trivially be true (y is still exactly `restingY`), immediately
   zeroing `vy` and resetting `onGround = true` — silently swallowing the
   jump. Not reachable by a human pressing a real key (real keydown events
   never fire with zero elapsed time relative to `requestAnimationFrame`),
   but cheap to guard defensively. Fixed in `player.js`'s `update()`: added
   an early `if (dt <= 0) return;` before any integration/clamp logic, with
   a comment explaining why. Re-verified normal jump behavior still works
   correctly after the change (see Verification below — the same jump-arc
   trace used in pass 1 still lands at y=210 within ~0.65s, unaffected by
   the guard on a nonzero-dt playthrough).

### Implemented

5. **`obstacles.js`** (milestone 5)
   - `ObstacleManager` class: fixed-interval spawn, constant leftward
     movement, off-screen cleanup via array filter.
   - Values traced against player.js's existing jump physics, not guessed:
     `OBSTACLE_WIDTH=20`, `OBSTACLE_HEIGHT=35`, `OBSTACLE_SPEED=300px/s`,
     `SPAWN_INTERVAL=1.8s`. `OBSTACLE_HEIGHT=35` sits comfortably under the
     player's ~95-100px jump peak so a reasonably-timed jump clears it. At
     300px/s the player (40px wide) and obstacle (20px wide) have a ~60px
     combined critical x-overlap window, crossed in 0.2s — well inside the
     player's ~0.67s hang time, so timing doesn't have to be pixel-perfect.
     1.8s spawn interval leaves ~1.7s of clear ground between obstacles.
     These are fixed for now; milestone 8 will ramp `SPAWN_INTERVAL`/speed
     over time, and PLAN.md's own risk note already flags this as a feel
     value to playtest, not a hard spec.

6. **`collision.js`, wired into `game.js`** (milestone 6)
   - `rectsOverlap(a, b)` does a standard AABB check (strict inequalities,
     so exactly-touching edges don't count as a collision — verified in
     testing). `checkCollision(player, obstacles)` checks the player against
     each obstacle's own `x/y/width/height` individually (not one shared
     fixed size), matching PLAN.md's risk note about per-obstacle bounding
     boxes, even though all obstacles happen to share one size in this pass
     (obstacle variety is milestone 12).
   - Wired into `game.js`'s `update()`: during `PLAYING`, after updating
     player/obstacles/score, `checkCollision` runs each frame; on a hit,
     `endGame()` writes the current score into `#final-score` and calls
     `setState(STATE.GAME_OVER)`. The overlay show/hide logic for game-over
     already existed from pass 1 (`setState` toggles the `hidden` class), so
     no new overlay-visibility code was needed — game-over is now reachable
     for the first time because something finally calls `setState` with it.
   - Once in `GAME_OVER`, `update()`'s `PLAYING`-only branch stops running,
     so player/obstacles/score all freeze automatically — no extra "pause"
     logic needed.

7. **`score.js`** (milestone 7)
   - `Score` class: `value` increases by `SCORE_PER_SECOND (10) * dt` each
     frame while playing; `displayValue` is the floored integer for display.
     Time-based (not distance-based) since obstacle speed isn't tied to a
     "distance traveled" concept in this pass — matches PLAN.md's "score =
     survival time/distance" wording (time chosen as the simpler of the two
     options explicitly offered).
   - `draw(ctx, x, y)` renders `"Score: N"` right-aligned at a caller-given
     position — kept canvas-dimension-agnostic like `player.js`, with
     `game.js` passing `CANVAS_WIDTH - 16, 16` (top-right HUD position).
     Rendered during both `PLAYING` and `GAME_OVER` (so the final score
     stays visible on canvas after death, not just in the overlay).
   - **Note beyond the coordinator's milestone-6 instruction**: the
     coordinator's message said `#final-score` could stay a placeholder "0"
     for milestone 6 alone, since `score.js` didn't exist yet at that point
     in the description. Since milestones 5-7 were built together in this
     same pass and `score.js` was available by the time `collision.js` was
     wired up, I went ahead and wired the *real* run score into
     `#final-score` in `endGame()` rather than leaving it a dead "0" —
     this also directly satisfies this pass's own stated end-to-end goal
     ("game-over screen appears" implies showing that run's actual score,
     consistent with PLAN.md's Definition of Done #3: "shows a game-over
     screen with that run's score"). Flagging this as a small, deliberate
     choice, not scope creep — no new files or milestones were touched to
     do it.

### `index.html` change

Added `<script>` tags for `obstacles.js`, `collision.js`, `score.js`, in
that order, between `player.js` and `game.js` — order matters because
`game.js` constructs instances of all of them at load time.

### Verification performed

No headless browser was available in this sandbox (same constraint as pass
1), so verification again used a throwaway Node `vm`-context DOM/canvas stub
(in `/tmp/.../scratchpad/`, not part of the project) that loads the *actual*
five project JS files and exercises the real code paths, plus isolated
per-module unit checks:

- `node --check` on all 5 JS files — no syntax errors.
- **Full end-to-end, no-jump scenario**: started the run, never pressed
  jump, let the real loop run. The player was hit by the first obstacle at
  frame 248 (~4.13s), matching the hand-traced critical-window math above
  (obstacle #1 spawns at ~1.8s, reaches the player's x-range at
  ~1.8+2.33=4.13s). `game-over-screen`'s `hidden` class was correctly
  removed at that point, and `#final-score`'s `textContent` was `"41"`,
  matching the expected `floor(10 * 4.13s) = 41` ballpark from `score.js`'s
  accrual rate.
- **Full end-to-end, timed-jump scenario**: started the run, pressed jump
  ~230ms before obstacle #1's critical window, then stopped the simulation
  before obstacle #2 arrived. Confirmed `game-over-screen` stayed hidden
  (no collision) — traced the real player/obstacle `y`/`x` values frame by
  frame via their own `ctx.fillRect` calls and confirmed the player's
  bottom edge (`y+40`) stayed above the obstacle's top edge (`y=215`)
  throughout the entire critical x-overlap window.
  - First attempt at this scenario ran long enough for a *second* obstacle
    to also reach the player (since only one jump was scripted), which
    correctly ended the run — this was a test-script gap (only scripting
    one jump), not a game bug; re-verified by tracing the actual
    frame-by-frame positions before concluding that.
- **Multi-obstacle survival scenario**: jumped ahead of 5 consecutive
  obstacle danger windows across ~12.5s of simulated play; confirmed no
  false-positive collisions and the run never ended — obstacles clearing
  the screen correctly and existing obstacles not lingering/mis-triggering
  collisions after being passed.
- **`ObstacleManager` isolation test** (20s, 1/60s steps): 11 spawn events
  (expected ~11 at a 1.8s interval), max 2 concurrent obstacles on screen at
  once (consistent with ~2.67s on-screen lifetime / 1.8s spawn interval),
  array correctly stays bounded (old obstacles removed, not accumulating),
  and `reset()` clears both the array and the spawn timer.
- **`collision.js` isolation test**: far-apart obstacle → no collision;
  grounded/overlapping obstacle → collision; x-overlapping obstacle with
  player airborne above it → no collision; exactly edge-adjacent (touching
  but not overlapping) rects → no collision (correct AABB semantics).
- **`score.js` isolation test**: starts at 0; after 5s of `update(1/60)`
  calls at 10 pts/s, `displayValue` is 49 (expected ~50; the 1-point
  shortfall is floating-point accumulation error from summing `1/60`
  three hundred times plus `Math.floor`, not a bug); `reset()` returns to
  0; `draw()` calls `fillText` with the expected `"Score: N"` string and
  the given x/y.

### Open / not done in this pass

- Difficulty ramp (milestone 8), high-score `localStorage` persistence
  (milestone 9), restart flow (milestone 10), touch/mobile input
  (milestone 11), obstacle variety (milestone 12), and the polish pass
  (milestone 13) are all still open, as planned.
- Game-over is a dead end for now by design — pressing Space/Up while in
  `GAME_OVER` does nothing (`handleJumpInput` has a comment marking restart
  as milestone 10's job); this matches the pass's own stated goal ("game-
  over screen appears" — restart wiring explicitly out of scope here).
- Obstacle speed/spawn-interval and score-per-second are first-pass feel
  values, same caveat as the jump physics: PLAN.md flags this as a
  playtest concern, not a hard spec, worth a real human playthrough once
  restart (milestone 10) makes repeated runs convenient.

**Ready for testing.** Open `index.html` in a browser: start screen shows,
press Space/Up to start, the player auto-sits on the ground while a live
score counts up in the top-right corner, an obstacle scrolls in from the
right every ~1.8s, jump (Space/Up) to clear it or take a hit to end the run
— on a hit, the game-over overlay appears showing that run's final score.
Restart isn't wired yet (milestone 10), so ending a run currently requires
reloading the page to play again.

## Pass 3 — Milestone 8-10 nit fix + Milestones 8-10 (2026-09-15)

### Tester feedback addressed first

Tester confirmed no blockers/majors on milestones 5-7 (core loop solid,
cleanup bounded, dead-end game-over state safe) and raised one minor,
evidence-based finding: `obstacles.js`'s comment claimed a jump "started
slightly early or late still clears" the obstacle, implying forgiveness
close to the player's full ~0.67s hang time, but Tester measured the real
safe jump-start window at only ~320ms (3.72s-4.04s), with early jumps
failing just as reliably as late ones.

**Verified independently before fixing** (per my own process, not just
taking the finding at face value): solved the physics by hand —
`900t² - 600t + 35 ≤ 0` for when the player's bottom edge clears the
obstacle's top edge — giving a continuous-physics safe window of ~337ms,
matching Tester's ~320ms measurement (small gap expected from discrete
60fps frame quantization vs. continuous calculus). Confirmed the finding is
correct. Fixed the comment in `obstacles.js` to state the real ~320-340ms
tolerance and explicitly note that jumping too early is just as punishing
as too late — no physics values were changed, per the coordinator's
instruction to defer retuning to a real playtest after milestone 8 (below)
was in place.

### Implemented

8. **Difficulty ramp** (`obstacles.js`)
   - Both obstacle speed and spawn frequency now increase linearly with
     elapsed play time (tracked as `ObstacleManager.elapsed`, incremented
     each `update(dt)` while playing, reset on `reset()`):
     - Speed: `BASE_SPEED(300) + SPEED_RAMP_PER_SEC(10) * elapsed`, capped
       at `MAX_SPEED(600)` — reaches the cap at 30s elapsed.
     - Spawn interval: `BASE_SPAWN_INTERVAL(1.8) - SPAWN_RAMP_PER_SEC(0.03)
       * elapsed`, floored at `MIN_SPAWN_INTERVAL(0.8)` — reaches the floor
       at ~33s elapsed, roughly matching the speed ramp's timeline.
   - All currently-visible obstacles move at the same current speed each
     frame (not a speed fixed at their own spawn time), so the whole scene
     visibly accelerates together — matches the classic Chrome-Dino feel
     and is simpler to reason about than per-obstacle speeds.
   - These rates are a first-pass judgment call, explicitly flagged (same
     as the jump physics and base obstacle values) as a playtest concern
     per PLAN.md's risk section, not a hard spec.
   - **Side effect worth flagging explicitly**: because speed now ramps from
     the very start of a run (not just after some grace period), obstacle
     #1's danger window shifted earlier than pass 2's fixed-speed value —
     measured at `[3.867s, 4.017s]` now, vs. the pre-ramp `[4.133s,
     4.333s]`. This is expected (obstacle #1 is reached slightly faster
     since speed is already above 300px/s by the time it arrives) and was
     re-verified against the real code (see Verification below), not just
     assumed.

9. **High score persistence** (`score.js`, wired into `game.js`,
   `index.html`)
   - `Score` now loads a stored high score from `localStorage` on
     construction (`Score.loadHighScore()`) and exposes it as
     `score.highScore`.
   - `score.saveHighScoreIfBeaten()` (called from `game.js`'s `endGame()`)
     updates `highScore` in memory and persists it via
     `localStorage.setItem` only when the just-finished run's score is
     strictly greater than the previously stored best (ties don't
     overwrite — reasonable, avoids pointless writes).
   - Both `localStorage.getItem`/`setItem` calls are wrapped in try/catch:
     some browser contexts (certain private-browsing modes, or
     `localStorage` disabled) throw on access instead of just failing
     silently, and a high-score-persistence nice-to-have should never be
     able to crash the game. Verified this explicitly (see below) with a
     mocked `localStorage` that always throws.
   - `index.html`: added `<span id="start-high-score">` and
     `<span id="game-over-high-score">` to the two overlays.
     `game.js`'s new `refreshHighScoreDisplays()` keeps both in sync,
     called once on load (to show any persisted score immediately) and
     again in `endGame()` (in case the just-finished run set a new best).
   - `reset()` in `Score` deliberately does not touch `highScore` — only
     the current run's `value` resets between runs; the high score persists
     across runs and reloads, as it should.

10. **Restart flow** (`game.js`)
    - `handleJumpInput()` now has a third branch: pressing Space/Up-Arrow
      while `state === STATE.GAME_OVER` calls `startGame()` directly —
      identical reset path used for the very first run (resets player,
      obstacles including the ramp's `elapsed` timer, and the current-run
      score; does not touch the high score), transitioning straight back
      to `PLAYING` with no page reload.
    - Per PLAN.md's wording ("returns to playing"), restart goes straight
      to a new run rather than back to the start screen — matches the
      milestone's literal description.
    - No restart-input debounce/cooldown was added (e.g. to prevent an
      accidental instant-restart from a reflexive extra keypress right
      after dying) since PLAN.md's milestone 10 doesn't call for one; if
      Tester finds this to be a real usability problem in practice, that's
      a reasonable follow-up to flag, but I didn't want to invent UX scope
      that wasn't asked for.

### Verification performed

Same approach as passes 1-2: no headless browser available in this
sandbox, so verification used a Node `vm`-context DOM/canvas/localStorage
stub loading the *actual* project files, plus isolated per-module checks.

- `node --check` on all 5 JS files — no syntax errors.
- **Difficulty ramp isolation test**: `ObstacleManager.currentSpeed()` /
  `currentSpawnInterval()` read exactly 300px/s / 1.8s at t=0; 400px/s /
  1.50s at ~10s elapsed (matches `300+10*10=400` and `1.8-0.03*10=1.5`
  exactly); capped/floored at 600px/s / 0.8s by ~50s elapsed (well past
  both the 30s and ~33s cap/floor points); `reset()` returns `elapsed` to 0
  and speed/interval back to base.
- **High-score persistence, simulated reload**: ran a full session to
  game-over (score 38 under the new ramped timing), confirmed
  `localStorage` held `{"obstacleJump.highScore":"38"}` afterward, then
  built a *second, fresh* sandbox reusing the same backing store object
  (simulating a page reload) and confirmed the start screen's high-score
  display showed `"38"` immediately on load, matching the persisted value.
- **High-score persistence, live restart beating the previous best**: run 1
  died at score 38 (no jump). Restarted via keypress, jumped over obstacle
  #1 using the freshly re-measured safe window (jumped at 3.6s elapsed,
  inside the computed safe range), let the run continue and die on a later
  obstacle at score 54. Confirmed both `#final-score` and
  `#game-over-high-score` correctly showed `54`, `#start-high-score` also
  updated to `54`, and the `localStorage` store was overwritten to `"54"`.
  (An earlier, sloppier version of this same test had a scripting bug in
  my own test harness — not the game code — that made it look like the
  high score wasn't updating; re-ran with cleaner instrumentation printing
  actual elapsed-since-restart and per-frame state before concluding the
  real code was correct.)
- **Broken/throwing `localStorage` doesn't crash the game**: mocked
  `getItem`/`setItem` to always throw, ran a full run to game-over,
  confirmed no exception propagated and the game still reached game-over
  correctly with `#game-over-high-score` falling back to the in-memory
  value (`38`, matching that run's own score, since nothing was
  successfully persisted from a prior "session").
- **Restart flow end-to-end**: ran a full run to game-over, pressed
  Space/Up again, confirmed the game-over overlay's `hidden` class was
  restored (overlay disappeared) and the start overlay stayed hidden
  (confirming it went straight to `playing`, not back to `start`). Let the
  second run play out to its own, independent death and confirmed it took
  a comparable ~3.9s (not an instant collision from leftover obstacle
  state, and not requiring 0 frames from something carrying over) —
  confirms `obstacleManager.reset()` genuinely clears both the obstacle
  array and the ramp's elapsed timer on restart, not just the array.
- **Regression re-check of pass 2's hit/clear scenarios under the new
  ramped timing**: re-ran the "no jump → collide" and "timed jump →
  clear" scenarios against the *current* code (not the old pre-ramp
  timing) after first re-measuring the real danger window with the ramp
  active (`[3.867s, 4.017s]`, via a grounded-player-never-jumps trace using
  the actual `ObstacleManager` + `checkCollision` code). Both scenarios
  passed: no-jump run died at ~3.883s (matching the freshly measured
  window start), and a jump at 3.6s (inside the recomputed safe range)
  correctly cleared obstacle #1 with no collision.

### Open / not done in this pass

- Touch/mobile input (milestone 11), obstacle variety (milestone 12), and
  the polish pass (milestone 13) are still open, as planned.
- Difficulty ramp rates, obstacle base speed/height, spawn interval, and
  score-per-second are still first-pass feel values. With restart now
  wired, a real human playtest of these (per PLAN.md's risk note) is
  finally practical and worth doing before milestone 13's polish pass.
- No restart-input cooldown/debounce was added (see milestone 10 notes
  above) — flagging as a possible follow-up if it turns out to feel bad in
  practice, not implementing it preemptively.

**Ready for testing.** Open `index.html` in a browser: start screen shows
any previously-saved high score, press Space/Up to start, obstacles spawn
faster and move quicker the longer you survive, a hit ends the run and
shows the game-over screen with that run's score and the current high
score (updated/persisted immediately if you just beat it), and pressing
Space/Up again on the game-over screen restarts immediately into a fresh
run — no page reload needed anywhere in the loop now.

## Pass 4 — Milestones 11-13 (final pass before Manager review) (2026-09-15)

Tester confirmed no blockers on milestones 8-10 (restart resets everything
correctly including the ramp timer, `localStorage` failures degrade
gracefully, and an adaptive bot survived 3+ minutes at max ramp, confirming
the difficulty curve never creates an unavoidable sequence).

### Implemented

11. **Touch/mobile input** (`game.js`, `style.css`)
    - Added a single `pointerdown` listener on the canvas that calls the
      same `handleJumpInput()` used by the keyboard path. Pointer Events
      unify mouse/touch/pen into one event stream, so this one listener
      covers tap AND click — no separate touch/mouse-specific listeners
      were added.
    - **"Don't double-fire" requirement, addressed by construction, not by
      a workaround**: the risk is a single physical tap firing multiple
      DOM events (`touchstart` then a synthesized compatibility `click`)
      if you listen to more than one event type for the same interaction.
      Since only `pointerdown` is registered (verified — see Verification
      below, a structural check that exactly one canvas listener type
      exists) and its handler calls `event.preventDefault()`, the browser
      suppresses the subsequent compatibility mouse/click events per the
      Pointer Events spec, so one tap/click always yields exactly one
      `handleJumpInput()` call. Keyboard input is a fully separate
      listener/codepath that can't be triggered by a pointer interaction
      or vice versa, so there's no cross-modality double-fire to guard
      against either — a device with both is just two independent ways to
      trigger the same action, which is the intended redundancy.
    - "Works from all three states consistently with the keyboard path":
      `handleJumpInput()` is the single shared entry point for both input
      types, so this is automatic by design, not something maintained in
      two places — verified explicitly anyway (see below) by driving each
      of start/playing/game-over via tap alone and confirming identical
      outcomes to the keyboard path.
    - `style.css`: added `touch-action: none` and
      `-webkit-tap-highlight-color: transparent` on the canvas (disables
      default browser scroll/zoom gestures and the mobile tap-flash on the
      jump target), and a `max-width: 420px` media query that shrinks
      overlay text so it stays legible on small screens (canvas itself
      already scaled responsively via `width:100%` + `aspect-ratio` from
      pass 1, unchanged).

12. **Obstacle variety** (`obstacles.js`)
    - Replaced the single 20x35 obstacle with 3 weighted variants:
      `block` (20x35, 40% — unchanged from before, kept for continuity),
      `crate` (36x25, 35% — wider/lower), `spike` (15x55, 25% —
      narrower/taller). Each has a distinct fill color for visual
      distinction. `spawn()` picks a variant via
      `pickWeightedObstacleType()` (cumulative-weight random selection).
    - **Jump-clearance math for the new tallest/widest variant, traced by
      hand as instructed, not just for the original shape**: generalized
      the safe-jump-window derivation from pass 3 (`900t² − 600t + H ≤ 0`
      for height-clearance duration, `(40+W)/speed` for the x-overlap
      danger duration) and computed it for all 3 variants at both
      `BASE_SPEED` (worst case — largest danger duration) and `MAX_SPEED`
      (ramp cap). Full comment/table now lives in `obstacles.js`'s header.
      Summary: `spike` (tallest, H=55) has the smallest safe window of the
      three as expected (greater height eats more into the "high enough"
      duration), but even its worst case — 264ms at the run's slowest
      speed — is comfortably positive and in the same ballpark as the
      original 35px obstacle's 320-340ms, not some much tighter/unfair
      value. All 3 stay clearable (`safe window > 0`) across the entire
      `BASE_SPEED..MAX_SPEED` ramp range (verified numerically, see below).
    - `collision.js` was already written (pass 2) to check each obstacle's
      own `width`/`height` rather than one shared constant — confirmed
      this is *actually exercised*, not just structurally capable, per the
      coordinator's ask (see Verification: differential collision checks
      per shape, and a full randomized-spawn bot-survival run).

13. **Polish pass** (`game.js`, `index.html`, `style.css`)
    - **Visual distinction between states**: `game.js`'s `setState()` now
      sets `data-state` on `#game-container`; `style.css` uses that to tint
      the canvas border red (`#a83232`) and the game-over `<h1>` text the
      same red on `GAME_OVER`, so a run ending reads as a distinct visual
      event at a glance, not just different overlay text. `PLAYING` has no
      overlay at all (already true from pass 1), which is itself the
      clearest possible distinction from the two overlay-driven states.
    - **Short on-screen instructions**: added a small persistent
      `"Jump: Space / ↑ / Tap"` hint in the canvas's top-left corner,
      visible only during `PLAYING` (the start/game-over overlays already
      carry fuller instruction text; this is a lightweight in-play
      reminder, not a replacement for those).
    - **Tidy overlay show/hide transitions**: replaced the pass-1 abrupt
      `display:none` (`hidden` class) toggle with an opacity-based
      `visible` class and a `transition: opacity 0.2s ease` in CSS, so
      overlays fade in/out instead of snapping. `pointer-events: none`
      stays on the overlay regardless of visibility (unchanged from pass
      1) — all interaction goes through the canvas's own
      `pointerdown`/`keydown` listeners, so the overlay never needs to
      intercept clicks/taps, visible or not.
    - `index.html`/`game.js` updated together: initial markup now starts
      with `start-screen` already carrying `class="overlay visible"` and
      `game-over-screen` carrying just `class="overlay"` (invisible until
      `setState` adds `visible`), matching the actual initial state
      machine value (`STATE.START`) instead of relying on a separate
      `hidden` convention.

### Verification performed

Same approach as passes 1-3: no headless browser available in this
sandbox, so verification used a Node `vm`-context DOM/canvas/localStorage
stub loading the *actual* project files, plus isolated per-module checks
and hand-derived physics, cross-checked against the real code's behavior.

- `node --check` on all 5 JS files — no syntax errors.
- **No-double-fire, structural check**: confirmed exactly one listener
  type (`pointerdown`) is ever registered on the canvas — since that's the
  *only* event type in play, there's nothing for it to double-fire
  against by construction. (The Pointer-Events-suppresses-compatibility-
  events behavior itself is documented browser/spec behavior, not
  something Node's `vm` can simulate directly; the structural check plus
  citing that spec behavior in the code comment is the practical
  verification available without a real browser — flagging this
  explicitly rather than overclaiming a browser-level test that wasn't
  possible here.)
- **Tap input works consistently across all three states**: drove
  start→playing, a mid-play tap (jump, no state change), and
  game-over→playing (restart) purely via simulated `pointerdown` events
  against the real `game.js`, confirming `data-state` and each overlay's
  `visible` class ended up identical to what the equivalent keyboard input
  produces (explicit keyboard-vs-tap equivalence check included).
- **Obstacle variety, weighted distribution**: called `ObstacleManager.
  spawn()` directly 20,000 times and tallied resulting shapes — observed
  ~39.8% 20x35 / ~35.4% 36x25 / ~24.9% 15x55, matching the configured
  40/35/25 weights closely.
- **Per-obstacle collision boxes actually exercised**: checked a
  mid-air player position whose bottom edge clears a `crate`'s shorter top
  edge but does NOT clear a `spike`'s taller top edge at the *same*
  x-position — confirmed `checkCollision` returns `false` for the crate
  and `true` for the spike in that scenario, proving each obstacle's own
  height genuinely drives the result (not a shared/fixed size silently
  overriding the per-obstacle values).
- **Fairness across randomized variety, adaptive-bot survival**: ran 25
  independent 45-second sessions (comfortably past the ~30-33s ramp cap)
  against the real `player.js`/`obstacles.js`/`collision.js`, using a
  simple reactive bot (jump whenever the nearest oncoming obstacle enters
  a generous 130px trigger zone, only while grounded — deliberately
  simple/non-optimal, not hand-tuned per obstacle type) — 25/25 survived
  the full duration with no collisions. Sanity-checked this wasn't a
  vacuous test by confirming a bot that never jumps reliably dies (~3.87s,
  consistent with prior passes' measurements) against the same setup.
- **Full consolidated end-to-end trace against PLAN.md's Definition of
  Done** (see next section) — walked through every DoD bullet against the
  real, current code in one consolidated script.

### Definition of Done — final trace, explicitly checked item by item

1. *"Opening `index.html` directly in a browser shows a start screen"* —
   **MET**. Confirmed `start-screen` carries `visible` and `game-over-
   screen` does not, immediately on load, with `data-state="start"`.
2. *"Pressing spacebar/up-arrow or tapping/clicking starts the run; player
   auto-runs and jumps on input"* — **MET, with one implementation-choice
   callout worth being explicit about**: the player does not literally
   translate across the canvas — its `x` is fixed at 60, and the *ground
   line + obstacles* scroll left past it, which is the standard genre
   convention (this is exactly how the reference Chrome Dino game works
   too: the dino stays put, the world scrolls). This satisfies "auto-runs"
   as a continuous-forward-motion illusion, consistent with PLAN.md
   calling this "Chrome-Dino-style" in its own goal statement, but I'm
   flagging it explicitly in case "auto-runs" was expected to mean literal
   player translation — happy to revisit if that reading is wanted, but as
   built it matches the named reference implementation.
3. *"Obstacles (2-3 varied shapes/sizes) spawn continuously and move
   toward the player; touching one ends the run and shows a game-over
   screen with that run's score"* — **MET** (as of this pass — obstacle
   variety, milestone 12, was the last piece). Verified all 3 shapes
   actually appear on-canvas during a real (restart-looping) playthrough,
   and a hit reliably ends the run with the correct score displayed.
4. *"Game speed/difficulty visibly increases the longer a run lasts"* —
   **MET** (milestone 8). Speed/spawn-rate ramp verified numerically.
5. *"High score persists across page reloads via `localStorage` and is
   displayed on the start and game-over screens"* — **MET** (milestone 9).
   Verified via a simulated-reload test (fresh sandbox, same backing
   store) showing the persisted value on the start screen immediately.
6. *"Player can restart immediately from the game-over screen without
   reloading the page"* — **MET** (milestone 10). Verified via both
   keyboard and tap.
7. *"Playable via both keyboard (desktop) and tap/click (touch) input"* —
   **MET** (milestone 11, this pass). Verified both paths independently
   reach identical outcomes from every state.
8. *"All files are static... playable by opening `index.html` with no
   build/install step, ready to drop onto any static host later"* —
   **MET**. Confirmed via `grep` that no file in the project references
   any `http://`/`https://`/CDN URL — everything is relative local file
   references (`<script src="player.js">` etc.), no build step, no
   package manager involved anywhere in this project's own files.

**All 8 Definition of Done items are met.** The one item worth a second
look from the coordinator/Manager is #2's "auto-runs" phrasing, called out
above — not because anything is missing, but because there's a genuinely
different mental model (fixed player + scrolling world, vs. literal player
translation) and it's worth a conscious sign-off rather than an assumed
one, given it touches the core feel of the game.

### Open / not done

- Nothing from PLAN.md's milestone list (1-13) remains unimplemented.
- All values that PLAN.md's risk section flags as "playtest, don't just
  verify" (jump physics, obstacle speed/height/spawn-rate, difficulty ramp
  rates, obstacle-type weights) are still first-pass judgment calls,
  extensively fairness-checked by hand/simulation across this and prior
  passes, but not yet played by an actual human. That's explicitly a
  playtest task for Jordan, not something further automated verification
  can substitute for.
- No headless browser was available anywhere in this environment across
  all 4 passes, so every verification claim in this changelog is from a
  Node `vm`-context DOM/canvas/localStorage stub running the real project
  files, not a real browser. This is disclosed consistently rather than
  implied to be full browser testing — a real-browser check (desktop +
  at least one actual mobile device, for the touch-input and small-screen
  claims specifically) is the one category of verification this project
  has not had that a real browser could add.

**Ready for testing — this is the final pass before Manager review.** Open
`index.html` in any modern browser (desktop or mobile): start screen shows
with any saved high score, start via keyboard or tap, obstacles now vary in
shape (3 types) and speed/frequency ramp up with survival time, a small
in-play control hint sits in the corner, a hit shows a visually distinct
red-tinted game-over screen with that run's score and the current high
score, and tapping or pressing Space/Up immediately restarts — no reload
anywhere in the loop.

## Pass 5 — Real-browser confirmation + one doc correction (2026-09-15)

Tester got access to a real headless Chromium in the sandbox and
re-verified all 8 Definition of Done items against actual browser
rendering, real DOM events, and real `localStorage` under `file://` —
**confirmed for real this time**, not just via the Node `vm` stub pass 4's
verification section (correctly) disclosed as its limitation. No blockers.

### Correction

Tester found one inaccuracy in `game.js`'s touch-input comment (pass 4):
it claimed `event.preventDefault()` on `pointerdown` "suppresses the
subsequent compatibility mouse events (mousedown, click, etc.)" per the
Pointer Events spec. **Verified this myself independently** before fixing
it (same process as pass 3's comment-correction) using Playwright against
the real headless Chromium available in this environment:
`/home/claude/.npm-global/lib/node_modules/playwright`, launched against
the actual `index.html` via `file://`. Dispatched both a real mouse click
and a real touch tap (in a `hasTouch`/`isMobile` browser context) at the
canvas, with listeners recording every event type that fired:

- Mouse click: `['pointerdown', 'click']`
- Touch tap: `['pointerdown', 'touchstart', 'click']`

`click` fires in both cases, confirming `preventDefault()` on `pointerdown`
does **not** suppress it in this Chromium build — Tester's finding was
correct, and my pass-4 comment overstated what the spec/browser actually
guarantees here. Fixed the comment in `game.js` (the `pointerdown` listener
right before `canvas.addEventListener("pointerdown", ...)`) to describe the
*real* safety mechanism: `game.js` simply never registers a `click` (or
`touchstart`/`mousedown`) listener anywhere, so the extra `click` event
that does fire has nothing to trigger — one physical tap/click still
results in exactly one `handleJumpInput()` call, but because only one
event type is ever wired up, not because `preventDefault()` suppresses the
others. `preventDefault()` is still correctly called and still useful (it
stops default touch scrolling/zoom/selection on the canvas, working
together with `touch-action: none` in `style.css`) — that part of the
original comment was accurate and is kept; only the double-fire-prevention
mechanism claim was corrected. No behavior changed, only the comment.

Note: pass 4's "Verification performed" and "Definition of Done" sections
above (written before this correction) still describe the
`preventDefault()`-suppresses-compatibility-events claim in a couple of
places (the milestone 11 write-up and the "No-double-fire, structural
check" bullet) — left as-is rather than rewritten, since they're a dated
historical record of what was believed/tested at the time and pass 4
already correctly disclosed no real browser was available for that claim.
This Pass 5 entry is the authoritative correction going forward.

### Verification

- `node --check game.js` — no syntax errors after the comment edit (no
  functional code changed).
- Confirmed independently via Playwright + real headless Chromium (see
  above) before making the fix, rather than accepting Tester's report at
  face value.

**Project complete — no remaining milestones.** Moving to Manager review.
