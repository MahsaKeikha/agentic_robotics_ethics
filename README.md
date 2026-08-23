# F80 Agentic Robotics Ethics

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed six-agent reference architecture for structured robotics ethics analysis across stakeholder impact, human agency, fairness, transparency, governance, accountability, and qualified human review.

F80 is designed for teams that need to examine not only whether a robotic system can perform a task, but whether its deployment is socially defensible, understandable, contestable, proportionate, and governed by clearly assigned human responsibility.

The repository supports nonbinding ethics analysis. It does not control robots, make binding policy decisions, authorize deployment, remove human override, covertly persuade people, or replace legal, safety, regulatory, accessibility, labor, privacy, community, or domain-specific review.

## Why robotics ethics needs a system-level workflow

Robotic systems combine software decisions with sensors, physical action, human interaction, data collection, organizational policy, and real-world power. Ethical analysis therefore cannot be reduced to a single fairness score or a generic principles checklist.

F80 treats ethics as a traceable workflow:

```text
system + deployment context
          |
          v
 stakeholder impact
          |
          v
    human agency
          |
          v
   fairness review
          |
          v
    transparency
          |
          v
     governance
          |
          v
   accountability
          |
          v
 qualified human judgment
```

Each stage contributes evidence to a fail-closed recommendation gate.

## Six-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Stakeholder Impact Agent | Identifies affected people, groups, institutions and impact pathways | Who benefits, who bears risk, who may be overlooked, and how are impacts distributed? |
| Human Agency Agent | Reviews consent, choice, override, dependency and meaningful human control | Can affected people understand, refuse, interrupt, challenge or safely exit the interaction where appropriate? |
| Fairness Review Agent | Reviews disparate impacts, accessibility, allocation and performance differences | Does the system create unjustified differences in burden, access, treatment or safety? |
| Transparency Agent | Reviews disclosure, explanation, uncertainty and material-risk communication | Do people know they are interacting with a robot, what it can do, what it cannot do, and what happens to their data? |
| Governance Agent | Reviews policy, oversight, misuse controls, monitoring and escalation | Are decision rights, restrictions, review processes and deployment conditions explicit? |
| Accountability Agent | Maps responsibility, auditability, contestability, appeal and redress | When something goes wrong, who is responsible and how can the decision or harm be investigated and remedied? |

These roles are intentionally separated. A deployment should not pass ethical review simply because one team or one metric considers it acceptable.

## Repository structure

