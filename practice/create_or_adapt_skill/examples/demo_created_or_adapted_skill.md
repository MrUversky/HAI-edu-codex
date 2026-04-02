# Created or Adapted Skill Example

## Skill name
resume-analysis

## Purpose
Help an HR partner review a bounded batch of resumes against one specific vacancy.

## Trigger phrases
- помоги разобрать резюме по этой вакансии
- сделай первый проход по кандидатам
- структурируй эту пачку резюме

## Inputs
- vacancy description
- criteria for the role
- one bounded batch of resume files or pasted resume text
- optional recruiter notes

## Outputs
- normalized candidate summaries
- fit signals
- open questions
- risk flags
- next review recommendation

## Human review point
A person must review every recommendation before interview or hiring decisions.

## Fallback or integration notes
Default workshop mode is file-based or pasted-text input. No applicant tracking system write-back happens by default.

## Canonical layout
- `.agents/skills/resume-analysis/SKILL.md`
- optional `.agents/skills/resume-analysis/references/`
- optional `.agents/skills/resume-analysis/scripts/`
- `.agents/skills/resume-analysis/validation_report.md`

## Guardrails
- do not automate hiring decisions
- do not invent qualifications
- do not hide uncertainty
- do not produce hidden scoring claims

## Success conditions
- the review becomes faster to scan
- open questions become clearer
- human decision quality improves

## Out of scope
- automatic candidate rejection
- interview scheduling
- ATS write-back without explicit approval
