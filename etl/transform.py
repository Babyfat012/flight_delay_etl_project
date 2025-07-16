import pandas as pd
from datetime import time, datetime
from pathlib import Path
import shutil

def convert_to_datetime(val):
    if pd.isna(val):
        return None
    val = int(val)
    if val == 2400:
        return time(0, 0)
    time_str = str(val).zfill(4)
    hour = int(time_str[:2])
    minute = int(time_str[2:])
    return time(hour, minute)

def transform_time_columns(df: pd.DataFrame):
    time_columns = [
        'DEPARTURE_TIME',
        'SCHEDULED_DEPARTURE',
        'WHEELS_OFF',
        'WHEELS_ON',
        'SCHEDULED_ARRIVAL',
        'ARRIVAL_TIME'
    ]

    for col in time_columns:
        if col in df.columns:
            df[col] = df[col].apply(convert_to_datetime)
    
    return df


def transform_flight_data(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    df = transform_time_columns(df)
    df.to_csv(output_path, index=False)
    print(f"[{datetime.now()}] Đã clean và lưu flights.csv -> {output_path}")


def copy_other_file(input_path: str, output_path: str):
    shutil.copy(input_path, output_path) #
    print(f"[{datetime.now()}] Đã copy {Path(input_path).name} -> {output_path}")


def batch_transform(source_dir: str, target_dir: str):
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    if target_path.exists():
        for file in target_path.glob("*.csv"):
            file.unlink()
            print(f"[{datetime.now()}] Đã xóa file cũ: {file}")
    else:
        target_path.mkdir(parents=True)

    file_rename_map = {
    "raw_flights.csv": "clean_flights.csv",
    "raw_airlines.csv": "clean_airlines.csv",
    "raw_airports.csv": "clean_airports.csv"
    }

    for file in source_path.glob("*.csv"):
        output_name = file_rename_map.get(file.name, file.name)
        output_file = target_path / output_name
        if file.name == "raw_flights.csv":
            transform_flight_data(str(file), str(output_file))
        else:
            copy_other_file(str(file), str(output_file))
    
    print(f"[{datetime.now()}] Đã hoàn thành biến đổi toàn bộ dữ liệu từ {source_dir} sang {target_dir}")


if __name__ == '__main__':
    raw_dir = "data/raw"
    clean_dir = "data/processed"
    print(f"[{datetime.now()} Đang chạy Transform.py")
    batch_transform(raw_dir, clean_dir)