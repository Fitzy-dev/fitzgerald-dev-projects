// game.js — main loop (requestAnimationFrame), state machine, input handling,
// ties player/obstacles/collision/score modules together.
//
// NOTE on state machine scope, carried over from pass 1: PLAN.md milestone 2
// describes the loop/state skeleton with "no transitions wired yet," but a
// minimal start->playing transition on jump-input was wired then so the
// jump could actually be tested. Milestones 5-7 made game-over reachable via
// collision detection. Milestone 10 (below) makes game-over -> playing
// (restart) reachable too, so the state machine has no more dead ends.

(function () {
  const canvas = document.getElementById("game-canvas");
  const ctx = canvas.getContext("2d");
  const gameContainer = document.getElementById("game-container");
  const startScreen = document.getElementById("start-screen");
  const gameOverScreen = document.getElementById("game-over-screen");
  const finalScoreEl = document.getElementById("final-score");
  const startHighScoreEl = document.getElementById("start-high-score");
  const gameOverHighScoreEl = document.getElementById("game-over-high-score");

  const CANVAS_WIDTH = canvas.width;
  const CANVAS_HEIGHT = canvas.height;
  const GROUND_Y = 250;

  const STATE = {
    START: "start",
    PLAYING: "playing",
    GAME_OVER: "game-over",
  };
  let state = STATE.START;

  const player = new Player(GROUND_Y);
  const obstacleManager = new ObstacleManager(CANVAS_WIDTH, GROUND_Y);
  const score = new Score();

  function setState(next) {
    state = next;
    // milestone 13: overlays fade via CSS transition on the "visible" class
    // (see style.css) instead of an abrupt display:none toggle.
    startScreen.classList.toggle("visible", state === STATE.START);
    gameOverScreen.classList.toggle("visible", state === STATE.GAME_OVER);
    // milestone 13: data-state drives per-state visual accents in CSS
    // (e.g. the canvas border/title tinting red on game-over).
    gameContainer.dataset.state = state;
  }

  function refreshHighScoreDisplays() {
    startHighScoreEl.textContent = String(score.highScore);
    gameOverHighScoreEl.textContent = String(score.highScore);
  }

  function startGame() {
    player.reset();
    obstacleManager.reset();
    score.reset();
    setState(STATE.PLAYING);
  }

  function endGame() {
    finalScoreEl.textContent = String(score.displayValue);
    score.saveHighScoreIfBeaten();
    refreshHighScoreDisplays();
    setState(STATE.GAME_OVER);
  }

  function handleJumpInput() {
    if (state === STATE.START) {
      startGame();
    } else if (state === STATE.PLAYING) {
      player.jump();
    } else if (state === STATE.GAME_OVER) {
      startGame(); // milestone 10: restart directly into a new run, no reload
    }
  }

  window.addEventListener("keydown", (event) => {
    if (event.code === "Space" || event.code === "ArrowUp") {
      event.preventDefault(); // stop page scroll on spacebar/arrow
      handleJumpInput();
    }
  });

  // milestone 11: tap-anywhere-on-canvas jump input. Uses a single Pointer
  // Events listener (unifies mouse/touch/pen into one event type/stream)
  // rather than separate touchstart+click+mousedown listeners. This is what
  // actually prevents double-firing: a real tap/click still goes on to fire
  // a compatibility `click` event afterward regardless of this handler's
  // preventDefault() (confirmed in headless Chromium — preventDefault() on
  // pointerdown does NOT suppress it in that build), but since this file
  // never adds a `click` (or `touchstart`/`mousedown`) listener anywhere,
  // that extra event has nothing to trigger — `pointerdown` is the only
  // event type wired to handleJumpInput(), so one physical tap or click
  // always results in exactly one handleJumpInput() call. preventDefault()
  // here is still useful (stops default touch scrolling/zooming/text
  // selection on the canvas, see also `touch-action: none` in style.css),
  // it just isn't the mechanism that prevents double input handling — that
  // comes from only ever listening to one event type. Keyboard input is a
  // fully separate listener/codepath above and never overlaps with this one
  // (a key press cannot trigger a pointer event or vice versa), so there's
  // nothing to de-duplicate between the two modalities either — they're
  // just two independent ways to trigger the same action, which is the
  // intended redundancy for accessibility/device coverage.
  canvas.addEventListener("pointerdown", (event) => {
    event.preventDefault();
    handleJumpInput();
  });

  function drawGround() {
    ctx.strokeStyle = "#333333";
    ctx.beginPath();
    ctx.moveTo(0, GROUND_Y);
    ctx.lineTo(CANVAS_WIDTH, GROUND_Y);
    ctx.stroke();
  }

  // milestone 13: short, unobtrusive on-canvas reminder of the controls
  // while playing (the start/game-over overlays already carry the fuller
  // instruction text, this is just a small persistent corner hint in case
  // a player forgets mid-run or joined mid-scroll on mobile).
  function drawInstructions() {
    ctx.fillStyle = "#999999";
    ctx.font = "12px sans-serif";
    ctx.textAlign = "left";
    ctx.textBaseline = "top";
    ctx.fillText("Jump: Space / ↑ / Tap", 16, 16);
  }

  function update(dt) {
    if (state === STATE.PLAYING) {
      player.update(dt);
      obstacleManager.update(dt);
      score.update(dt);

      if (checkCollision(player, obstacleManager.obstacles)) {
        endGame();
      }
    }
  }

  function render() {
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    drawGround();
    obstacleManager.draw(ctx);
    player.draw(ctx);

    if (state === STATE.PLAYING || state === STATE.GAME_OVER) {
      score.draw(ctx, CANVAS_WIDTH - 16, 16);
    }
    if (state === STATE.PLAYING) {
      drawInstructions();
    }
  }

  let lastTimestamp = null;

  function loop(timestamp) {
    if (lastTimestamp === null) {
      lastTimestamp = timestamp;
    }
    // Clamp dt so a dropped/backgrounded frame can't cause a physics jump.
    const dt = Math.min((timestamp - lastTimestamp) / 1000, 0.05);
    lastTimestamp = timestamp;

    update(dt);
    render();

    requestAnimationFrame(loop);
  }

  refreshHighScoreDisplays(); // show any persisted high score immediately on load
  setState(STATE.START);
  requestAnimationFrame(loop);
})();
