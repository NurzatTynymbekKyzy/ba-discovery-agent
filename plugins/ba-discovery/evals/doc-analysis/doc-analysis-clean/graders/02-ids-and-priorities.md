---
# The output uses the log and register formats: Q- and REQ- ids, P1 questions.
type: regex
target: last_message
pattern: 'Q-0*1[\s\S]*P1[\s\S]*REQ-0*1|REQ-0*1[\s\S]*Q-0*1[\s\S]*P1'
flags: i
weight: 1
---
