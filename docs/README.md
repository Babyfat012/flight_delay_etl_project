# Flight Delay ETL Project

Phân tích dữ liệu chuyến bay tại Mỹ trong năm 2015 để khám phá các yếu tố ảnh hưởng đến delay và huỷ chuyến, thông qua một ETL Pipeline cơ bản.

## Mục tiêu

* Xác định hãng hàng không nào có tỷ lệ delay thấp nhất
* Phân tích nguyên nhân delay chính
* Phân tích theo thời gian (ngày trong tuần)
* Xác định sân bay có hiệu suất kém

## Công nghệ sử dụng

* **Python (Pandas)** – trích xuất + xử lý (biến đổi) dữ liệu
* **MySQL** – lưu trữ và truy vấn dữ liệu
* **Power BI** – trực quan hóa dữ liệu
* **Docker** – đóng gói môi trường

## Cấu trúc thư mục

```
flight_delay_etl_project/
├── data/              
│   ├── raw/
│   └── processed/
├── db/                
├── diagram/           
├── docs/              
├── etl/               
├── notebooks/         
├── reports/           
├── main_etl.py                 
├── docker-compose.yaml
└── makefile
```

## Dữ liệu đầu vào

Nguồn dữ liệu: Bộ Giao thông Vận tải Hoa Kỳ (DOT)

* `airlines.csv`
* `airports.csv`
* `flights.csv`

## Tài liệu chi tiết

Xem tại: [`docs/Dự án 1_ ETL Pipleline đầu tiên.docx`](docs/)

Lưu ý: Do giới hạn 100MB của GitHub, các file .csv lớn và .pbix không được đẩy lên.👉 Bạn có thể tải các file này tại: 
[Link Google Drive (cập nhật sau)](https://drive.google.com/drive/u/0/folders/1lHcaXphxpZoIXkDyI5SIEObHiKSYdp6o)