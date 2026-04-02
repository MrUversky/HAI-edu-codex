# Telegram Digest Scenario Guide

## Best fit
Use when one person or team is overwhelmed by one Telegram chat or channel.

## Required context
- whether the workshop mode uses:
  - exported chat data
  - or a future guided connection path
- that this skill is only preparing raw data for downstream processing

## Input sources
- preferred `v1`: exported chat history
- optional advanced path: explicit group/channel connection guide

## Output contract
- normalized raw packet from the export
- obvious noise removed
- one short human check note before downstream handoff

## Human review point
A person confirms that the export is complete enough and the raw packet can go downstream.

## Fallback and integration path
- default workshop mode: exported data
- advanced guide: connection to one clearly specified Telegram source
- never imply live monitoring if only export mode is available
- do not ask for the concrete export file until the runtime step

## Canonical layout
- `.agents/skills/telegram-digest/SKILL.md`
- optional `.agents/skills/telegram-digest/references/`
- optional `.agents/skills/telegram-digest/scripts/`
- optional `.agents/skills/telegram-digest/integration_notes.md`
