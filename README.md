WeightLogConverter
==
スマートフォンなどの体重記録アプリのログを、まとめて対象のアプリのインポート可能形式ファイルに変換するスクリプトです。

使い方:
```
$python converter.py -m 出力モード ログファイル...

// SimpleDiet形式で出力
$python converter.py -m sd 2012_sd.csv 2013_rs.csv
```

対応アプリケーション
==
以下のアプリケーションのログ読み込み・出力に対応しています。
- SimpleDiet(iOS)
  - http://simple-diet.softonic.jp/iphone
  - mode: sd

- RecStyle(Android)
  - http://www.recstyle.jp/
  - mode: rs
