<!-- Synthetic data for evals. -->
# Wireframe v1 — Meridian Fitness: approved screen map

Users: member, trainer

Flow: Book a class (member): 1. Class list → 2. Class details → 3. Booking confirmed
Flow: Manage bookings (member): 4. My bookings → cancel
Flow: Waitlist (member): 2. Class details (join waitlist) → 5. Waitlist offer
Flow: Attendees (trainer): 6. Attendees

| # | Screen (id) | For | What's on it | Requirements |
|---|---|---|---|---|
| 1 | Class list (class-list) | Member | Upcoming classes with free places; "Book" or "Join waitlist" per class | REQ-005, REQ-006 |
| 2 | Class details (class-details) | Member | Time, trainer, places left; "Book" or "Join waitlist" | REQ-005, REQ-006 |
| 3 | Booking confirmed (booking-confirmed) | Member | Confirmation, note that a reminder comes 24 hours before | REQ-005, REQ-007 |
| 4 | My bookings (my-bookings) | Member | Booked classes; "Cancel" per row, available until 1 hour before; note that later cancellations count as a no-show | REQ-005, REQ-009 |
| 5 | Waitlist offer (waitlist-offer) | Member | "A place freed up", accept within 30 minutes, countdown | REQ-006, REQ-011 |
| 6 | Attendees (attendees) | Trainer | List of booked members for a class | REQ-008 |

Assumptions: club filter on the class list.
Not shown as a screen: REQ-001, REQ-002, REQ-003, REQ-012 (business), REQ-013 (non-functional).
