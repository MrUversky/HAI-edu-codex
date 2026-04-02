# Telegram Digest Scenario Guide

## Best fit
Use when one person or team is overwhelmed by one Telegram chat or channel.

## Required context
- what chat or channel matters
- whether the workshop mode uses:
  - exported chat data
  - or a future guided connection path
- what digest output is actually useful

## Input sources
- preferred `v1`: exported chat history
- optional advanced path: explicit group/channel connection guide

## Output contract
- grouped themes
- notable updates
- watch items
- action items
- unanswered questions

## Human review point
A person reviews the digest before using it for downstream decisions or communications.

## Fallback and integration path
- default workshop mode: exported data
- advanced guide: connection to one clearly specified Telegram source
- never imply live monitoring if only export mode is available

## Canonical layout
- `.agents/skills/telegram-digest/SKILL.md`
- optional `.agents/skills/telegram-digest/references/`
- optional `.agents/skills/telegram-digest/scripts/`
- optional `.agents/skills/telegram-digest/integration_notes.md`
