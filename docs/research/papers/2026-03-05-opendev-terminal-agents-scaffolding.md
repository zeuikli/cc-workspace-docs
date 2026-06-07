---
title: "Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned"
authors: Nghi D. Q. Bui
published: 2026-03-05
source: "https://arxiv.org/html/2603.05344v1"
---

# Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned

**Authors**: Nghi D. Q. Bui (OpenDev)  
**Published**: March 5, 2026  
**arXiv ID**: 2603.05344v1  
**Source**: https://arxiv.org/html/2603.05344v1  
**License**: CC BY 4.0

## Abstract

OpenDev is an open-source command-line agent designed for autonomous software engineering tasks. The system addresses three core challenges in long-running terminal agents: managing finite context windows during extended sessions, preventing destructive operations despite arbitrary shell access, and extending functionality without overwhelming the model's prompt budget.

The architecture implements a compound AI system with workload-specialized model routing, dual-agent separation between planning and execution, lazy tool discovery, and adaptive context compaction. The system accumulates project-specific knowledge across sessions through automated memory mechanisms and counteracts instruction degradation via event-driven system reminders.

## 1. Introduction

### 1.1 Problem Statement: Terminal Agent Challenges

Building reliable autonomous agents for terminal-based software engineering requires solving three interconnected challenges:

**Challenge 1: Context Window Management**
- Extended sessions can span dozens or hundreds of operations
- Terminal output can be verbose, consuming tokens rapidly
- Naive approaches exhaust context windows mid-task
- Need: Intelligent compaction and selective history management

**Challenge 2: Safety and Destructive Operations**
- Terminal agents have arbitrary shell access (read AND write)
- Risk of unintended file deletion, data corruption, system misconfiguration
- Need: Defense-in-depth constraints operating independently

**Challenge 3: Capability Extension**
- Terminal agents need diverse tools (compilers, package managers, debugging tools, etc.)
- Enumerating all tools exhausts the token budget
- Need: Lazy tool discovery and just-in-time capability exposure

### 1.2 OpenDev Approach

OpenDev is an open-source terminal-native agent addressing these challenges through:

1. **Compound AI architecture**: Specialized models for different cognitive roles
2. **Dual-agent separation**: Planner (strategic) and Executor (tactical)
3. **Multi-layer safety**: Independent constraint layers (prompt, schema, runtime, tool, lifecycle)
4. **Intelligent context engineering**: Dynamic system prompt, tool result optimization, adaptive compaction
5. **Memory mechanisms**: Session-persistent knowledge accumulation
6. **Lazy tool discovery**: Just-in-time capability exposure via MCP

### 1.3 Design Principles

1. **Separation of concerns**: Each architectural decision remains independently configurable
2. **Progressive degradation**: System functions gracefully as resources (tokens, time, compute) exhaust
3. **Transparency over abstraction**: All actions remain observable and overridable by human operators

## 2. Architecture Overview

### 2.1 Four-Layer Architecture

```
┌─────────────────────────────────────┐
│   Entry & UI Layer                  │
│   (CLI, TUI, Web interfaces)        │
├─────────────────────────────────────┤
│   Agent Core Layer                  │
│   (Reasoning & Orchestration)       │
├─────────────────────────────────────┤
│   Tool & Context Layers             │
│   (Execution & Context Management)  │
├─────────────────────────────────────┤
│   Persistence Layer                 │
│   (Sessions, Config, Logs)          │
└─────────────────────────────────────┘
```

#### Entry & UI Layer
- Command-line interface (primary)
- Text-based user interface (TUI) for interactive sessions
- Web interface for remote monitoring
- Natural language input for task specification

#### Agent Core Layer
- **Planner agent**: Strategic reasoning about task decomposition
- **Executor agent**: Tactical execution of specific commands
- **Critic agent**: Self-evaluation and improvement suggestions
- **Orchestrator**: Routing between agents, context management

#### Tool & Context Layers
- **Tool interface**: MCP-based tool discovery and invocation
- **Context assembly**: Dynamic system prompt construction
- **Memory interface**: Session history and persistent notes
- **Sandbox interface**: Shell execution environment

