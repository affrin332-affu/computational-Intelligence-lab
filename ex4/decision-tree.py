import csv
import math
from collections import Counter

def load_data(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            if row:
                data.append(row)
    return headers, data

def entropy(rows):
    total = len(rows)
    if total == 0: return 0
    counts = Counter(row[-1] for row in rows)
    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

def expected_info_and_gain(rows, attr_index, attr_name):
    total_entropy = entropy(rows)
    total_rows = len(rows)
    values = sorted(set(row[attr_index] for row in rows))
    expected_info = 0
    class_labels = sorted(set(row[-1] for row in rows))

    print(f"\nAttribute: {attr_name}\n")
    print(f"{'Value':<15}", end="")
    for label in class_labels:
        print(f"{label:<10}", end="")
    print(f"{'Total':<6}")

    stored = []
    for val in values:
        subset = [row for row in rows if row[attr_index] == val]
        label_counts = Counter(row[-1] for row in subset)
        total = len(subset)
        ent = entropy(subset)
        expected_info += (total / total_rows) * ent

        print(f"{val:<15}", end="")
        for label in class_labels:
            print(f"{label_counts.get(label, 0):<10}", end="")
        print(f"{total:<6}")
        stored.append((val, label_counts, total, ent))

    print("\nEntropy calculations:")
    for val, label_counts, total, ent in stored:
        probs = ", ".join(f"{label_counts.get(label, 0)}/{total}" for label in class_labels)

        active_counts = [count for count in label_counts.values() if count > 0]
        formula_str = " - ".join([f"({c}/{total} log2 ({c}/{total}))" for c in active_counts])

        print(f"Info({val}) = Entropy({probs}) = -[{formula_str}]")

        value_parts = []
        for c in active_counts:
            p = c / total
            value_parts.append(f"{abs(p * math.log2(p)):.4f}")

        value_str = " + ".join(value_parts)
        print(f"           = {value_str}")
        print(f"           = {ent:.4f}\n")

    print(f"Expected Information (Weighted Average):")
    weighted_parts = [f"({total}/{total_rows} * {ent:.4f})" for val, lc, total, ent in stored]
    print(f"= {' + '.join(weighted_parts)}")
    print(f"= {expected_info:.4f}")

    gain = total_entropy - expected_info
    print(f"\nInformation Gain ({attr_name}) = {total_entropy:.4f} - {expected_info:.4f} = {gain:.4f}")
    return gain

def main():
    filename = input("Enter CSV filename: ")
    try:
        headers, data = load_data(filename)
    except FileNotFoundError:
        print("File not found!")
        return

    print(f"\nDataset loaded: {len(data)} rows")
    print(f"Attributes: {headers[:-1]}")
    print(f"Target Attribute: {headers[-1]}")
    total_ent = entropy(data)
    print(f"Total Entropy of Dataset = {total_ent:.4f}")

    gains = {}
    for i in range(len(headers) - 1):
        gain = expected_info_and_gain(data, i, headers[i])
        gains[headers[i]] = gain
        print("-" * 60)

    print("\nInformation Gain Summary:")
    for attr, g in gains.items():
        print(f"{attr} : {g:.4f}")

    root = max(gains, key=gains.get)
    print(f"\nRoot Node of the Decision Tree is: {root} as it has the Maximum InfoGain value")

if __name__ == "__main__":
    main()
