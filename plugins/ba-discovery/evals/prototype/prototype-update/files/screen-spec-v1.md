<!-- Synthetic data for evals: export of the Google Doc "Screen spec v1". -->
# Meridian Fitness — Screen spec v1

Date: 2026-10-26 · Wireframe: Wireframe v1 — 2026-10-26.html · Register read on: 2026-10-26

## Flows
- Book a class (member): Class list → Class details → Booking confirmed
- Manage bookings (member): My bookings → cancel
- Attendees (trainer): Attendees

## Screens

### 1. Class list (class-list)
For: member · Reached from: start · Leads to: Class details
| Element | Behaviour | Requirements |
|---|---|---|
| Class table | Upcoming classes with free places | REQ-005 |
| "Get the app" banner | Invites members to the mobile app | REQ-004 |

### 2. Class details (class-details)
For: member · Reached from: Class list · Leads to: Booking confirmed
| Element | Behaviour | Requirements |
|---|---|---|
| Book button | Books the class | REQ-005 |
| Join waitlist | Shown when the class is full | REQ-006 |

### 3. Booking confirmed (booking-confirmed)
| Element | Behaviour | Requirements |
|---|---|---|
| Confirmation | "You're booked"; reminder 24 hours before | REQ-005, REQ-007 |

### 4. My bookings (my-bookings)
| Element | Behaviour | Requirements |
|---|---|---|
| Bookings table | Booked classes | REQ-005 |
| Cancel link (page footer) | Cancel up to 2 hours before | REQ-005 |
| No-show note | Cancellations later than 2 hours before count as a no-show | REQ-009 |

### 5. Attendees (attendees)
For: trainer
| Element | Behaviour | Requirements |
|---|---|---|
| Attendee list | Booked members for a class | REQ-008 |

## Not shown as a screen
- REQ-001, REQ-002, REQ-003 (business); REQ-013 (non-functional)