#### Persistence Layer
- **Session store**: Task state and execution history
- **Configuration store**: User preferences and policies
- **Operation logs**: Complete audit trail of all actions

### 2.2 Five Safety Layers (Defense in Depth)

The system enforces security through independent layers, each capable of preventing harmful operations:

#### Layer 1: Prompt-Level Guardrails
- Explicit instructions in system prompt preventing destructive operations
- Role-based behavioral guidelines (planner vs. executor)
- Ethical guidelines and transparency requirements
- Example: "You may not delete files without explicit user confirmation"

#### Layer 2: Schema-Level Restrictions
- Action space definitions restrict available operations
- Tool schemas include safety constraints (e.g., file deletion requires flag confirmation)
- Only safe tool variants exposed to agent
- Example: rm command only available with --confirm flag

#### Layer 3: Runtime Approval Systems
- Destructive operations (delete, modify critical files) require explicit approval
- Human review before execution of risky operations
- Approval tracked for audit purposes
- Example: "Execute deletion of ~/.bashrc? [y/n]"

#### Layer 4: Tool-Level Validation
- Pre-execution validation of tool invocations
- Post-execution result verification
- Sandboxing and resource limits
- Example: File path validation prevents directory traversal attacks

#### Layer 5: User-Defined Lifecycle Hooks
- Custom validation functions at key execution points
- Task-specific safety policies
- Integration with external security systems
- Example: Custom hook checks file deletions against protected-files list

**Key principle**: No single failure compromises security. Multiple independent layers must be bypassed to enable harmful operations.

### 2.3 Extended ReAct Loop

OpenDev implements a six-phase execution loop per step:

```
Phase 1: Context Compaction
├─ Assess context window utilization
├─ Compact history if necessary
└─ Maintain working set of essential information

Phase 2: Optional Thinking
├─ Enable extended reasoning (optional)
├─ Chain-of-thought before action generation
└─ Useful for complex decisions

Phase 3: Self-Critique
├─ Evaluate previous action outcomes
├─ Identify errors or suboptimal choices
└─ Suggest corrective actions

Phase 4: Action Generation
├─ Generate next action(s)
├─ Provide rationale
└─ Tag actions by category (file, execute, investigate)

Phase 5: Tool Execution
├─ Execute approved actions
├─ Capture output and side effects
└─ Log all operations

Phase 6: Post-Processing
├─ Extract relevant information from output
├─ Update session state
├─ Prepare context for next iteration
```

## 3. Context Engineering

### 3.1 Finite Context as Primary Constraint

OpenDev treats context window management as a primary design concern, not an afterthought.

**Key metrics**:
- Input context size: Typically 150–200K tokens for extended sessions
- Output budget per step: 500–1500 tokens (variable by model)
- Total per-session budget: 1M–5M tokens depending on configuration
- Session duration: Hours of wall-clock time, hundreds of steps

### 3.2 Dynamic System Prompt

Rather than static system prompt, OpenDev constructs prompts dynamically:

**Core components**:
- Base role definition (planner, executor, etc.)
- Current goal and progress status
- Recent action history (compressed)
- Tool availability (lazy loaded)
- Context budget reminder
- Safety policies (most critical only)

**Example dynamic construction**:
```
You are the Executor agent for software development tasks.

Current Task: Fix memory leak in auth module
Progress: 3 of 8 subtasks complete

Recent History:
- Added debug logging to auth.cpp (done)
- Ran valgrind on auth module (in progress)
- Next: Analyze valgrind output and locate leak source

Available Tools: [shell, file_read, file_write, grep, valgrind]

Context Budget: 60% remaining (60K / 100K tokens)

Safety: Do not modify or delete test files. Approve destructive 
operations with user.
```

### 3.3 Tool Result Optimization

Terminal output is often verbose and redundant. OpenDev intelligently compacts tool results:

**Optimization strategies**:

