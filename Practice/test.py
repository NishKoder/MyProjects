import pandas as pd

data = [
    [1.52, 62.2, 58.0, 7.27, 7.33, 4.55, "Premium", "F", "VS2"],
    [1.52, 62.2, 58.0, 7.27, 7.33, 4.55, "Premium", "F", "VS2"],
    [1.52, 62.2, 58.0, 7.27, 7.33, 4.55, "Premium", "F", "VS2"],
    [1.52, 62.2, 58.0, 7.27, 7.33, 4.55, "Premium", "F", "VS2"],
    [1.52, 62.2, 58.0, 7.27, 7.33, 4.55, "Premium", "F", "VS2"],
    [1.52, 62.2, 58.0, 7.27, 7.33, 4.55, "Premium", "F", "VS2"],
    [1.52, 62.2, 58.0, 7.27, 7.33, 4.55, "Premium", "F", "VS2"],
    [1.52, 62.2, 58.0, 7.27, 7.33, 4.55, "Premium", "F", "VS2"]
]
df = pd.DataFrame(data, columns=["carat", "depth", "table", "x", "y", "z", "cut", "color", "clarity"])

df.to_csv("data/data.csv", index=False)

