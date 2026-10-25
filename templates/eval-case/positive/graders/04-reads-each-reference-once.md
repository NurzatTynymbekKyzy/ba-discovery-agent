---
# Token efficiency: the skill should read each reference file at most once per
# run. Replace the pattern with the skill's own files; add a `max: 0` grader for
# any large file the skill must NOT read in this case (for example, data only
# needed after the BA approves).
type: tool_used
tool: Read
input_match: 'references/output-format\.md'
min: 0
max: 1
arm: with-only
weight: 1
---
