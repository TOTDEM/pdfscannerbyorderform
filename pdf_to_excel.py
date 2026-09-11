import pdfplumber
import pandas as pd

# ファイルパスの設定
pdf_path = "order.pdf"
excel_path = "output_order.xlsx"

all_rows = []

try:
    with pdfplumber.open(pdf_path) as pdf:
        for page_idx, page in enumerate(pdf.pages):
            # ページ内のすべての表を抽出
            tables = page.extract_tables()
            
            for table in tables:
                for row in table:
                    # セル内の改行をスペースに置換し、None（空欄）を空文字に変換
                    cleaned_row = [cell.replace("\n", " ") if cell else "" for cell in row]
                    all_rows.append(cleaned_row)

    if all_rows:
        # pandasのDataFrameに変換
        df = pd.DataFrame(all_rows)
        
        # Excelファイルに出力 (indexやheaderは必要に応じて調整可能)
        df.to_excel(excel_path, index=False, header=False)
        
        print(f"成功！ '{excel_path}' にExcelファイルを出力しました。")
    else:
        print("警告: 抽出できる表データが見つかりませんでした。")

except FileNotFoundError:
    print(f"エラー: '{pdf_path}' が見つかりません。ファイル名を確認してください。")
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")