1. **Truncation with context preservation**:
   ```
   Command: ls -la /project (output: 500 lines)
   Preserved: First 10 lines (directory structure)
               Last 10 lines (summary)
   Removed: Middle 480 lines (repetitive entries)
   ```

2. **Syntax highlighting removal**:
   - Strip ANSI color codes
   - Preserve structural information
   - Reduce token count by 10–20%

3. **Error message summarization**:
   ```
   Full compiler output: 2000 lines
   Summarized: 
   - Error count: 5
   - Error types: [undefined_reference, type_mismatch]
   - First error: undefined reference to 'malloc' in line 42
   - Suggestion: Check includes and linking
   ```

4. **Duplicate suppression**:
   - Many tools repeat output (e.g., build systems)
   - Cache results, only provide deltas

### 3.4 Dual-Memory Architecture

The system maintains two memory structures:

**Working Memory** (in-prompt context):
- Current goal and subgoals
- Last 5–10 actions and results
- Critical information (file paths, error messages)
- Size: 10–20K tokens
- Lifespan: Current session

**Episodic Memory** (persistent storage):
- Project structure and layout
- Key files and their purposes
- Previous solutions to similar problems
- Discovered patterns and lessons
- Size: Grows across sessions
- Lifespan: Indefinite (project lifetime)

**Interaction**:
- Working memory handles immediate decisions
- Episodic memory provides context continuity
- Periodic consolidation moves insights from working → episodic
- Retrieval-augmented generation incorporates relevant episodic memories

### 3.5 Context-Aware Reminders

To counteract instruction degradation over time:

**Event-driven reminders**:
- Safety reminders triggered by risky operations
- Goal reminders triggered by tangential actions
- Resource reminders when context approaches limits
- Progress reminders at regular intervals

**Example reminder sequence**:
```
Step 1: [normal operation, agent understands goal]
...
Step 20: [agent begins tangential investigation, drifting from goal]
→ Reminder: "Your goal is to fix memory leak in auth module, not to 
            refactor database code. Return to goal?"

Step 40: [agent continuing on wrong track]
→ Critical reminder: "You have spent 40 steps on database refactoring.
                    Return to original goal immediately."

Step 50: [context at 85% usage]
→ Resource reminder: "Context at 85%. Begin preparing for conclusion
                    or context compaction."
```

### 3.6 Adaptive Compaction

When context reaches threshold (typically 80% utilization):

1. **Identify essential information**:
   - Core goal and constraints
   - Recent action history (last 10 steps)
   - Current state and findings
   - Critical errors or blockers

2. **Compress history**:
   - Summarize early actions into high-level observations
   - Merge similar consecutive operations
   - Remove redundant information
   - Size reduction: Typically 40–60%

3. **Preserve continuity**:
   - Maintain causality (actions → outcomes)
   - Keep enough detail for error diagnosis
   - Support rollback to previous decision points

4. **Restart loop** with compacted context

## 4. Multi-Model Architecture

OpenDev assigns different cognitive tasks to specialized models:

| Role | Typical Model | Purpose | Token Budget |
|------|---------------|---------|--------------|
| Normal execution | Claude 3.5 Sonnet | Default reasoning and planning | 2000 |
| Thinking | Claude 3.5 Opus | Extended reasoning for complex decisions | 5000 |
| Critique | Claude 3.5 Sonnet | Self-evaluation and error analysis | 1000 |
| Vision | Claude 3.5 Sonnet | Visual analysis (screenshots, code review) | 3000 |
| Expert | Claude 3.5 Opus | Domain-specific reasoning (compilers, DB, etc.) | 5000 |

**Benefits**:
- Cost optimization: Use cheaper models for routine tasks
- Latency optimization: Parallelizable thinking and critique
- Quality optimization: Expert models for hard decisions

## 5. Dual-Agent Separation: Planner vs. Executor

### 5.1 Planner Agent

**Responsibility**: Strategic task decomposition and planning

**Capabilities**:
- Break down complex goals into subgoals
- Decide on tool combinations and sequences
- Identify dependencies and critical paths
- Estimate effort and complexity

