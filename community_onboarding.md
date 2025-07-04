# Corgi Community Onboarding Guide

Welcome to the Corgi Spec Community — a growing ecosystem of builders, artists, researchers, and vibe coders designing the next generation of decentralized social interaction.

This guide will help you get oriented, contribute meaningfully, and find your place in the Corgi network.

---

## 🧭 What Is Corgi?
Corgi is a collection of specifications for decentralized, flexible, vibe-rich social platforms. It's:
- **Nostr-compatible**: Plugs into Nostr today, expands tomorrow
- **Modular**: Built from independent specs
- **Pragmatic**: Designed to be implementable, not ideological
- **Inclusive**: Supports weirdness, minimalism, and creativity
- **Evolving**: Always open to new ideas and soft forks

Instead of a multi-faceted protocol, Corgi is a garden — people can grow new types, prune old ones, and remix the soil of identity and interaction.

---

## 🧰 Key Concepts
- **Events**: The atomic units of content, signed or unsigned (`C-EVENT-001`)
- **Delegated Identities**: Wallet-compatible and scoped for safety (`C-ID-001`)
- **Human-Readable Names**: Via DIDs (`C-DID-001`)
- **Capability Signaling**: Clients/relays say what they support (`C-COMPAT-001`)
- **Flexible Encodings**: JSON, MessagePack, CBOR (`C-ENC-001`)
- **Spec Garden**: Open, non-authoritative spec repo (`C-SPEC-001`)

---

## 🏁 Getting Started

### 👩💻 Developers
- Fork and star the [Corgi Spec Garden](https://github.com/corgips/specs)
- Pick a spec and try implementing it in a new branch on your project
- Publish your client/relay manifest (see `C-COMPAT-001`) _somewhere_
- Contribute new event types or tools

### ✍️ Spec Authors
- Read `C-SPEC-001` for how to propose a new spec
- Use our `generate-spec-id.py` tool
- Fork the repo, add your spec, open a pull request

### 🌱 Community Members
- Join discussions on new specs, problems, and potential features.
- Propose UX ideas or client behaviors
- Translate specs, organize hackathons, or test prototypes

---

## 🤝 Community Norms
- Be supportive, curious, and constructive
- Specs describe, not dictate
- There is no “official” client or implementation
- Weirdness and divergence are both expected and encouraged

---

## 🔗 Useful Resources
- 📚 [Spec Index](./specs/README.md)
- 🔐 [generate-spec-id.py](generate-spec-id.py)
- 💬 Community forum: `#corgi` on your preferred protocol
- 🧪 Experimental client gallery (coming soon)
