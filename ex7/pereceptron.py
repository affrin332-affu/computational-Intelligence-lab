def activation(yin):
    if activation_type == 1:
        return 1 if yin > theta else 0
    elif activation_type == 2:
        return 1 if yin > theta else -1

def train():
    global w, b
    max_epochs = 5
    for epoch in range(1, max_epochs + 1):
        print(f"\nEpoch {epoch}")

        f_hdr = " | ".join([f"f{j+1}" for j in range(n)])
        w_hdr = " | ".join([f"w{j+1}" for j in range(n)])
        print(f"{f_hdr} | t | y(in) | y | {w_hdr} | b")
        print("-" * 44)

        has_error = False

        for row in data:
            x = row[:-1]
            t = row[-1]

            yin = b + sum(x[i] * w[i] for i in range(n))
            y = activation(yin)

            if y != t:
                for i in range(n):
                    w[i] = w[i] + alpha * x[i] * t
                b = b + alpha * t
                has_error = True

            f_values = " | ".join([f"{x[j]:^3}" for j in range(n)])
            w_values = " | ".join([f"{w[j]:.2f}" for j in range(n)])
            print(f"{f_values} | {t:^3} | {yin:^6.2f} | {y:^3} | {w_values} | {b:.2f}")

        if not has_error:
            print(f"\nTraining Converged after {epoch} epochs!")
            return

    print(f"\nStopped at max epoch ({max_epochs})")

n = int(input("Enter number of features (n): "))
n_samples = int(input("Enter number of samples: "))

data = []
print(f"\nEnter {n} features followed by the target for each sample:")
for i in range(n_samples):
   row = list(map(float, input(f"Sample {i+1}: ").split()))
   data.append(row)

w = []
for i in range(n):
    w.append(float(input(f"Enter initial weight w{i+1}: ")))
b = float(input("Enter initial bias (b): "))
alpha = float(input("Enter learning rate (alpha): "))

print("\nSelect Activation Function:\n1. Binary (0,1)\n2. Bipolar (-1,1)")
activation_type = int(input("Enter choice (1 or 2): "))
theta = float(input("Enter threshold value (theta): "))

train()

print("\nFinal Answer:")
print(f"Weights: {[round(wi, 2) for wi in w]} Bias: {round(b, 2)}")