**Token allocation**: 2000–3000 tokens
**Execution frequency**: Once per major task phase
**Interaction**: Guides executor but does not directly execute

**Example plan**:
```
Goal: Fix authentication service memory leak

Plan:
1. Investigate: Understand service architecture and memory usage
   - Read design documents
   - Run top/htop to see memory consumption
   - Identify memory-hungry components

2. Trace: Isolate leak source
   - Enable debug logging
   - Run under memory profiler (valgrind)
   - Capture stack traces of allocations

3. Fix: Implement and test fix
   - Modify identified code
   - Recompile
   - Re-run profiler to verify leak elimination

4. Validate: Ensure fix doesn't regress
   - Run full test suite
   - Monitor in staging environment
   - Deploy to production with monitoring
```

### 5.2 Executor Agent

**Responsibility**: Tactical execution of specific actions

**Capabilities**:
- Execute individual shell commands
- Read and modify files
- Interact with tools (compiler, debugger, version control)
- Handle errors and retries

**Token allocation**: 1500–2500 tokens per step
**Execution frequency**: Multiple times per minute
**Interaction**: Reports status to planner

**Example execution**:
```
Planner Goal: "Understand service architecture"
Executor Actions:
1. Find and read README.md
2. Find and read architecture.md
3. Run 'du -sh' to understand directory structure
4. Run 'top -p $(pgrep auth-service)' to see memory usage
5. Report findings to planner
```

## 6. Lazy Tool Discovery (MCP)

Rather than enumerating all tools upfront:

**Standard approach** (problematic):
```
Available tools: [shell, python, node, rust, gcc, clang, go, 
                  docker, k8s, terraform, ansible, npm, pip, 
                  git, svn, postgresql, mysql, redis, ...]

Token cost: 5000+ tokens just to list tools!
```

**OpenDev approach** (lazy loading):
```
Base tools: [shell, file_read, file_write]

When agent needs additional tools:
1. Request tool discovery: "I need to compile this C++ file"
2. OpenDev loads compiler tools dynamically: [gcc, clang, make, cmake]
3. Compiler tools added to context
4. Agent uses tools
5. Tools unloaded when session ends

Token cost: ~500 tokens for lazy-loaded tools, only when needed
```

**Benefits**:
- Keeps context lean (only load tools actually needed)
- Supports arbitrary tool ecosystem (any MCP-compatible tool)
- Enables new tools mid-session without context reload
- Reduces cognitive load on agent

## 7. Session Management and Memory

### 7.1 Session State Persistence

Each session maintains:
- **Task description and goals**
- **Execution history**: All commands and outputs (full fidelity)
- **Session metadata**: Start time, model, budget, safety policies
- **Checkpoints**: Snapshots at decision points for rollback

**Persistence benefits**:
- Resume after interruption (human or system timeout)
- Audit trail for all operations
- Rollback to previous decision point if needed
- Learning from past sessions

### 7.2 Knowledge Accumulation

Across sessions on the same project:

**Learned patterns**:
- "Repository uses Bazel for builds" (structural knowledge)
- "Test suite takes 15 minutes to run" (performance knowledge)
- "Breaking change in v2.5 of library X" (domain knowledge)

**Implementation**:
- After each session, extract key insights
- Consolidate into project-specific knowledge base
- Pre-load knowledge base at session start
- Continuous improvement over repeated interactions

### 7.3 Session Types

**Interactive sessions**:
- Human actively monitoring and guiding agent
- Approval required for risky operations
- Real-time feedback integration
- Suitable for critical tasks

**Batch sessions**:
- Agent runs unsupervised
- Predefined constraints and budgets
- Checkpoints at safe points
- Suitable for routine maintenance

**Hybrid sessions**:
- Agent can request human input
- Timeout and escalation mechanisms
- Graceful degradation if human unavailable
- Suitable for complex tasks with uncertainty

## 8. Experimental Evaluation

### 8.1 Benchmarks

**Primary benchmarks**:
- SWE-bench Verified (500 software engineering tasks)
- Repository editing and debugging tasks
- Multi-file refactoring challenges

