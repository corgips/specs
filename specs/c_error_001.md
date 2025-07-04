---
title: Error and Incompatibility Event Format
status: Draft
version: 0.1.0
id: spec:@corgi/error/v0.1.0
hash_id: spec:TODO
authors:
  - "@corgicontributors"
created: 2025-07-03
---

# C-ERROR-001: Error and Incompatibility Event Format

This specification defines a standard event type for reporting errors, incompatibilities, and processing issues encountered by Corgi clients or relays.

## Purpose

This event type is intended to support:

- Reporting compatibility issues between clients, relays, and events.
- Structured debugging and diagnostics in decentralized environments.
- Improving interoperability by making problems visible.

## Event Type

```json
{
  "type": "spec:@corgi/error/v0.1.0#incompatibility",
  "content": "Event type 'video' not supported in CorgiNotes v0.3.2",
  "tags": [
    ["event", "abc123deadbeef"],
    ["client", "CorgiNotes"],
    ["version", "0.3.2"],
    ["type", "spec:@corgi/event/v0.1.0#video"]
  ],
  "created_at": 1689000000,
  "auth_mode": "unsigned"  
}
```

## Tags

The `tags` array should include relevant context about the error:

| Tag       | Description                                                  |
|-----------|--------------------------------------------------------------|
| `event`   | (Optional) The event ID this report refers to                |
| `client`  | Name of the client or relay encountering the error           |
| `version` | Version of the client or relay                               |
| `type`    | The type (or kind) of event that triggered the incompatibility |
| `spec`    | (Optional) Reference to the spec that was not followed or misread |
| `note`    | (Optional) Human-readable hint or extra detail               |

## Auth Mode

These events MAY be unsigned (`auth_mode: "unsigned"`) or signed by the reporting identity. Relays and clients SHOULD still treat them as advisory.

## Behavior

- Clients and relays MAY emit this event type locally or to known reporting relays.
- Events may be filtered into logs, diagnostic dashboards, or shared as public issue reports.
- Tools MAY aggregate these events to highlight common implementation issues.

## Spec Status

This spec is in draft form and intended to seed feedback on a structured mechanism for reporting issues in the ecosystem.

## Future Considerations

- Formalize severity levels (`info`, `warning`, `error`, `fatal`).
- Define standardized error codes for common problems.
- Add `reported_by` field to signal the authority of the reporter.
- Link errors to schemas or spec versions when appropriate.

