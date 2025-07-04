---
title: Compatibility Manifest
status: Draft
version: 0.1.0
id: spec:@corgi/compatibility-manifest/v0.1.0
hash_id: spec:TODO
authors:
  - "@corgicontributors"
created: 2025-06-23
---
# C-COMPAT-001: Compatibility Manifest

## Abstract
This spec defines a machine-readable manifest that clients, relays, and agents can use to declare which Corgi specs, event types, and encoding formats they support. It promotes compatibility without requiring central enforcement.

---

## Motivation
In a modular protocol ecosystem, implementations must communicate what they support. Instead of enforcing strict conformance, Corgi encourages flexible compatibility signaling. This lets clients adapt dynamically and surface ecosystem health organically.

---

## Manifest Format
The manifest is a JSON object containing:
- Agent identity
- Supported spec versions
- Accepted event types
- Signature/auth modes
- Encoding formats

```json
{
  "agent": "corgi-client-x",
  "version": "0.3.1",
  "supports": {
    "specs": {
      "@corgi/event/v0.1.0",
      "@corgi/id/v0.1.0",
      "@corgi/did/v0.1.0"
    },
    "types": [
      "spec:@corgi/event/v0.1.0#note",
      "spec:@corgi/event/v0.1.0#profile_update",
      "spec:@corgi/event/v0.1.0#reaction",
      "spec:@corgi/event/v0.1.0#boost"
    ], 
    "auth_modes": ["unsigned", "signed", "delegated"],
    "encodings": ["json", "msgpack", "cbor"]
  }
}
```

---

## Usage
- Clients and relays **should publish** their manifest at a known URL or via metadata events.
- Clients **should display** compatibility when interacting with relays.

This allows tools and dashboards to collect and visualize manifests to track adoption.

---

## Manifest Field Reference
- `agent`: Human-readable identifier.
- `version`: Software version of the agent.
- `supports.specs`: List of versioned spec IDs.
- `supports.types`: List of supported event `type` strings.
- `supports.auth_modes`: Accepted event authentication modes.
- `supports.encodings`: Accepted serialization formats.

---

## Example Relay Manifest
```json
{
  "agent": "corgi-relay",
  "version": "0.1.0",
  "supports": {
    "specs": {
      "@corgi/event/v0.1.0",
      "@corgi/id/v0.1.0"
    },
    "types": [
      "spec:@corgi/event/v0.1.0#note",
      "spec:@corgi/event/v0.1.0#profile_update",
      "spec:@corgi/event/v0.1.0#reaction"
    ],
    "auth_modes": ["signed"],
    "encodings": ["json"]
  }
}
```
---

## Compatibility Headers

Senders MAY embed `intended_for` and `required_support` hints in event metadata.

```json
"meta": {
  "intended_for": ["CorgiNotes", "WagmiWave"],
  "required_support": ["spec:@corgi/event/v0.1.0#video"]
}
```

`intended_for` allows for feature targeting, scoped deployment as far as rendering preferences go, and multi-client A/B testing. 

`required_support` allows clients without support to fallback gracefully or alert in the UI under debugging conditions.

---

## Considerations
- Spec support may be partial; manifests are **informative**, not binding.
- Manifest claims should be considered **hints**, not guarantees.
- Unknown fields should be ignored for forward compatibility.

---

## Future Extensions
- Declare supported `media_types`, languages, moderation policies
- Signed manifests for trust assessment
- Real-time discovery via relay endpoints

---

## Dependencies
- `C-EVENT-001` (for event types)
- `C-ID-001`, `C-DID-001` (for auth modes)
- `C-ENC-001` (for encoding declarations)

---

## Copyright

CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

To the extent possible under law, the authors of this Corgi spec have waived all copyright and related or neighboring rights to this work.
