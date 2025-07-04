---
title: Event Encoding Formats
status: Draft
version: 0.1.0
id: spec:@corgi/event-encoding/v0.1.0
hash_id: spec:82cb6e0a
authors:
  - "@corgicontributors"
created: 2025-06-23
---
# C-ENC-001: Event Encoding Formats

## Abstract
This specification defines how Corgi events may be encoded for transmission and storage. Multiple serialization formats including JSON, MessagePack, and CBOR accommodate different performance, readability, and size constraints.

---

## Motivation
Corgi exists to allow both flexibility and composability. Rather than mandate a single serialization format, this spec outlines a negotiation-friendly approach where encoding is explicit, discoverable, and fallback-compatible. This spec allows applications to choose what fits their role without splintering UX.

---

## Supported Encodings
- `json`: UTF-8 encoded JSON (human-readable)
- `msgpack`: MessagePack binary format
- `cbor`: Concise Binary Object Representation (CBOR, RFC 8949)

All formats must encode the same core event structure as defined in `C-EVENT-001`.

---

## Encoding Declaration
### Option 1: External Declaration (Preferred)
Clients and relays should declare their supported formats via the compatibility manifest (see `C-COMPAT-001`).

```json
"encodings": ["json", "msgpack"]
```

### Option 2: Embedded in Event (Optional)
For advanced applications, events may include an `encoding` hint:
```json
{
  "type": "spec:@ocorgi/event/v0.1.0#note",
  "encoding": "msgpack",
  "payload": "<base64-encoded-bytes>"

```
This format is useful for meta-events, batch messages, or envelope containers.

---

## Transport Layer Behavior
- Relays should accept any supported encoding they advertise.
- Clients should prefer the most efficient supported format, falling back as needed.
- When transmitting via WebSocket or HTTP, the content type may indicate encoding:
  - `application/json`
  - `application/msgpack`
  - `application/cbor`

---

## Encoding Comparison (Example Event)
| Format     | Size (bytes) | Notes                     |
|------------|---------------|----------------------------|
| JSON       | 191           | Readable, large overhead   |
| MessagePack| 129           | Compact, easy drop-in      |
| CBOR       | 123           | Efficient + type-safe      |

Exact sizes vary with event complexity and field lengths.

---

## Dependencies
- `C-EVENT-001` (defines event structure)
- `C-COMPAT-001` (for capability signaling)

---

## Copyright

CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

To the extent possible under law, the authors of this Corgi spec have waived all copyright and related or neighboring rights to this work.
