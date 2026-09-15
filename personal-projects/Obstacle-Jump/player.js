// player.js — player entity: position, jump physics, draw method.
//
// Physics values (traced by hand, not guessed):
//   GRAVITY = 1800 px/s^2, JUMP_VELOCITY = -600 px/s (up is negative y).
//   Peak jump height = v^2 / (2*g) = 600^2 / (2*1800) = 100px.
//   Time to peak = v / g = 600 / 1800 ≈ 0.33s, full hang time ≈ 0.67s.
//   Player is 40px tall resting on GROUND_Y=250 in a 300px-tall canvas,
//   so a 100px-high jump leaves the player's top at y=110 — well clear
//   of the canvas top (0) and reads as a quick, snappy arcade jump
//   rather than a slow floaty one.

const PLAYER_WIDTH = 40;
const PLAYER_HEIGHT = 40;
const GRAVITY = 1800; // px/s^2, downward
const JUMP_VELOCITY = -600; // px/s, upward (negative because +y is down)

class Player {
  constructor(groundY) {
    this.groundY = groundY;
    this.width = PLAYER_WIDTH;
    this.height = PLAYER_HEIGHT;
    this.x = 60;
    this.y = this.restingY();
    this.vy = 0;
    this.onGround = true;
  }

  restingY() {
    return this.groundY - this.height;
  }

  jump() {
    if (this.onGround) {
      this.vy = JUMP_VELOCITY;
      this.onGround = false;
    }
  }

  update(dt) {
    // Guard against a dt=0 frame (e.g. the very first frame, or a
    // pathological case where two keydowns are dispatched synchronously
    // before any animation frame has run). Without this, a freshly-set
    // jump velocity would immediately be re-clamped: y is still exactly
    // restingY (nothing has moved yet since dt=0), so the ground-clamp
    // check below would trivially fire and silently zero vy/onGround,
    // swallowing the jump before it ever got a chance to move the player.
    if (dt <= 0) {
      return;
    }

    this.vy += GRAVITY * dt;
    this.y += this.vy * dt;

    const restingY = this.restingY();
    if (this.y >= restingY) {
      this.y = restingY;
      this.vy = 0;
      this.onGround = true;
    }
  }

  draw(ctx) {
    ctx.fillStyle = "#333333";
    ctx.fillRect(this.x, this.y, this.width, this.height);
  }

  reset() {
    this.y = this.restingY();
    this.vy = 0;
    this.onGround = true;
  }
}
