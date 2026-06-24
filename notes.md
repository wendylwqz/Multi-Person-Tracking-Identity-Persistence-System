# Person Tracker Evaluation

Single person:
- stable while moving slowly.
- ID changes after leaving frame for ~2 seconds.

Multi-person:
- stable if the people do not intersect on screen.
- ID changes after leaving frame or identities run into each other.

Occlusion:
- ID sometimes changes when body fully blocked.

Re-entry:
- always assigned new ID.