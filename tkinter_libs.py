"""
"""
import tkinter as tk
import tkinter.font
import sys
from typing import Tuple                # 関数アノテーション用 

class ScrolledFrame(tk.Frame):
    """
    スクロールバー付Frameクラス
    コンストラクタでの親以外のオプションの指定は未対応configで後から指定する
    """
    def __init__(self, master, has_h_bar=None) -> None:
        """
        Frameがスクロールバーを持つためにはCanvasでラップしたFrameを作成する。
        スクロールバーとCanvasはmasterに作成する
        """
        # 親としてcanvasを作成
        self.parent_canvas = tk.Canvas(master)
        super().__init__(self.parent_canvas)
        # 水平スクロールバー作成(option)
        if has_h_bar:
            hsb1 = tk.Scrollbar(master, orient=tk.HORIZONTAL, command=self.parent_canvas.xview)
            self.parent_canvas.configure(xscrollcommand=hsb1.set)
            hsb1.pack(side="bottom", fill="x")
        # 垂直スクロールバー作成
        vsb1 = tk.Scrollbar(master, orient=tk.VERTICAL, command=self.parent_canvas.yview)
        self.parent_canvas.config(yscrollcommand=vsb1.set)
        vsb1.pack(side="right", fill="y")
        self.parent_canvas.pack(side="left", fill="both", expand=True)
        # キャンバスにフレームを割り当て
        self.parent_canvas.create_window((4,4), window=self, anchor="nw")
        # bind
        self.bind_all("<MouseWheel>", self.on_frame_mouse_wheel)
        self.bind("<Configure>", self.on_frame_configure)

    def on_frame_mouse_wheel(self, event=None):
        """
        Canvasをmouse wheelで垂直scrollさせる
        """
        if event:
            # print(event.widget)   # for debug
            self.parent_canvas.yview_scroll(int(-1 * (event.delta / abs(event.delta))), "units")

    def on_frame_configure(self, event=None):
        """
        canvasを親に持つframeでサイズ変更があった場合にcanvasのscrollregionを更新する
        これでスクロールバーが動作する
        frameの<configure>シーケンスとbindして使う
        """
        if event:
            if type(event.widget.master) == tk.Canvas:
                canvas1 = event.widget.master
                canvas1.configure(scrollregion = canvas1.bbox("all"))

if __name__ == '__main__':
    print("This module has: ")
    print(" ScrolledFrame class")