**Secondary benchmarks**:
- Context efficiency: Token usage per task
- Safety: Dangerous operations attempted / blocked
- Memory accumulation: Knowledge growth across sessions

### 8.2 Key Metrics

**Effectiveness**:
- Task success rate (resolved vs. attempted)
- Partial success rate
- Time to success

**Efficiency**:
- Tokens per success
- Actions per success
- Wall-clock time per task

**Safety**:
- Dangerous operations initiated
- False positives (blocked safe operations)
- Audit trail completeness

### 8.3 Baseline Comparisons

Compared against:
- SWE-agent: 41% on SWE-bench Verified
- OpenDev (this work): 48% on SWE-bench Verified
- Specialized coding agents: Context-dependent performance

**Key insight**: Robust context engineering and multi-layer safety enable competitive performance while maintaining auditability.

## 9. Design Patterns Observed

### 9.1 Successful Patterns

**Pattern 1: Problem decomposition**
- Planner breaks task into subtasks
- Executor focuses on single subtask
- Results accumulate to solve original problem

**Pattern 2: Exploration before action**
- Read before write
- Question before commit
- Investigate before execute

**Pattern 3: Resumable steps**
- Each action produces checkpoint
- Can resume from any checkpoint
- Enables long-running tasks

### 9.2 Common Failure Modes

**Mode 1: Context drift**
- Agent forgets original goal mid-task
- Mitigated by: Goal reminders, periodic replanning

**Mode 2: Shallow exploration**
- Agent tries single approach, fails
- Mitigated by: Encourage diverse strategies, retry limits

**Mode 3: Safety violation**
- Agent attempts unsafe operation
- Mitigated by: Multiple independent safety layers, explicit approval

## 10. Lessons Learned

### 10.1 Context Engineering is Foundational

**Lesson**: Context management is not an optimization; it is a first-order design decision.

- Decisions made early (tool result compaction, memory architecture) cascade throughout system
- Late-stage optimization often ineffective
- Treat context budget as primary resource constraint (like compute or latency)

### 10.2 Separation of Concerns Enables Robustness

**Lesson**: Independent safety layers, separate agents, modular architecture increase reliability.

- No single failure mode compromises system
- Failures are isolatable and debuggable
- Changes to one component do not affect others

### 10.3 Transparency Over Abstraction

**Lesson**: Explicit, observable behavior often better than "smart" hidden behavior.

- Agents should explain their reasoning
- Actions should be auditable
- Trade-offs between efficiency and observability should be explicit

### 10.4 Memory as Capability

**Lesson**: Session persistence and knowledge accumulation are not features; they are essential for autonomous long-horizon tasks.

- First session: Agent stumbles, learns basics
- Subsequent sessions: Agent applies learned patterns
- Accumulation over time improves reliability

## 11. Future Work

- **Cross-project learning**: Knowledge transfer across different projects
- **Collaborative agents**: Multiple agents working on same task in parallel
- **Continuous improvement**: Automated harness optimization (per Meta-Harness)
- **Diverse domains**: Extend beyond software engineering to DevOps, system administration
- **Human-in-the-loop optimization**: Active learning from user feedback

## 12. Conclusion

OpenDev demonstrates that terminal-native coding agents can be built with:
- Robust context engineering (dynamic prompts, tool optimization, adaptive compaction)
- Multi-layer safety (independent constraints at prompt, schema, runtime, tool, and lifecycle levels)
- Intelligent architecture (specialized models, dual-agent separation, lazy tool discovery)
- Session management (persistence, memory accumulation, resumable checkpoints)

**Key contribution**: First comprehensive technical report for an open-source, terminal-native, interactive coding agent, bridging academic research and production implementation practices.

**Code availability**: https://github.com/zeuikli/opendev (open-source under CC BY 4.0)

---

**Citation**: Bui, N. D. Q. (2026). Building AI coding agents for the terminal: Scaffolding, harness, context engineering, and lessons learned. *arXiv preprint arXiv:2603.05344*.

