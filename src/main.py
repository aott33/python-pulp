from pulp import (
    LpProblem,
    LpVariable,
    LpMaximize,
    LpInteger,
    LpStatus,
    value
)
import json

def main():
    print("Hello from python-pulp!")

    problem = LpProblem("Maximize Profits", LpMaximize)

    qtyHotSauce = LpVariable("Hot Sauce Quantity", lowBound=10, upBound=40, cat=LpInteger)
    qtyBBQ = LpVariable("BBQ Sauce Quantity", lowBound=10, cat=LpInteger)
    qtySalsa = LpVariable("Salsa Quantity", lowBound=10, cat=LpInteger)

    problem += qtyHotSauce * 35 + qtyBBQ * 45 + qtySalsa * 50

    problem += qtyHotSauce * 1 + qtyBBQ * 3 + qtySalsa * 2 <= 120, "Mixer Capacity"
    problem += qtyHotSauce * 2 + qtyBBQ * 2 + qtySalsa * 3 <= 150, "Cooker Capacity"
    problem += qtyHotSauce * 2 + qtyBBQ * 1.5 + qtySalsa * 1 <= 80, "Bottling Capacity"

    problem.solve()

    status = LpStatus[problem.status]
    max_profits = value(problem.objective)
    qtyHotSauceVal = 0 if qtyHotSauce.varValue is None else qtyHotSauce.varValue
    qtyBBQVal = 0 if qtyBBQ.varValue is None else qtyBBQ.varValue
    qtySalsaVal = 0 if qtySalsa.varValue is None else qtySalsa.varValue

    mixer_used = qtyHotSauceVal * 1 + qtyBBQVal * 3 + qtySalsaVal * 2 
    mixer_utilization = (mixer_used / 120) * 100

    cooker_used =  qtyHotSauceVal * 2 + qtyBBQVal * 2 + qtySalsaVal * 3
    cooker_utilization = (cooker_used / 150) * 100

    bottler_used =  qtyHotSauceVal * 2 + qtyBBQVal * 1.5 + qtySalsaVal * 1
    bottler_utilization = (bottler_used / 80) * 100

    results = {
        "status": status,
        "objective": value(problem.objective),
        "variables": {v.name: v.varValue for v in problem.variables()},
        "max_profits": max_profits,
        "bottles": {
            "hot_sauce": qtyHotSauceVal,
            "bbq_sauce": qtyBBQVal,
            "salsa": qtySalsaVal
        },
        "machine_utilization_percent": {
            "mixer": mixer_utilization,
            "cooker": cooker_utilization,
            "bottler": bottler_utilization
        }
    }
    
    def_filepath = f"problems/{problem.name}_Definition.json"
    print(f"Writing problem definition to {def_filepath}")
    problem.toJson(def_filepath)

    results_filepath = f"problems/{problem.name}_Results.json"
    json_output = json.dumps(results, indent=4)
    print(f"Writing problem results to {results_filepath}")
    with open(results_filepath, "w") as f:
        f.write(json_output)
        
    print("Results:")
    print(json_output)

if __name__ == "__main__":
    main()
