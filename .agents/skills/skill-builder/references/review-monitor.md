# Review Monitor Scenario Guide

## Best fit
Use when a team needs to turn reviews or feedback into a cleaner signal layer.

## Required context
- which review source matters
- what kind of review bundle is available
- what downstream action the team wants from the result

## Input sources
- copied review bundles
- exported comments
- support feedback exports
- survey comment exports

## Output contract
- signal clusters
- urgency flags
- what changed
- suggested follow-up buckets

## Human review point
A person reviews the grouped signals before customer-facing or priority decisions.

## Fallback and integration path
- default workshop mode: pasted or exported raw review data
- if an external source is mentioned, document it as a future guide unless access is truly available
- keep the source list bounded and explicit

## Canonical layout
- `.agents/skills/review-monitor/SKILL.md`
- optional `.agents/skills/review-monitor/references/`
- optional `.agents/skills/review-monitor/scripts/`
- optional `.agents/skills/review-monitor/integration_notes.md`
