# PuLP Practice Problem

## What is Linear Programming?

Linear Programming (LP) is a mathematical method for finding the best outcome (like maximum profit or minimum cost) given a set of constraints. Think of it as "optimization with limits."

### The Three Core Components

1. **Decision Variables** - The unknowns you're solving for
   - *"How many of X should I make?"*
   - These are what the solver figures out for you

2. **Objective Function** - What you're trying to maximize or minimize
   - *"I want to maximize profit"* or *"I want to minimize cost"*
   - Always a linear equation (variables multiplied by constants, then added together)

3. **Constraints** - The rules and limitations you must follow
   - *"I only have 120 hours of machine time"*
   - *"I must make at least 10 units"*
   - Also linear equations (using <=, >=, or ==)

### Why "Linear"?

The word "linear" means all relationships are straight-line equations:
- **Valid:** `2x + 3y <= 100` (variables multiplied by constants)
- **Invalid:** `x * y <= 100` (variables multiplied together)
- **Invalid:** `x² <= 100` (exponents on variables)

### How the Solver Works (Conceptually)

Imagine each constraint as a wall in a room. The "feasible region" is the space inside all the walls - every point in this region is a valid solution. The solver then finds the point in this region that gives the best value for your objective function.

For maximization problems, this optimal point is always at a "corner" of the feasible region, which is why LP solvers are so efficient - they only need to check the corners, not every possible point.

### PuLP's Role

PuLP is a Python library that lets you:
1. Define your problem in readable Python code
2. Translate it into a format solvers understand
3. Call a solver (CBC is the default, free solver)
4. Extract and display the results

---

## Production Scheduling Challenge

### Scenario

You're the production planner at a food processing plant that makes three products:

- **Salsa** - $50 profit per batch
- **Hot Sauce** - $35 profit per batch
- **BBQ Sauce** - $45 profit per batch

### Machine Time Requirements

Each product requires time on three machines:

| Product   | Mixer (hrs) | Cooker (hrs) | Bottling (hrs) |
|-----------|-------------|--------------|----------------|
| Salsa     | 2           | 3            | 1              |
| Hot Sauce | 1           | 2            | 2              |
| BBQ Sauce | 3           | 2            | 1.5            |

### Available Machine Hours Per Day

- **Mixer:** 120 hours
- **Cooker:** 150 hours
- **Bottling:** 80 hours

### Additional Constraints

- You must produce at least 10 batches of each product (customer commitments)
- You cannot produce more than 40 batches of Hot Sauce (storage limitation)

### Your Task

Using PuLP, determine how many batches of each product to make daily to maximize profit.

### Solution Should Output

- Optimal number of batches for each product
- Total daily profit
- Machine utilization percentages