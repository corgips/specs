# Corgi Design Philosophy

Corgi specifications are not a monolithic standard, but an evolving collection. They are shaped by the belief that human expression, digital presence, and social coordination deserve protocols that can adapt to satisfy ever-changing needs.

---

## 🌊 Guiding Themes

### 1. **Specifications as Description, Not Rule**
Corgi specs are modular and descriptive. They do not dictate behavior. They describe it. Developers are encouraged to adapt, remix, or extend specs based on context and need.

### 2. **Development without Gatekeeping**
Specs evolve in the garden. Anyone can author a spec using namespaced or hash-based IDs. Compatibility is signaled via clear manifests. Discovery is social, not enforced.

### 3. **Minimum Viable Interoperability**
The goal is not to enforce sameness but to provide shared interfaces that allow systems to communicate. Relays and clients can implement only what they need.

### 4. **Trust Is a Spectrum**
Corgi allows for events to be **signed or unsigned**. While cryptographic signatures enable authenticity and integrity, unsigned events are also valid and useful — especially for:
- Bots, relays, mirroring and ephemeral agents
- Anonymous or pseudonymous expression
- Secure channels

### 5. **Delegated Identity as the Norm**
In a world of wallets and signatures, identities in Corgi are delegable and derived from keys that are managed by existing cryptographic tools. Root identities can sign scopes and expiry windows, enabling safer, scoper-specific keys for day-to-day use.

### 6. **Event-First, Graph-Friendly**
The atomic unit of the network is the event. Events are timestamped, optionally verifiable, and can form graphs of interaction — threads, likes, presence beacons, you name it. This allows applications to freely explore temporal, spatial, or semantic relationships.

### 7. **Encoding Is Negotiable**
JSON is friendly. MessagePack and CBOR are compact. The specs do not demand one over the other — instead, agents can declare or negotiate their encoding. This supports a range of human legibility and machine efficiency.

### 8. **Weirdness Is a Feature**
Experimental clients, playful event types, subjective vibes — these are not outliers. They are expected. The specs aim accommodate novelty, not suppress it.

---

## The Social Layer Is Primary
Corgi specs exists to empower people to make meaning together. That means:
- Prioritizing clarity over complexity
- Supporting both permanent and ephemeral presence
- Letting communities operate with full agency and optionality.
- Making room for uses that don’t feed engagement metrics

---

## Final Thought
Corgi is a bet on specifications that evolve and grow. It’s scaffolding for collaboration, experimentation, and emergent culture.
