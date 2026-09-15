// obstacles.js — obstacle spawner: fixed-interval spawn (rate ramps with
// milestone 8's difficulty curve), constant leftward movement, off-screen
// cleanup, and (milestone 12) weighted-random variety across 3 shapes.
//
// --- Jump-clearance math, generalized (traced by hand, not guessed) ---
// For any obstacle of height H, the player's bottom edge (y+40) is above
// the obstacle's top edge (groundY-H) for a duration D_above(H), found by
// solving 900t^2 - 600t + H <= 0 (same derivation as pass 2/3's original
// 35px obstacle, generalized to arbitrary H):
//   D_above(H) = sqrt(360000 - 3600*H) / 900   (real only for H <= 100,
//   i.e. below the player's ~100px theoretical peak jump height)
// For an obstacle of width W at the current obstacle speed S, the critical
// x-overlap ("danger") duration is:
//   D_cross(W, S) = (PLAYER_WIDTH + W) / S = (40 + W) / S
// The real forgiveness on *when* to start a jump (not the full ~0.67s hang
// time — see pass 2/3's notes on that distinction) is:
//   safe_window = D_above(H) - D_cross(W, S)
// This must stay positive for a jump to be possible at all; the numbers
// below were checked by hand at both the slowest (BASE_SPEED, worst case:
// largest D_cross) and fastest (MAX_SPEED) points of the difficulty ramp
// for the tallest/widest variants, not just the original shape:
//
//   variant | W  | H  | safe window @ BASE_SPEED(300) | @ MAX_SPEED(600)
//   block   | 20 | 35 | 337ms                          | 437ms
//   crate   | 36 | 25 | 324ms                          | 451ms
//   spike   | 15 | 55 | 264ms  <- tightest of the 3     | 356ms
//
// "spike" is both the tallest AND has the smallest safe window of the
// three (as expected — greatest height eats into D_above the most), but
// even its worst case (264ms, at the run's slowest/easiest speed) is
// comfortably positive and in the same ballpark as the original single
// obstacle's 320-340ms, not some much tighter/unfair value. All 3 remain
// clearable across the full BASE_SPEED..MAX_SPEED ramp range.
//
// Weighted spawn odds (block 40% / crate 35% / spike 25%) are a first-pass
// judgment call — spike is rarest since it's the tightest-margin, most
// demanding shape — same "playtest to tune, not a hard spec" caveat as
// every other feel value in this file, per PLAN.md's risk section.
//
// --- Difficulty ramp (milestone 8) ---
// Both speed and spawn frequency increase with elapsed play time, linearly,
// each capped so the game doesn't become literally unplayable on a long
// run:
//   speed:  BASE_SPEED + SPEED_RAMP_PER_SEC * elapsed, capped at MAX_SPEED.
//           +10px/s every second means the cap (MAX_SPEED=600, i.e. 2x
//           base) is reached at 30s elapsed.
//   spawn:  BASE_SPAWN_INTERVAL - SPAWN_RAMP_PER_SEC * elapsed, floored at
//           MIN_SPAWN_INTERVAL. -0.03s every second means the floor
//           (MIN_SPAWN_INTERVAL=0.8s) is reached at (1.8-0.8)/0.03 ≈ 33s
//           elapsed, roughly matching the speed ramp's timeline.
// All currently-visible obstacles move at the same current speed each frame
// (not a speed fixed at their own spawn time), matching the classic
// Chrome-Dino feel of the whole scene visibly accelerating together.

const OBSTACLE_TYPES = [
  { name: "block", width: 20, height: 35, color: "#a83232", weight: 0.4 },
  { name: "crate", width: 36, height: 25, color: "#c9782e", weight: 0.35 },
  { name: "spike", width: 15, height: 55, color: "#6b2142", weight: 0.25 },
];

const BASE_SPEED = 300; // px/s, leftward
const SPEED_RAMP_PER_SEC = 10; // px/s added per second elapsed
const MAX_SPEED = 600;

const BASE_SPAWN_INTERVAL = 1.8; // seconds
const SPAWN_RAMP_PER_SEC = 0.03; // seconds shaved off per second elapsed
const MIN_SPAWN_INTERVAL = 0.8;

// Picks an obstacle type using OBSTACLE_TYPES' relative weights (they sum
// to 1.0, but this normalizes against their actual total so that doesn't
// have to stay exactly precise as a hard invariant).
function pickWeightedObstacleType() {
  const totalWeight = OBSTACLE_TYPES.reduce((sum, t) => sum + t.weight, 0);
  let roll = Math.random() * totalWeight;
  for (const type of OBSTACLE_TYPES) {
    if (roll < type.weight) {
      return type;
    }
    roll -= type.weight;
  }
  return OBSTACLE_TYPES[OBSTACLE_TYPES.length - 1]; // float rounding fallback
}

class ObstacleManager {
  constructor(canvasWidth, groundY) {
    this.canvasWidth = canvasWidth;
    this.groundY = groundY;
    this.obstacles = [];
    this.timeSinceSpawn = 0;
    this.elapsed = 0;
  }

  reset() {
    this.obstacles = [];
    this.timeSinceSpawn = 0;
    this.elapsed = 0;
  }

  currentSpeed() {
    return Math.min(BASE_SPEED + SPEED_RAMP_PER_SEC * this.elapsed, MAX_SPEED);
  }

  currentSpawnInterval() {
    return Math.max(
      BASE_SPAWN_INTERVAL - SPAWN_RAMP_PER_SEC * this.elapsed,
      MIN_SPAWN_INTERVAL
    );
  }

  spawn() {
    const type = pickWeightedObstacleType();
    this.obstacles.push({
      x: this.canvasWidth,
      y: this.groundY - type.height,
      width: type.width,
      height: type.height,
      color: type.color,
    });
  }

  update(dt) {
    this.elapsed += dt;

    this.timeSinceSpawn += dt;
    if (this.timeSinceSpawn >= this.currentSpawnInterval()) {
      this.timeSinceSpawn -= this.currentSpawnInterval();
      this.spawn();
    }

    const speed = this.currentSpeed();
    for (const obstacle of this.obstacles) {
      obstacle.x -= speed * dt;
    }

    // Remove obstacles once fully off the left edge of the canvas.
    this.obstacles = this.obstacles.filter((o) => o.x + o.width > 0);
  }

  draw(ctx) {
    for (const obstacle of this.obstacles) {
      ctx.fillStyle = obstacle.color;
      ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
    }
  }
}
