import math

def gaussian_kernel(size: int, sigma: float) -> list:
    if size % 2 == 0 or size <= 0:
        raise ValueError("size must be a positive odd integer")
    if sigma <= 0:
        raise ValueError("sigma must be positive")

    center = size // 2

    kernel = []
    total = 0.0

    # Compute unnormalized weights
    for y in range(size):
        row = []
        for x in range(size):
            dx = x - center
            dy = y - center

            weight = math.exp(
                -(dx * dx + dy * dy) / (2 * sigma * sigma)
            )

            row.append(weight)
            total += weight

        kernel.append(row)

    # Normalize so the kernel sums to 1
    kernel = [
        [weight / total for weight in row]
        for row in kernel
    ]

    return kernel


# Example
size = 5
sigma = 1.0

kernel = gaussian_kernel(size, sigma)

for row in kernel:
    print(row)