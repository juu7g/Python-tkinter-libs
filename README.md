# Python-tkinter-libs
Tkinter向けライブラリ
Library for Tkinter

## 概要 Description
Tkinter向けライブラリ
Library for Tkinter

## 内容 Contents

- ScrolledFrameクラス  
	ScrolledFrame class

## ScrolledFrameクラス ScrolledFrame class

### 特徴 Features

- スクロールバーを持つフレームクラスを提供
	Provides Frame class with scrollbars  
- マウスホイールでスクロール  
	Scroll with mouse wheel  

### 使い方 Usage

```python
	from tkinter_libs import ScrolledFrame
	import tkinter as tk
	
	root = tk.Tk()
	scrolled_frame = ScrolledFrame(root)
```
### コンストラクタ Constructor
`ScrolledFrome(master, *args, has_h_bar=False, **kwargs)`  

## 依存関係 Requirement

- Python 3.8.5  

## プログラムの説明サイト Program description site
[スクロールバー付Frameで作るフォント一覧の作り方【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/tkinter/scrolled-frame)  

## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。  
This software is released under the MIT License, see LICENSE.txt.

