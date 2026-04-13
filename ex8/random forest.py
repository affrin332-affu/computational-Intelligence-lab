from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# 1. User Inputs
n_est = int(input("Enter number of estimators (n_estimators): "))
crit = input("Enter criterion (gini or entropy): ")

# 2. Data Loading
data = load_breast_cancer()
X = data.data
y = data.target

split_ratios = [0.30, 0.40, 0.25]
split_names = ["70-30", "60-40", "75-25"]
final_results = []

# 3. Model Training and Evaluation Loop
for i in range(len(split_ratios)):
    print("\n--------------------------------------------")
    print("Split:", split_names[i])

    # Splitting data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_ratios[i], random_state=42)
    print("Train samples:", len(X_train))
    print("Test samples :", len(X_test))

    # Model configuration and fitting
    rf = RandomForestClassifier(n_estimators=n_est, criterion=crit, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    # Confusion Matrix unpacking
    cm = confusion_matrix(y_test, y_pred)
    TN, FP, FN, TP = cm.ravel()

    print("\nConfusion Matrix:")
    print("          Predicted 0   Predicted 1")
    print(f"Actual 0     TN= {TN:<10} FP= {FP}")
    print(f"Actual 1     FN= {FN:<10} TP= {TP}")

    # Metric Calculation
    accuracy = round(accuracy_score(y_test, y_pred), 4)
    precision = round(precision_score(y_test, y_pred), 4)
    recall = round(recall_score(y_test, y_pred), 4)
    f1 = round(f1_score(y_test, y_pred), 4)

    print("\nAccuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    # Storing results for the final table
    final_results.append([split_names[i], TP, TN, FP, FN, accuracy, precision, recall, f1])

# 4. Final Consolidated Results Table
print("\n\nFinal Consolidated Results:")
# Column headers with specific alignment/width
header = f"{'Split':<8} {'TP':<4} {'TN':<4} {'FP':<4} {'FN':<4} {'Accuracy':<10} {'Precision':<10} {'Recall':<10} {'F1-Score':<10}"
print(header)
print("-" * len(header))

for res in final_results:
    # Printing each row with the same alignment as the header
    print(f"{res[0]:<8} {res[1]:<4} {res[2]:<4} {res[3]:<4} {res[4]:<4} {res[5]:<10} {res[6]:<10} {res[7]:<10} {res[8]:<10}")
