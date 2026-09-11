import pdfplumber

pdf_path = "order.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for page_idx, page in enumerate(pdf.pages):
        print(f"=== ページ {page_idx + 1} の表データ ===")
        
        # ページ内の表を自動検出してリストで取得
        tables = page.extract_tables()
        
        if not tables:
            print("表が検出されませんでした。")
            continue
            
        for table_idx, table in enumerate(tables):
            print(f"--- 表 {table_idx + 1} ---")
            for row in table:
                # 各行のデータを表示（Noneを空文字に置換してすっきりさせる）
                cleaned_row = [cell.replace("\n", " ") if cell else "" for cell in row]
                print(cleaned_row)
        print("\n" + "="*40 + "\n")