---
# The wireframe uses the kit: sections per screen, data-go navigation, REQ tags, coverage screen.
type: regex
target: last_message
pattern: '^(?=[\s\S]*id="class-list")(?=[\s\S]*id="my-bookings")(?=[\s\S]*id="waitlist-offer")(?=[\s\S]*id="attendees")(?=[\s\S]*id="coverage")(?=[\s\S]*data-go=")(?=[\s\S]*class="req-tag")(?=[\s\S]*req-toggle)'
weight: 2
---
