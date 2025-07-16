import pandas as pd
import os
from pathlib import Path
from datetime import datetime

def extract_data(input_file : str):
    df = pd.read_csv(input_file)
    print(f"[{datetime.now()}] Đọc {len(df)} dòng từ {input_file}")
    return df


def save_intermediate(df: pd.DataFrame, output_file: str):
    os.makedirs(os.path.dirname(output_file), exist_ok=True) # Lấy đường dẫn chứa output_file và tạo file này
    df.to_csv(output_file, index=False)
    print(f"[{datetime.now()}] Đã lưu dữ liệu vào {output_file}")


def batch_extract_all(source_dir: str, target_dir: str):
    source_path = Path(source_dir) # chuyển từ chuỗi thành đường dẫn
    target_path = Path(target_dir)

    if target_path.exists():
        for file in target_path.glob("*.csv"):
            file.unlink()
            print(f"[{datetime.now()}] Đã xóa file cũ: {file}")
    else:
        target_path.mkdir(parents=True) # nếu chưa có cha của thư mục thì tạo luôn  
        print(f"[{datetime.now()}] Tạo thư mục: {target_path}")


    file_rename_map = {
    "flights.csv": "raw_flights.csv",
    "airlines.csv": "raw_airlines.csv",
    "airports.csv": "raw_airports.csv"
    }
    for file in source_path.glob("*.csv"):
        df = extract_data(str(file)) # vì read_csv cần string path
        output_name = file_rename_map.get(file.name, file.name)
        output_file = target_path / output_name # nối data/raw và /tên-file 
        save_intermediate(df, str(output_file))

    print(f"[{datetime.now()}] Đã hoàn thành trích xuất toàn bộ dữ liệu từ {source_dir} sang {target_dir}")


if __name__ == '__main__':
    source_folder = "C:/Users/admin/Desktop/data_source"
    target_folder = "data/raw"
    print(f"[{datetime.now()} Đang chạy Extract.py")
    batch_extract_all(source_folder, target_folder)
