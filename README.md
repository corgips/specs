# Corgi Specifications

Welcome to the Corgi Spec Garden, a modular and flexible set of specifications for building clients, relays, and tools within the decentralized social ecosystem.

Just as ECMA and TypeScript have enabled JavaScript to mature and flourish, Corgi builds on what's working in Nostr by providing a straightforward venue for further protocol development.

## 🌱 Philosophy
- **Modular**: Each spec is focused and versioned.
- **Non-authoritative**: Specs describe a way to work, not what must be done.
- **Competitive**: Competing or differently-scoped specs can co-exist using namespaced IDs.
- **Compatibility-first**: Clients and servers can unambiguously signal what they support.

---

## 📚 Spec Index
Each spec is a standalone markdown file in the `specs/` directory. Below is an index of initial specs and their roles.

| ID             | Title                               | Role                                                                                    |
| -------------- | ----------------------------------- | --------------------------------------------------------------------------------------- |
| [C-EVENT-001](./specs/c_event_001.md) | Event Schema | Defines the basic unit of content exchange: optionally signed, timestamped events.                 |
| [C-ID-001](./specs/c_id_001.md) | Delegated Identity & Key Management | Outlines identities that can be derived from wallet-compatible seeds and use delegation chains. |
| [C-DID-001](./specs/c_did_001.md) | Human-Readable Identity via DID | Describes how DID documents link keys to user-friendly names like `@alice.vibes`. |
| [C-ENC-001](./specs/c_enc_001.md) | Event Encoding Formats | Specifies allowed serialization formats (e.g. JSON, MessagePack, CBOR). |
| [C-COMPAT-001](./specs/c_compat_001.md) | Compatibility Manifest | Defines how clients and relays declare supported features and spec versions. |
| [C-ERROR-001](./specs/c_error_001.md) | Error and Incompatibility Event Format | Defines an event type for reporting errors, incompatibilities, and processing issues. |
| [C-SPEC-001](./specs/c_spec_001.md) | Spec Publishing and Governance | Explains the self-assigned ID system, spec lifecycle stages, and community process. |

---

## 📁 Folder Structure

```
/
├── README.md              # this file
├── specs/                 # protocol specifications
│   ├── C-EVENT-001.md
│   ├── C-ID-001.md
│   ├── C-DID-001.md
│   ├── C-ENC-001.md
│   ├── C-ERROR-001.md
│   ├── C-COMPAT-001.md
│   ├── C-SPEC-001.md
│   └── ... 
├── schemas/               # json schemas
│   ├── note.v0.1.0.json
│   ├── reply.v0.1.0.json
│   ├── profile_update.v0.1.0.json
│   ├── ...
└── tools/                # scripts and utilities
    ├── generate-spec-id.py
    └── validate-spec.py
```

---

## ✍️ Proposing a New Spec
See [./spec/c_spec_001.md](./specs/c_spec_001.md)

---

## 🔐 License
CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

To the extent possible under law, the authors of this Corgi spec have waived all copyright and related or neighboring rights to this work.
