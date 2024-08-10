<!-- djangoのREADME -->
# Django

## 概要
学習用
生成AIを用いて、商品の画像から商品名を生成するECサイトのバックエンドです。
このREADMEは自動生成されています。

## 環境
- Windows 10
- Python 3.12.x
- Django 3.x.x
- Node.js 14.x.x
- docker 20.x.x

## dockerの起動(postgres)
```bash
$ docker-compose up -d
```

## インストール
```bash
$ cd c01bec
$ pip install -r requirements.txt
```

## プロジェクトの実行
```bash
$ cd c01bec
$ python manage.py runserver
$ cd ../ec-site-vue-with-claude-main
$ npm install
$ npm run dev

ブラウザで以下のURLにアクセス(キッチンの商品リンク先でAPI実行)
http://localhost:3000/
```
