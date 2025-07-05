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
Defines the base schema for events, the atomic units of data in the network. Events may be signed or unsigned and are intended to be minimal, extensible, and interoperable.

---

## Motivation
Events are the foundation of the Corgi ecosystem. They represent actions like posting, reacting, broadcasting presence, or sending ephemeral data. This spec standardizes their structure while allowing flexibility in encoding and authentication.

---

As a baseline events are as described in [NIP-01 `0c99352`](https://github.com/nostr-protocol/nips/blob/0c993526f0c662af44fdf562dfc74f32521df9bb/01.md). Added fields of `type`, `did`, and `sig` optionality are the main differences at this time.

## Event Structure
```json
{
  "event_id": "<string>",
  "created_at": <unix timestamp>,
  "pubkey": "<string> (optional)",
  "type": "<string>",
  "kind": <16-bit unsigned integer>,
  "tags": [
    [<string>...],
    // ...
  ],
  "content": "<string>",
  "sig": "<string> (optional)"
}
```

### Fields
- id: 32-byte lowercase hex-encoded sha256 digest of serialized event data.
- created_at: Unix timestamp in seconds.
- pubkey (optional): 32-byte lowercase hex-encoded public key of the sender. Required if `sig` is present.
- **type**: String identifyier for event type (see [Type Registry](types.json)).
- kind: 16-bit unsigned integer for compatibility with nostr
- tags: List of lists that may contain arbitrary type-specific strings.
- content: Raw content, markdown, or JSON-encoded string.
- **sig** (optional): A digital signature. Required for identity verification.

### `type`
The `type` field MUST reference a defined event type within the spec garden. It takes the form:
```json
"type": "spec:@namespace/specname/version#typename"
```
Clients and relays SHOULD use this value to determine how to parse or display an event. Schemas for machine-readable validation MAY be provided in the `types:` section of the spec’s frontmatter.

---

## Authentication
Signatures are **optional**, but encouraged for events linked to identity or long-term state. They are computed according to https://bips.xyz/340.

### Valid modes:
- **Unsigned**: No `sig` or `pubkey`. Treated as anonymous or ephemeral.
- **Signed**: Includes `sig` and `pubkey`. Allows verification.
- **Delegated**: Uses derived keys and delegation proofs (see `C-ID-001`).

Clients and relays may:
- Accept unsigned events unless policy restricts them
- Show visual indicators of verification status
- Allow filters based on trust level

---

## Examples
### Minimal Unsigned Event
```json
{
  "id": "9a2b1c4d..."
  "type": "spec:@corgi/event/v0.1.0#note",
  "kind": 1,
  "created_at": 1710000000,
  "tags": [],
  "content": "🌀 just vibin"
}
```

### Signed Identity-Linked Event
```json
{
  "id": "a1b2c3d4...",
  "type": "spec:@corgi/event/v0.1.0#note",
  "created_at": 1710000000,
  "did": "did:web:alice.vibes.social",
  "pubkey": "dae227f1...",
  "tags": [],
  "content": "hello world",
  "sig": "e1f6a5f2..."
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
