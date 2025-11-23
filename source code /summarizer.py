expenses = [
    ["2025-11-23", "Food", 200, "Snacks"],
    ["2025-11-23", "Transport", 50, "Bus fare"],
    ["2025-11-22", "Food", 300, "Lunch"]
]

def summary_by_category():
    summary = {}
    for e in expenses:
        cat = e[1]
        summary[cat] = summary.get(cat, 0) + e[2]

    print("Summary by Category:")
    for cat, total in summary.items():
        print(f"{cat}: {total}")

# Example usage
summary_by_category()
