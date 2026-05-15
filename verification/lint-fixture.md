# Deliberately Broken Wiki for Lint Testing

This fixture contains intentional errors for the lint workflow to detect.

## Contradictions

- In `wiki/entities/memex.md`: "The Memex was never built."
- In `wiki/concepts/associative-trails.md`: "The Memex was partially built as a prototype."

## Stale Claims

- `wiki/entities/vannevar-bush.md` says Bush is "currently working on new projects" (he died in 1974).

## Orphan Pages

- `wiki/entities/unknown-person.md` — No other page links to it.

## Missing Pages

- `wiki/sources/2026-05-15--as-we-may-think.md` mentions "Office of Scientific Research and Development" but no entity page exists for it.

## Broken Links

- `wiki/entities/memex.md` links to `[[NonExistentPage]]` which does not exist.
