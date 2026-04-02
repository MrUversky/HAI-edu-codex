# Review Monitor Scenario Guide

## Best fit
Use when a team needs to turn reviews or feedback into a cleaner signal layer.

## Required context
- which review source matters
- that the skill should only collect and normalize raw review data
- what minimal human check is required before downstream processing

## Input sources
- copied review bundles
- exported comments
- support feedback exports
- survey comment exports

## Output contract
- normalized raw review packet
- obvious duplicates or empty noise removed
- one short handoff note for downstream processing

## Human review point
A person confirms that the raw packet is usable before the next step processes it.

## Fallback and integration path
- default workshop mode: pasted or exported raw review data
- if an external source is mentioned, document it as a future guide unless access is truly available
- keep the source list bounded and explicit
- do not ask for the concrete export or bundle until the runtime step

## Canonical layout
- `.agents/skills/review-monitor/SKILL.md`
- optional `.agents/skills/review-monitor/references/`
- optional `.agents/skills/review-monitor/scripts/`
- optional `.agents/skills/review-monitor/integration_notes.md`
