// score.js — live score tracking (survival-time based), HUD rendering, and
// localStorage-backed high score persistence.

const SCORE_PER_SECOND = 10; // points per second survived; simple v1 baseline
const HIGH_SCORE_KEY = "obstacleJump.highScore";

class Score {
  constructor() {
    this.value = 0;
    this.highScore = Score.loadHighScore();
  }

  // Reads the stored high score from localStorage. Guarded with try/catch:
  // some browser contexts (e.g. certain private-browsing modes, or
  // localStorage disabled entirely) throw on access rather than just
  // returning null, and this is a zero-infrastructure nice-to-have, not
  // something that should ever crash the game.
  static loadHighScore() {
    try {
      const raw = window.localStorage.getItem(HIGH_SCORE_KEY);
      const parsed = parseInt(raw, 10);
      return Number.isFinite(parsed) && parsed > 0 ? parsed : 0;
    } catch (e) {
      return 0;
    }
  }

  // Call at end of a run. Updates this.highScore in memory and persists it
  // if the just-finished run beat the previous best. Returns true if a new
  // high score was set, so callers can react (e.g. show a "new best!" note)
  // if they want to.
  saveHighScoreIfBeaten() {
    if (this.displayValue > this.highScore) {
      this.highScore = this.displayValue;
      try {
        window.localStorage.setItem(HIGH_SCORE_KEY, String(this.highScore));
      } catch (e) {
        // Persistence failed (see loadHighScore comment) — the in-memory
        // highScore is still updated for this session, it just won't
        // survive a reload. Not fatal.
      }
      return true;
    }
    return false;
  }

  // Resets the current run's score. Deliberately does NOT touch
  // this.highScore — that persists across runs/reloads.
  reset() {
    this.value = 0;
  }

  update(dt) {
    this.value += SCORE_PER_SECOND * dt;
  }

  get displayValue() {
    return Math.floor(this.value);
  }

  draw(ctx, x, y) {
    ctx.fillStyle = "#222222";
    ctx.font = "20px sans-serif";
    ctx.textAlign = "right";
    ctx.textBaseline = "top";
    ctx.fillText("Score: " + this.displayValue, x, y);
  }
}
