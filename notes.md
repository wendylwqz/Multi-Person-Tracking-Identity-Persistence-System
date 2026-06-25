# Person Tracker Evaluation

### MVP 
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

### Persistent Tracker V1
Single person:
- stable while moving very slowly, 
- ID remains persistent after leaving frame for ~2 seconds.

Multi-person:
- IDs remain persistent after leaving frame .
- each individual ID remains persistent even after they run into each other.
- new ID is created once identies intersect on screen.

Occlusion:
- IDs change if person looks different from the very initial impression.