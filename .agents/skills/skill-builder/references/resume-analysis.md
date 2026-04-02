# Resume Analysis Scenario Guide

## Best fit
Use when an HR or recruiting workflow needs one structured pass over resumes for one specific vacancy.

## Required context
- company context
- the selected vacancy
- criteria for that vacancy
- whether the input is:
  - one resume
  - or a bounded batch
- what kind of recommendation is acceptable

## Input sources
- role or vacancy description
- criteria for the role
- one resume or a bounded batch of resumes
- optional recruiter or interviewer notes

## Output contract
- normalized candidate summary
- fit signals
- open questions
- risk flags
- next review recommendation

## Human review point
A human must review every recommendation before interview or hiring decisions.

## Fallback and integration path
- default workshop mode: pasted text or uploaded files
- no automatic ATS write-back in workshop mode
- do not allow vacancy-independent resume scoring

## Canonical layout
- `.agents/skills/resume-analysis/SKILL.md`
- optional `.agents/skills/resume-analysis/references/`
- optional `.agents/skills/resume-analysis/scripts/`
- optional `.agents/skills/resume-analysis/integration_notes.md`
