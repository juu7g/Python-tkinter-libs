# Python-tkinter-libs
Tkinter向けライブラリ `en` Library for Tkinter

## 概要 Description
Tkinter向けライブラリ `en` Library for Tkinter

## 内容 Contents

- ScrolledFrameクラス `en` ScrolledFrame class
- TkinterLibクラス `en` TkinterLib class
	- wrapped_grid()クラスメソッド `en` wrapped_grid() class method

## ScrolledFrameクラス ScrolledFrame class

### 特徴 Features

- スクロールバーを持つフレームクラスを提供  
	`en` Provides Frame class with scrollbars  
- マウスホイールでスクロール  
	`en` Scroll with mouse wheel  

### 使い方 Usage

```python
	from tkinter_libs import ScrolledFrame
	import tkinter as tk
	
	root = tk.Tk()
	scrolled_frame = ScrolledFrame(root)
```
### コンストラクタ Constructor
`ScrolledFrome(master, *args, has_h_bar=False, **kwargs)`  

## TkinterLibクラス TkinterLib class

### メソッド Method
- `wrapped_grid(cls, parent, *widgets, event=None, flex=False, force=False, divisions=None, **kwargs)`  

	- 引数 `en` Argument
		- `parent`：親ウィジェット(親として幅を取得するウィジェット)  
			&emsp;&emsp;`en` Parent widget (widget to get width as parent)
		- `*widgets`：子ウィジェット(既にgridされていること。そうしないと幅が確定しない)  
			&emsp;&emsp;`en` Child widget (already gridded, otherwise the width will not be determined)
		- `flex`：子ウィジェットの幅を可変にするか（True：可変、False：固定）  
			&emsp;&emsp;`en` Whether to make the width of the child widget variable (True: variable, False: fixed)
		- `force`：親ウィジェットにサイズ変更がなくても処理する  
			画面作成時に使うと良い  
			&emsp;&emsp;`en` Run without resizing the parent widget
		- `divisions`：`flex=True` にした場合の親ウィジェットの幅の分割数  
			デフォルトは500。大きくすれば精密になるがあまり大きくしても差が出ない  
			&emsp;&emsp;`en` Number of divisions of the width of the parent widget when `flex = True` is set
		- `**kwargs`：grid に準ずる  
			&emsp;&emsp;`en` Same as grid

	- 特徴 `en` Features

		- 親ウィジェットの幅で子ウィジェットをラップ  
			`en` Wrap the child widget with the width of the parent widget  
		- 子ウィジェットの幅を可変と固定を選択できる  
			`en` You can choose variable or fixed width for child widgets  

	- 使い方 `en` Usage

```python
    self.frame.parent_canvas.bind("<Configure>", lambda event: TkinterLib.wrapped_grid(
        self.frame.parent_canvas, *self.labels, event=event, flex=flex), add=True)
```
## 依存関係 Requirement

- Python 3.8.5  

## プログラムの説明サイト Program description site

- [スクロールバー付Frameで作るフォント一覧の作り方【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/tkinter/scrolled-frame)  
- [親Frameの幅に合わせてgrid数を決めて作るフォント一覧の作り方【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/tkinter/wrapped-grid)


## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。  
`en` This software is released under the MIT License, see LICENSE.txt.