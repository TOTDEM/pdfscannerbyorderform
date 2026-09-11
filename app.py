import streamlit as st
import pdfplumber
import pandas as pd

st.title("注文書データ抽出ツール（ローカル版）")

# ファイルアップロード枠
uploaded_file = st.file_uploader("注文書のPDFファイルを選択してください", type=["pdf"])

if uploaded_file is not None:
    st.success("PDFファイルがアップロードされました！")
    
    # データを一時的に格納するリスト
    all_rows = []
    
    # pdfplumberでファイルを直接開いてテーブル抽出
    with pdfplumber.open(uploaded_file) as pdf:
        for page_idx, page in enumerate(pdf.pages):
            # ページからテーブルを抽出
            tables = page.extract_tables()
            
            if tables:
                for table in tables:
                    for row in table:
                        all_rows.append(row)
                        
    # データが見つかった場合、pandasでDataFrameにしてプレビュー表示
    if all_rows:
        df = pd.DataFrame(all_rows)
        
        st.subheader("📊 抽出されたデータのプレビュー")
        st.write(f"全 {len(df)} 行のデータを検出しました。")
        
        # 画面上で確認できるインタラクティブな表
        st.dataframe(df, use_container_width=True)
        
        # データの確定・Excel出力ボタン
        if st.button("このデータを整形して保存する"):
            st.info("ここに、Excel出力やデータ整形の処理を接続できます！")
            
    else:
        st.warning("PDFからテーブル形式のデータが見つかりませんでした。設定を確認してください。")