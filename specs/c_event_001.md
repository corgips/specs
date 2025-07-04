---
title: Event Model
status: Draft
version: 0.1.0
id: spec:@corgi/event-model/v0.1.0
hash_id: spec:af218e3b
authors:
  - "@corgicontributors"
created: 2025-06-23
types:
  note:
    description: Plain text post
    schema: ./schemas/note.json
  reply:
    description: Reply to another post
    schema: ./schemas/reply.json
---
# C-EVENT-001: Event Model

## Abstract
Defines the base schema for Corgi events — the atomic units of data in the network. Events may be signed or unsigned and are intended to be minimal, extensible, and interoperable.

---

## Motivation
Events are the foundation of the Corgi ecosystem. They represent actions like posting, reacting, broadcasting presence, or sending ephemeral data. This spec standardizes their structure while allowing flexibility in encoding and authentication.

---

## Event Structure
```json
{
  "id": "<string> (optional, may be derived hash)",
  "type": <string>,
  "created_at": <unix timestamp>,
  "pubkey": "<string> (optional)",
  "tags": [["p", "pubkey"], ["e", "event-id"]],
  "content": "<string>",
  "sig": "<string> (optional)"
}
```

### Fields
- **id** (optional): A unique identifier. Can be hash of the full event or client-generated.
- **type**: String identifying the type of event (see [Type Registry](types.json)).
- **created_at**: Unix timestamp in seconds.
- **pubkey** (optional): The public key of the sender. Recommended if `sig` is present.
- **tags**: A list of `[type, value]` pairs.
- **content**: Raw content, markdown, or JSON-encoded string.
- **sig** (optional): A digital signature. Required for identity verification.

### `type`
The `type` field MUST reference a defined event type within the spec garden. It takes the form:
```json
"type": "spec:@namespace/specname/version#typename"
```
Clients and relays MAY use this value to determine how to parse or display an event. Schemas for machine-readable validation may be provided in the `types:` section of the spec’s frontmatter.

---

## Authentication
Signatures are **optional**, but encouraged for events linked to identity or long-term state.

### Valid modes:
- **Unsigned**: No `sig` or `pubkey`. Treated as anonymous or ephemeral.
- **Signed**: Includes `sig` and `pubkey`. Allows verification.
- **Delegated**: Uses derived keys and delegation proofs (see `C-ID-001`).

Clients and relays should:
- Accept unsigned events unless policy restricts them
- Show visual indicators of verification status
- Allow filters based on trust level

---

## Examples
### Minimal Unsigned Event
```json
{
  "type": "spec:@corgi/event/v0.1.0#note",
  "created_at": 1710000000,
  "tags": [],
  "content": "🌀 just vibin"
}
```

### Signed Identity-Linked Event
```json
{
  "id": "abc123...",
  "type": "spec:@corgi/event/v0.1.0#note",
  "created_at": 1710000000,
  "did": "did:web:alice.vibes.social",
  "pubkey": "DAE227F1...",
  "tags": [],
  "content": "hello world",
  "sig": "e1f6a..."
}
```

---

## Versioning & Extensions
- Clients should gracefully ignore unknown fields.
- Future versions may define canonical ID derivation, chunking, or media support.

---

## Dependencies
- `C-ID-001` (for delegated key support)
- `C-ENC-001` (for event encoding formats)

---

## Copyright

CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

To the extent possible under law, the authors of this Corgi spec have waived all copyright and related or neighboring rights to this work.
