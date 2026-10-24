---
# Deterministic structure check: replace the pattern with the section
# headings this skill's output format requires, in order.
# JavaScript regex: no inline flags like (?s) or (?i). Use [\s\S]* to span
# lines and put case-insensitivity in `flags`.
type: regex
target: last_message
pattern: 'Decisions[\s\S]*Action items[\s\S]*Open questions'
flags: i
weight: 1
---