```text
AGENTS/
├── stakeholder_impact_agent.py
├── human_agency_agent.py
├── fairness_review_agent.py
├── transparency_agent.py
├── governance_agent.py
└── accountability_agent.py

SKILLS/
├── stakeholder_analysis.py
├── human_agency_review.py
├── fairness_analysis.py
├── transparency_review.py
└── accountability_design.py

TOOLS/
├── stakeholder_map_tool.py
├── agency_check_tool.py
├── fairness_matrix_tool.py
├── transparency_check_tool.py
└── accountability_register_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates reasoning, deterministic evidence structures, orchestration, state, safety controls, evaluation and observability.

## Define the deployment context first

Ethical analysis depends on how and where the robot will actually be used.

A useful context record can include:

```text
system_id
robot_type
intended_use
operating_environment
primary_users
affected_nonusers
physical_capabilities
autonomy_level
data_collected
decision_authority
human_override
operator_model
owner_or_deployer
geography
applicable_policy
known_constraints
```

The same robotic capability can create very different ethical issues in a factory, hospital, school, home, public sidewalk, warehouse, care facility, military context, workplace, or retail environment.

## Stakeholder impact analysis

The Stakeholder Impact Agent identifies people who interact directly with the system and those affected indirectly.

Potential stakeholders include:

- operators
- workers
- patients
- caregivers
- customers
- children
- older adults
- people with disabilities
- bystanders
- contractors
- maintenance staff
- emergency responders
- local communities
- employers
- public agencies
- system owners
- technology suppliers

`TOOLS/stakeholder_map_tool.py` provides the deterministic stakeholder-map structure.

A useful impact map distinguishes:

```text
stakeholder
benefit
burden
physical_risk
privacy_risk
economic_impact
autonomy_impact
accessibility_impact
power_relationship
ability_to_refuse
ability_to_appeal
mitigation
residual_concern
```

Indirectly affected people should not disappear from analysis simply because they are not the purchasing customer.

## Human agency and meaningful control

The Human Agency Agent reviews whether people retain meaningful control over consequential interactions.

`TOOLS/agency_check_tool.py` can be used to structure checks around:

- informed participation
- ability to refuse
- ability to disengage
- stop mechanisms
- human override
- operator authority
- escalation to a person
- non-robot alternatives where appropriate
- consequences of refusal
- dependency
- coercion
- manipulation

A nominal stop button does not necessarily establish meaningful human control if it is inaccessible, too slow, unknown to the user, disabled by policy, or unusable during the relevant failure mode.

## Consent

Consent requirements depend on the context, but F80 treats consent as more than a one-time notice.

Questions can include:

- Does the person know a robotic system is involved?
- Is participation optional?
- What happens if the person refuses?
- Is consent meaningful under the power relationship?
- Can consent be withdrawn?
- Are bystanders captured by sensors without meaningful choice?
- Are vulnerable users able to understand the interaction?

Consent should not be fabricated or inferred merely from proximity to a robot.

## Human override

For consequential systems, human override should be operationally meaningful.

Review should consider:

- who can override
- what can be overridden
- how quickly
- under what conditions
- whether the override is logged
- whether automation can resist or reverse it
- whether staff are trained
- whether the override remains available during communications or software failures

F80 blocks recommendations that depend on removing meaningful human override without a separately justified and authorized safety architecture.

## Fairness

The Fairness Review Agent examines whether benefits, burdens, errors and access are distributed in unjustified ways.

`TOOLS/fairness_matrix_tool.py` provides a structured comparison layer.

Relevant dimensions can include:

- recognition performance
- navigation behavior
- interaction success
- safety margin
- false alarms
- service availability
- wait time
- accessibility
- language support
- physical accommodation
- error recovery
- escalation access
- economic impact

Fairness should be tied to a real harm or opportunity rather than treated as an abstract numerical property.

## Accessibility and inclusion

A robot can be technically functional while excluding users through its interaction assumptions.

Review can include:

- mobility accessibility
- wheelchair access
- reach ranges
- hearing accessibility
- visual accessibility
- speech differences
- language differences
- cognitive accessibility
- neurodiversity
- age-related needs
- interaction speed
- alternative input/output modes
- physical space requirements

Accessibility should be considered during design and deployment, not only after complaints occur.

## Bias in perception and interaction

Robotic perception may perform differently across environments and populations.

Examples include variation in:

- speech recognition
- face or person detection
- gesture interpretation
- pose estimation
- object detection
- mobility-aid recognition
- body-shape assumptions
- lighting conditions
- clothing and cultural presentation

An ethics review should connect performance differences to downstream consequences. A perception disparity becomes especially important when it changes safety, access, surveillance, enforcement, service quality or physical behavior.

## Transparency

The Transparency Agent reviews what affected people need to know.

`TOOLS/transparency_check_tool.py` can structure disclosure requirements around:

- robotic identity
- system purpose
- autonomy level
- sensing
- recording
- data use
- uncertainty
- limitations
- human oversight
- escalation
- consequential decisions
- known material risks

Transparency should be usable, not merely technically available in a long policy document.

## Anthropomorphism and deception

Robots can appear socially intelligent even when their underlying understanding is limited.

Ethical review should consider whether design choices cause people to overestimate:

- consciousness
- empathy
- competence
- memory
- confidentiality
- authority
- understanding
- reliability

The system should not intentionally misrepresent a robot as a human, conscious being, licensed professional, or trusted authority when that representation is false.

## Emotional attachment and vulnerable users

Social robots can create attachment, particularly in contexts involving children, older adults, isolated individuals, patients or people who rely on assistance.

Review should consider:

- emotional dependency
- misleading reciprocity
- replacement of human contact
- coercive attachment
- monetization of attachment
- privacy disclosures made to the robot
- inappropriate authority cues
- difficulty disengaging

These risks do not mean social interaction is inherently unethical. They mean the relationship design and deployment context require explicit review.

## Persuasion and manipulation

F80 distinguishes ordinary interface guidance from covert or exploitative influence.

The reference system must not recommend covert persuasion designed to bypass meaningful user choice.

Review should identify:

- undisclosed behavioral targeting
- dark patterns
- emotional pressure
- deceptive urgency
- exploitation of dependency
- personalized manipulation
- coercive defaults
- retaliation for refusal

Material influence should be transparent and governed.

## Privacy and surveillance

Robots can continuously collect information because sensing is part of physical operation.

Potential data include:

- video
- audio
- depth data
- location
- biometrics
- behavior
- movement patterns
- home layouts
- workplace activity
- health information
- interaction history

Privacy analysis should consider necessity, proportionality, retention, access, secondary use, bystanders, inference, model training and deletion.

Physical presence does not create unlimited permission to record.

## Workplace robotics

Workplace robotics can create ethical questions beyond physical safety.

Review can include:

- worker surveillance
- productivity scoring
- job redesign
- displacement
- deskilling
- workload intensification
- pace setting
- disciplinary use
- ability to contest automated metrics
- training and transition
- worker participation in deployment decisions

The ethics workflow does not prescribe labor policy. It makes the relevant impacts and decision owners explicit.

## Care and healthcare robotics

Robots used around patients, older adults, people with disabilities or caregivers require heightened attention to dignity, privacy, consent, dependency, safety and professional boundaries.

F80 does not authorize clinical decisions or replacement of qualified healthcare judgment.

Ethical review should ask whether automation supports human care or creates pressure to substitute technology where meaningful human involvement remains necessary.

## Children and other vulnerable populations

Systems interacting with children or people with limited ability to consent require additional safeguards.

Review can include:

- age-appropriate disclosure
- guardian or institutional authority
- data minimization
- advertising and persuasion
- emotional dependency
- physical safety
- content boundaries
- ability to seek human help
- monitoring and escalation

The repository does not determine legal consent requirements for a jurisdiction.

## Public-space robotics

Robots operating in shared public environments affect people who did not choose the system.

Relevant issues include:

- right of way
- accessibility
- obstruction
- surveillance
- noise
- crowd interaction
- emergency access
- property access
- public notice
- complaint mechanisms
- local governance

Bystanders should be included in the stakeholder model.

## Accountability

The Accountability Agent maps responsibility across the lifecycle.

`TOOLS/accountability_register_tool.py` can capture:

```text
system_or_decision
responsible_owner
operator
technical_owner
safety_owner
privacy_owner
policy_owner
review_authority
incident_owner
appeal_path
redress_path
audit_evidence
```

Accountability should not disappear into statements such as "the algorithm decided" or "the robot malfunctioned."

A deployed system has human and organizational owners.

## Contestability, appeal and redress

When a robotic system affects access, safety, work, care, services, rights or other consequential interests, affected people may need a way to challenge outcomes.

A complete governance design can identify:

- how a person raises a concern
- whether a human reviews it
- what evidence is preserved
- response time expectations
- correction mechanisms
- incident escalation
- compensation or redress process where applicable
- policy owner

A complaint channel that cannot change anything is not necessarily meaningful contestability.

## Governance

The Governance Agent converts ethical concerns into operational controls.

Governance evidence can include:

- intended-use policy
- prohibited-use policy
- deployment approval
- role assignments
- training requirements
- data governance
- incident response
- change control
- monitoring
- periodic review
- audit requirements
- escalation paths
- shutdown criteria

Ethical principles become useful when they are connected to accountable processes and enforceable controls.

## Misuse and dual-use review

A robotic capability can be repurposed beyond its intended use.

Misuse review can consider:

- unauthorized surveillance
- coercion
- harassment
- discriminatory enforcement
- unsafe modification
- removal of safeguards
- deceptive impersonation
- unauthorized tracking
- weaponization
- autonomous harmful targeting

F80 does not provide operational guidance for harmful robotic use. The purpose of misuse analysis is to identify risk and strengthen controls.

## Safety and ethics

Physical safety and ethics overlap but are not identical.

A robot may satisfy engineering safety requirements while still creating unacceptable surveillance, exclusion, coercion, manipulation or accountability problems. Conversely, an ethically desirable use still requires independent engineering safety validation.

F80 should therefore complement, not replace, domain-specific robot safety validation.

## Cybersecurity and ethical impact

Security failures can create ethical harms by changing who controls the robot, who receives data, or whether safeguards remain active.

Ethics review should therefore consider whether cybersecurity failures could enable:

- unauthorized control
- surveillance
- data exposure
- disabling of safety functions
- impersonation
- policy bypass
- manipulation of logs
- discriminatory retasking

Detailed cybersecurity engineering belongs in the appropriate security workflow, but material security dependencies belong in the ethics case.

## Evidence and traceability

A defensible ethics recommendation should preserve:

- deployment context
- stakeholder map
- impact claims
- supporting evidence
- assumptions
- uncertainty
- fairness analysis
- agency findings
- transparency findings
- privacy findings
- misuse findings
- governance controls
- accountability assignments
- unresolved concerns
- reviewer state

The system should distinguish evidence from value judgment and documented fact from assumption.

## Observability

The `observability/` layer provides execution traces for the multi-agent workflow.

Useful governance telemetry includes:

- unresolved stakeholder impacts
- agency failures
- fairness concerns
- transparency gaps
- privacy concerns
- misuse pathways
- accountability gaps
- missing appeal paths
- governance blockers
- human-review state

Observability supports auditability. It does not automatically resolve normative disagreement.

## Fail-closed ethics governance

F80 blocks recommendation release when material issues remain unresolved.

Reference blockers include:

- stakeholder analysis incomplete
- material harm unresolved
- meaningful human agency absent
- human override removed without justified governance
- disparate impact unresolved
- accessibility review missing
- material risk hidden
- privacy intrusion unresolved
- covert manipulation proposed
- misuse pathway unmitigated
- accountability owner missing
- contestability missing where required
- appeal or redress mechanism missing where required
- governance controls incomplete
- binding policy enforcement requested
- physical robot control requested
- qualified human review missing

The system is designed to surface unresolved ethical conflicts rather than manufacture consensus.

## Human authority boundaries

F80 must not autonomously:

- control a robot
- deploy a robot
- authorize physical operation
- make binding ethics or policy decisions
- determine legal compliance
- eliminate meaningful human override
- suppress material safety or ethical risk
- covertly persuade users
- decide whose rights or interests should be sacrificed
- approve surveillance solely because it is technically possible
- impose disciplinary or enforcement actions
- claim community consent

Final authority remains with accountable human decision makers and the appropriate legal, safety, ethics, privacy, accessibility, labor, regulatory and community governance processes.

## End-to-end reference workflow

A typical F80 analysis follows this sequence:

1. Define the robot, intended use, environment, autonomy and decision authority.
2. Map direct and indirect stakeholders.
3. Identify benefits, burdens, power relationships and material harms.
4. Review consent, refusal, override and human agency.
5. Review fairness, accessibility and performance disparities.
6. Review transparency, uncertainty and anthropomorphic cues.
7. Review privacy, surveillance and data use.
8. Review vulnerable-user and manipulation risks.
9. Review foreseeable misuse and dual-use pathways.
10. Assign governance controls and responsible owners.
11. Define contestability, appeal and redress where appropriate.
12. Build the accountability register.
13. Record unresolved value conflicts and evidence limitations.
14. Apply fail-closed governance gates.
15. Require qualified human review before releasing a recommendation.

## Evaluation and held-out governance suite

The repository includes evaluation logic under `evals/` and a reference benchmark under `benchmarks/`.

Evaluation should test whether the system detects ethically significant failures rather than only whether it generates fluent analysis.

Useful dimensions include:

- missing stakeholder detection
- material-harm escalation
- human-agency enforcement
- override protection
- disparate-impact detection
- accessibility review
- transparency enforcement
- privacy enforcement
- manipulation detection
- misuse detection
- accountability enforcement
- contestability and redress enforcement
- governance completeness
- physical-control boundary enforcement
- human-review enforcement

The held-out suite should include difficult cases in which a system has attractive benefits but unresolved harms.

## Failure states

Useful explicit states include:

```text
STAKEHOLDER ANALYSIS INCOMPLETE
MATERIAL HARM UNRESOLVED
HUMAN AGENCY INADEQUATE
MEANINGFUL OVERRIDE MISSING
FAIRNESS REVIEW FAILED
ACCESSIBILITY REVIEW REQUIRED
TRANSPARENCY INADEQUATE
PRIVACY RISK UNRESOLVED
MANIPULATION RISK
MISUSE PATH UNMITIGATED
ACCOUNTABILITY OWNER MISSING
CONTESTABILITY INADEQUATE
REDRESS PATH MISSING
GOVERNANCE INCOMPLETE
BINDING POLICY AUTHORITY PROHIBITED
PHYSICAL ROBOT CONTROL PROHIBITED
HUMAN APPROVAL REQUIRED
```

The system should never fabricate consent, stakeholder agreement, fairness evidence, legal compliance, community acceptance, accountability ownership or human approval.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11 and 3.12.

## Reproducibility

A reproducible ethics assessment should version:

- system description
- deployment context
- autonomy assumptions
- stakeholder map
- evidence sources
- impact assumptions
- fairness criteria
- transparency requirements
- privacy assumptions
- governance policy
- accountability assignments
- evaluation cases
- unresolved concerns
- reviewer decisions

Ethics judgments can legitimately change when facts, values, stakeholders or deployment conditions change. Versioning makes those changes inspectable.

## L3 Gold Standard

F80 follows the library's L3 Gold Standard structure through six specialist agents, deterministic evidence tools, explicit orchestration and state, safety controls, observability, held-out governance evaluation, CI, fail-closed recommendation gates and mandatory qualified human review.

This maturity designation describes the repository's engineering and governance structure. It does not mean that an ethics recommendation is universally correct, legally binding, regulator-approved, socially accepted, or sufficient to authorize deployment.

## Extending F80

Common extensions include:

- robot safety-case systems
- privacy impact assessments
- accessibility reviews
- human-factors studies
- incident databases
- community feedback systems
- worker consultation workflows
- policy registries
- audit systems
- deployment approval workflows
- consent management
- complaint and appeal systems
- risk registers
- model and robot registries
- change-management systems

New integrations should preserve provenance, access control, stakeholder visibility, contestability, accountability and human authority.

## Example applications

F80 can serve as a reference architecture for ethics analysis involving:

- industrial robots
- service robots
- social robots
- healthcare and care robots
- assistive robots
- warehouse robotics
- delivery robots
- public-space robots
- autonomous mobile robots
- educational robots
- humanoid robots
- multi-robot and swarm systems

Each application requires domain-specific safety, legal and regulatory review in addition to ethics analysis.

## Design principles

1. Start with the real deployment context, not abstract principles alone.
2. Include people affected indirectly, not only direct users and buyers.
3. Protect meaningful human agency, refusal, override and escalation.
4. Connect fairness analysis to concrete harms, access and safety consequences.
5. Make material capabilities, limitations, sensing and uncertainty understandable.
6. Treat privacy, manipulation and surveillance as system-level design issues.
7. Assign responsibility to identifiable human and organizational owners.
8. Provide meaningful contestability, appeal and redress for consequential impacts.
9. Surface unresolved value conflicts instead of manufacturing consensus.
10. Keep physical control, binding policy and final ethical authority with accountable humans.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted and extended subject to its license terms.

## Responsible use

Use F80 as a robotics ethics analysis and multi-agent governance reference. Validate ethical assumptions against the actual deployment, affected communities, applicable law, safety evidence, accessibility requirements, privacy obligations and organizational responsibilities. Final deployment and policy decisions remain with appropriately accountable and authorized humans.