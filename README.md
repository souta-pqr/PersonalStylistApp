# AIファッションアドバイザー

## 概要
ユーザーの服装や体型の画像を分析し、個別化されたファッション提案を行うWebアプリケーションです。具体的には、Vision Transformer (ViT) モデルを使用してスタイル分析を行い、DETR (DEtection TRansformer) モデルを用いて画像内のアイテムを検出します。

## 目的
- Vision Transformer を用いて、ユーザーの個人的なスタイルと体型に合わせた服装提案を行う
- DETR モデルによる画像内アイテムの検出に基づいた、コーディネート提案を提供する
- 季節や場面に応じた適切なファッション推奨を生成する

## 主な機能
1. 画像アップロード：ユーザーは自身の服装や体型の画像をアプリケーションにアップロードできます
2. スタイル分析：Vision Transformer (ViT) モデルを使用して画像のスタイルを分析し、ユーザーの全体的なファッションスタイルを判定します
3. アイテム検出：DETR (DEtection TRansformer) モデルを使用して画像内の個々の服飾アイテムを検出し、識別します
4. パーソナライズされた推奨：ユーザープロファイル、検出されたスタイル、識別されたアイテムに基づいて、個別化された服装の推奨を生成します
5. 季節・場面対応：選択された季節や場面（仕事、カジュアル、パーティーなど）に応じて、推奨内容を調整します
6. 詳細なアイテム別推奨：検出された各アイテムに対して、具体的な着こなしや組み合わせのアドバイスを提供します

## 動作環境
- Python 3.9以上
- 必要なライブラリ
  - Flask >= 2.0.1
  - PyTorch == 2.2.2
  - torchvision >= 0.16.0
  - transformers >= 4.35.0
  - Pillow >= 9.0.0
  - OpenCV-Python >= 4.8.0
  - Werkzeug >= 2.0.1
  - timm >= 0.9.0
  - importlib-metadata < 5.0
  - scipy >= 1.9.0

## セットアップ
1. リポジトリをクローン
```
git clone https://github.com/souta-pqr/PersonalStylistApp.git
```
```
cd PersonalStylistApp
```

2. 仮想環境の作成と有効化（Anacondaを使用する場合）
```
conda create -n vit python=3.10
```
```
conda activate vit
```

3. 必要なライブラリのインストール
```
pip install -r requirements.txt
```

4. アプリケーションの実行
```
python app.py
```

5. ブラウザで **http://localhost:5000** にアクセスし、アプリケーションを使用開始

## 使用方法
1. 「ファイルを選択」ボタンをクリックして分析したい服装や体型の画像を選択
2. ドロップダウンメニューから現在の季節と想定される場面を選択
3. 「分析する」ボタンをクリックして画像をアップロードし、分析を開始
4. 分析結果画面で、以下の情報が確認可能です
- 検出されたスタイル
- 検出されたアイテムとそれぞれに対する具体的なアドバイス
- 季節と場面に応じたコーディネートのヒント

## 技術詳細
- スタイル分析：Google の Vision Transformer (ViT) モデルを使用
- アイテム検出：Facebook の DETR (DEtection TRansformer) モデルを使用
- バックエンド：Flask フレームワークを使用した Python Webアプリケーション
- フロントエンド：HTML, CSS, JavaScript を使用した軽量な SPA (Single Page Application)

## 謝辞
- このプロジェクトは、Google の Vision Transformer と Facebook の DETR モデルの研究成果を活用しています
