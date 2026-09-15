// collision.js — AABB collision check between the player and obstacles.
// Each obstacle can have its own width/height (per PLAN.md's risk note
// about per-obstacle bounding boxes), so this checks each obstacle's own
// rect rather than assuming one fixed size.

function rectsOverlap(a, b) {
  return (
    a.x < b.x + b.width &&
    a.x + a.width > b.x &&
    a.y < b.y + b.height &&
    a.y + a.height > b.y
  );
}

function checkCollision(player, obstacles) {
  for (const obstacle of obstacles) {
    if (rectsOverlap(player, obstacle)) {
      return true;
    }
  }
  return false;
}
