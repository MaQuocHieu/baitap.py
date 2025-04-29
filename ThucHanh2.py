import pandas as pd

df = pd.read_excel("data.xlsx.xls")


# Xử lý cột SOC
df['SOC'] = df['SOC'].str.replace('%', '', regex=False)
df['SOC'] = pd.to_numeric(df['SOC'], errors='coerce')

# Các cột cần xử lý kiểu số
cols_to_numeric = ['vpv1', 'pCharge', 'ppv1', 'ppv2', 'ppv3']
for col in cols_to_numeric:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# In thử vài dòng dữ liệu đã xử lý
print(df[['vpv1', 'pCharge', 'SOC']].head(20))

# Lọc dữ liệu
filtered_df = df[(df['vpv1'] != 0) & (df['pCharge'] != 0) & (df['SOC'] > 8)]
print(f"Số dòng sau khi lọc: {len(filtered_df)}")

# Nếu có dữ liệu, tính tổng
if not filtered_df.empty:
    filtered_df['Sum_PPV'] = filtered_df[['ppv1', 'ppv2', 'ppv3']].sum(axis=1)
    filtered_df.to_csv("Data_new.csv", index=False)
    print(" Đã lưu Data_new.csv")
else:
    print(" Không có dòng nào thỏa mãn điều kiện lọc!")