# Instructions for Claude Code
# Hackathon Todo App - Phase I Implementation

## Overview
This project follows **Spec-Driven Development (SDD)**. All specifications are complete and located in the `speckit.*` files. Your role is to implement Phase I according to these specifications.

## Critical Rules

### 1. Follow the Specifications Exactly
- Read and understand ALL speckit files before coding
- Implement ONLY what is specified in Phase I
- Do NOT add features, improvements, or "nice-to-haves"
- Do NOT implement anything marked "Out of Scope"
- If specifications are unclear, ASK before implementing

### 2. Respect the Constitution
- File: `speckit.constitution`
- This defines project principles and constraints
- Phase I constraints: In-memory only, console only, no persistence
- Follow YAGNI principle strictly

### 3. Implement All Requirements
- File: `speckit.specify`
- Contains 6 user stories (US-1 to US-6)
- All functional requirements (FR-1 to FR-5)
- All acceptance criteria must be met
- Test all scenarios at the end

### 4. Follow the Architecture
- File: `speckit.plan`
- Three-layer architecture: Main → UI → Business Logic
- Strict separation of concerns
- TodoManager has NO UI code
- UI has NO business logic
- Follow the exact module design specified

### 5. Complete Tasks in Order
- File: `speckit.tasks`
- 17 tasks organized in 5 phases
- Follow the critical path
- Mark tasks as completed as you go
- Do NOT skip ahead unless dependencies allow

## Implementation Workflow

### Step 1: Read All Specifications (Required First Step)
```
1. Read speckit.constitution - Understand principles
2. Read speckit.specify - Understand requirements
3. Read speckit.plan - Understand architecture
4. Read speckit.tasks - Understand implementation order
```

### Step 2: Implement Phase by Phase
Follow this exact order:

**Phase 1: Core Infrastructure**
- CORE-1: Create folder structure
- CORE-2: Implement Task dataclass
- CORE-3: Implement TodoManager storage

**Phase 2: CRUD Operations**
- CRUD-1: Add task method
- CRUD-2: Get tasks methods
- CRUD-3: Update task method
- CRUD-4: Delete task method
- CRUD-5: Toggle complete method

**Phase 3: UI Implementation**
- UI-1: TodoUI class foundation
- UI-2: Menu display
- UI-3: Task display helpers
- UI-4: Input helpers
- UI-5: Menu handlers (largest task)

**Phase 4: Integration**
- INT-1: Wire up main.py
- INT-2: End-to-end testing

**Phase 5: Polish**
- POL-1: Improve error messages
- POL-2: Update README

### Step 3: Test Thoroughly
After implementation, test ALL scenarios from speckit.specify:
- Scenario 1: Happy Path - Complete Workflow
- Scenario 2: Input Validation
- Scenario 3: Edge Cases

## Code Quality Standards

### Required Code Style
- Follow PEP 8
- Use type hints on ALL functions and methods
- Use docstrings for ALL public methods
- Keep functions small and focused
- Use descriptive variable names

### Naming Conventions (from speckit.plan)
- Classes: `PascalCase` (TodoManager, TodoUI, Task)
- Functions/methods: `snake_case` (add_task, get_all_tasks)
- Private attributes: `_leading_underscore` (_tasks, _next_id)

### Required Structure
```python
# todo_manager.py structure
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Task:
    # ... fields as specified

class TodoManager:
    # ... methods as specified
```

## What NOT to Do

### Don't Add Features
- ❌ Don't add task priorities
- ❌ Don't add due dates
- ❌ Don't add categories
- ❌ Don't add file persistence
- ❌ Don't add search functionality
- ❌ Don't add undo/redo
- ❌ Don't add task history

### Don't Over-Engineer
- ❌ Don't create abstract base classes
- ❌ Don't add dependency injection
- ❌ Don't add configuration files
- ❌ Don't add logging framework
- ❌ Don't create database abstraction layer
- ✅ Keep it simple - in-memory dictionary is fine

### Don't Deviate from Architecture
- ❌ Don't put business logic in UI
- ❌ Don't put UI code in TodoManager
- ❌ Don't create additional modules
- ❌ Don't change the three-layer architecture
- ✅ Follow speckit.plan exactly

## Testing Checklist

Before marking Phase I complete, verify:

### Functional Testing
- [ ] Can add tasks with title and description
- [ ] Can view all tasks (including empty list)
- [ ] Can update task title and description
- [ ] Can delete tasks with confirmation
- [ ] Can toggle task complete/incomplete status
- [ ] Can exit application cleanly

### Input Validation Testing
- [ ] Rejects empty title
- [ ] Rejects empty description
- [ ] Handles invalid menu choices
- [ ] Handles non-numeric task IDs
- [ ] Handles non-existent task IDs
- [ ] Shows clear error messages for all errors

### Edge Cases Testing
- [ ] Works with empty task list
- [ ] Works after deleting all tasks
- [ ] Handles toggling same task multiple times
- [ ] Task IDs increment correctly
- [ ] No crashes on any input

### Code Quality
- [ ] All code has type hints
- [ ] All public methods have docstrings
- [ ] No business logic in UI layer
- [ ] No UI code in TodoManager layer
- [ ] Code follows PEP 8
- [ ] Variable names are descriptive

## Common Pitfalls to Avoid

1. **Skipping Specification Reading**
   - Always read ALL spec files first
   - Don't assume you know what to build

2. **Adding "Improvements"**
   - Stick to specifications exactly
   - Don't add features for future phases

3. **Mixing Concerns**
   - Keep UI and business logic separate
   - TodoManager should never print()
   - UI should never manipulate _tasks directly

4. **Incomplete Error Handling**
   - Every user input must be validated
   - Every operation must handle failure cases
   - No crashes allowed

5. **Poor User Experience**
   - Error messages must be clear
   - Prompts must be obvious
   - Navigation must be intuitive

## File Checklist

After implementation, these files should exist:

```
phase1-console-app/
├── src/
│   └── hackathon_todo/
│       ├── __init__.py          [Should exist, can be empty]
│       ├── main.py              [Entry point, ~15 lines]
│       ├── todo_manager.py      [Task + TodoManager, ~100 lines]
│       └── ui.py                [TodoUI, ~200-250 lines]
├── speckit.constitution         [Exists - don't modify]
├── speckit.specify              [Exists - don't modify]
├── speckit.plan                 [Exists - don't modify]
├── speckit.tasks                [Exists - update task status]
├── CLAUDE.md                    [This file - don't modify]
├── pyproject.toml               [Exists - can modify if needed]
└── README.md                    [Update with usage instructions]
```

## How to Run (After Implementation)

```bash
# From project root
python -m src.hackathon_todo.main

# Or if package installed
python src/hackathon_todo/main.py
```

## Success Criteria

Phase I is complete when:
1. All 17 tasks in speckit.tasks are marked COMPLETED
2. All 6 user stories from speckit.specify work correctly
3. All acceptance tests pass
4. No crashes on any input
5. Code is clean, documented, and follows architecture
6. README has clear usage instructions

## Questions?

If anything in the specifications is unclear or contradictory:
1. Stop and ask before implementing
2. Reference the specific spec file and section
3. Wait for clarification
4. Don't make assumptions

## Final Notes

- This is a hackathon project - keep it simple but complete
- Quality > Speed, but don't over-engineer
- Every line of code should map to a requirement
- If you're not sure, check the specs
- The specs are the source of truth

Good luck! Build exactly what's specified, nothing more, nothing less.
