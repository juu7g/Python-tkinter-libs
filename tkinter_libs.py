"""
Tkinter用ライブラリ
"""
import tkinter as tk


class ScrolledFrame(tk.Frame):
    """
    スクロールバー付Frameクラス
    ※bind時の注意
        selfのConfigure, selfのMouseWheel, self.parent_canvasのConfigureは
        既にbindしているので、外部でバインドする場合add=Trueオプションを指定する
    """
    def __init__(self, master, *args, has_h_bar:bool=False, **kwargs) -> None:
        """
        Frameがスクロールバーを持つためにはCanvasでラップしたFrameを作成する。
        スクロールバーとCanvasはmasterに作成する
		Args:
			bool(has_h_bar):    水平スクロールバー(True:表示、False:非表示)
            その他:             Frameクラスに準拠
        """
        # 親としてcanvasを作成
        self.parent_canvas = tk.Canvas(master)
        super().__init__(self.parent_canvas, *args, **kwargs)
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
        # キャンバスにフレームを割り当て 0,0はanchor位置なのでnwを指定
        self.frame_id = self.parent_canvas.create_window(0, 0, anchor="nw", window=self)
        # bind
        self.bind_all("<MouseWheel>", self.on_frame_mouse_wheel)
        self.bind("<Configure>", self.on_frame_configure)
        # self.parent_canvas.bind("<Configure>", self.on_canvas_configure)  # スクロールバーと相性が悪い

    def on_frame_configure(self, event=None):
        """
        canvasを親に持つframeでサイズ変更があった場合にcanvasのscrollregionを更新する
        これでスクロールバーが動作する
        frameの<configure>シーケンスとbindして使う
        """
        if event:
            if type(event.widget.master) == tk.Canvas:
                canvas1 = event.widget.master
                canvas1.config(scrollregion = canvas1.bbox("all"))

    def on_canvas_configure(self, event=None):
        """
        frameを子に持つcanvasでサイズ変更があった場合にframeの幅と高さを更新する
        self.frame_idはcanvasにframeを配置した時のID
        スクロールバーと相性が悪い
        """
        if event:
            if event.width > self.winfo_width():
                self.parent_canvas.itemconfig(self.frame_id, width=event.width)
            if event.height > self.winfo_height():
                self.parent_canvas.itemconfig(self.frame_id, height=event.height)

    def on_frame_mouse_wheel(self, event=None):
        """
        Canvasをmouse wheelで垂直scrollさせる
        """
        if event:
            # print(event.widget)   # for debug
            self.parent_canvas.yview_scroll(int(-1 * (event.delta / abs(event.delta))), "units")

if __name__ == '__main__':
    print("This module has: ")
    print(" ScrolledFrame class")