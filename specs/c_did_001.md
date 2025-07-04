---
title: Human-Readable Identity via DID
status: Draft
version: 0.1.0
id: spec:@corgi/did-aliasing/v0.1.0
hash_id: spec:e2adf7a1
authors:
  - "@corgicontributors"
created: 2025-06-23
---
# C-DID-001: Human-Readable Identity via DID

## Abstract
This spec describes how Corgi clients and relays can support human-readable identifiers via Decentralized Identifiers (DIDs). It defines how DIDs map to cryptographic keys and optionally provide display names, avatars, and service metadata, all without relying on a central authority.

---

## Motivation
Cryptographic pubkeys are difficult for humans to remember or verify. DIDs provide a flexible, decentralized method for linking a human-readable name to a verifiable document containing keys, metadata, and optional delegation rules.

---

## DID Basics
A DID is a W3C-standard identifier:
```
did:<method>:<unique-identifier>
```
Examples:
- `did:web:alice.vibes.social`
- `did:key:z6MkfooBar...`
- `did:pkh:bip122:000000000019d6689c085...`

A DID resolves to a **DID document** containing:
- Public keys
- Verification methods
- Optional service endpoints
- Human-readable metadata

---

## DID in Corgi
### DID Field in Events (Optional)
```json
{
  "type": "spec:@corgi/event/v0.1.0#note",
  "created_at": 1710000000,
  "pubkey": "DAE227F1...",
  "did": "did:web:alice.vibes.social",
  "content": "gm!"
}
```
- `did` is an optional field that helps clients resolve display info.
- Clients may use it to fetch a DID document, verify key match, and load profile data.

### DID Document Example
```json
{
  "@context": "https://www.w3.org/ns/did/v1",
  "id": "did:web:alice.vibes.social",
  "verificationMethod": [{
    "id": "#main-key",
    "type": "Ed25519VerificationKey2020",
    "controller": "did:web:alice.vibes.social",
    "publicKeyBase58": "F8kz..."
  }],
  "alias": "alice.vibes",
  "avatar": "https://alice.vibes.social/avatar.png",
  "service": [{
    "id": "#corgi",
    "type": "CorgiRelay",
    "serviceEndpoint": "wss://relay.vibes.social"
  }]
}
```

---

## Resolution Guidelines
- Clients **should** resolve DIDs and cache metadata.
- Clients **must** verify that the public key in the DID document matches or delegates to the signing key in the event.
- Fallback if resolution fails: display pubkey and treat identity as unsigned.

---

## Identity Linking & Trust
- A DID can sign a delegation proof (see `C-ID-001`).
- A DID may be listed in a compatibility manifest to indicate verified scope.
- Clients can cache and share DID → pubkey mappings for UX.

---

## Supported DID Methods (Recommended)
- `did:web` — DNS-based, great for websites or servers
- `did:key` — Purely local, wallet-derived or generated

Support for other DID methods is implementation-dependent.

---

## Security Considerations
- Always verify that a DID document’s key matches the signer or authorized delegation.
- Warn users if DID resolution fails or data is stale.
- Don’t assume that DID = unique user unless explicitly verified.

---

## Future Extensions
- DID-based group or org identifiers
- Multi-profile DID documents (e.g. work / anon / vibe mode)
- Interop with Verifiable Credentials

---

## Dependencies
- `C-ID-001` (for delegation and verification)
- `C-EVENT-001` (for DID field in events)

---

## Copyright

CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

To the extent possible under law, the authors of this Corgi spec have waived all copyright and related or neighboring rights to this work.
