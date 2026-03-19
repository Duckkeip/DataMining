from datasets import load_dataset
import pandas as pd

print("Đang kết nối với Hugging Face để lấy dữ liệu...")

# Sử dụng chế độ streaming=True để không phải tải cả file lớn
# Bạn có thể thay 'Wikipedia (en)' bằng các nguồn khác trong The Pile nếu muốn
ds = load_dataset("EleutherAI/pile", split="train", streaming=True)

data_list = []
limit = 3000  # Số lượng dòng bạn muốn lấy cho Weka

for i, example in enumerate(ds):
    if i >= limit:
        break
    # Lấy văn bản và cắt ngắn mỗi dòng (khoảng 1000 ký tự) để Weka không bị quá tải
    text = example['text'].replace('\n', ' ').strip()[:1000]
    data_list.append(text)

    if i % 500 == 0:
        print(f"Đã lấy được {i} dòng...")

# Lưu thành file CSV để nạp vào Weka
df = pd.DataFrame(data_list, columns=['text_content'])
df.to_csv('pile_sample_for_weka.csv', index=False, encoding='utf-8')

print("Thành công! File 'pile_sample_for_weka.csv' đã sẵn sàng.")