import pandas as pd

df = pd.read_csv("legacy_internship_records_final.csv")

rows, columns = df.shape

print("CSV Loaded Successfully")
print(f"Rows: {rows}")
print(f"Columns: {columns}")

print("\nSchema:")
for col in df.columns:
    print(col)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumerical Statistics:")
print(df.describe())

with open("analysis_report.txt", "w") as report:

    report.write("CSV ANALYSIS REPORT\n")
    report.write("===================\n\n")

    report.write(f"Rows: {rows}\n")
    report.write(f"Columns: {columns}\n\n")

    report.write("Schema:\n")
    report.write("-------\n")

    for col in df.columns:
        report.write(f"{col}\n")

    report.write("\nMissing Values:\n")
    report.write("---------------\n")
    report.write(str(df.isnull().sum()))

    report.write("\n\nNumerical Statistics:\n")
    report.write("---------------------\n")
    report.write(str(df.describe()))

print("\nanalysis_report.txt generated successfully!")