"""
Tkinter用ライブラリ
"""
import tkinter as tk

class TkinterLib:
    @classmethod
    def wrapped_grid(cls, parent, *widgets, event=None, flex=False, force=False, divisions=None, **kwargs):
        """
        parentの幅に合わせてwidgetsをgridで再配置する
        gridの列数は(parentの幅//widgetsの要素で最大の幅)で求める
        flexがTrueの時は、parentの幅に1行ごとに入れられるだけのwidgetを入れる
        bindさせる場合、widgetsのgridでサイズ変更が起きないウィジェットで行う
            そうしないとgrid直後に再度呼ばれて無限ループになる
        ScrolledFrameクラスのオブジェクトにbindする場合、parent_canvasプロパティにbindする
        Args:
            Any:    親ウィジェット
            *Any:   子ウィジェット
            bool:   子ウィジェットの幅を固定するかどうか(True:固定しない、False:固定)
            bool:   親ウィジェットの幅がサイズ変更してなくても動作させる
            int:    親ウィジェットの幅の分割数
        """
        if not widgets: return
        # コマンドライン引数指定の場合、mainloopが起動していないのでupdateする
        parent.update()
        print(f"Enter wrapped_grid parent:{parent.winfo_width()}, child:{widgets[0].winfo_width()}")
        if not divisions: divisions = 500
        force_f = force                     # サイズ変更がなくてもgridしたい時
        try:
            parent.previous_width
        except:
            parent.previous_width = -1
        parent_width = parent.winfo_width()
        # parentの幅が変わっていなかったら抜ける
        if parent_width == parent.previous_width and not force_f: return # 

        parent.previous_width = parent_width

        if flex:
            r = c = width = 0
            print(f"Do grid by flex")    # for DEBUG
            for widget in widgets:
                widget_width = widget.winfo_width()
                cspan = max(1, int(widget_width * float(divisions) / parent_width))
                width += widget_width
                if width > parent_width:
                    r += 1
                    width = widget_width
                    c = 0
                widget.grid(row=r, column=c, columnspan=cspan, **kwargs)
                c += cspan
        else:
            # parentに前のカラム数を覚えさせる
            try:
                parent.previous_column
            except:
                parent.previous_column = -1
            max_width = max([x.winfo_width() for x in widgets])
            column_num = max(1, parent_width // max_width)  # 0を除く
            if parent.previous_column == column_num and not force_f: return
            parent.previous_column = column_num
            print(f"Do grid by fixed colum num : {column_num} ({parent_width}//{max_width})")    # for DEBUG
            for i, widget in enumerate(widgets):
                widget.grid(row=i // column_num, column=i % column_num, **kwargs)

        parent.update_idletasks() # update()
        return

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
        # 親としてFrameを作成 notebookにaddするために用意
        # このFrameにCanvas,Scrollbarを設置
        self.parent_frame = tk.Frame(master, background="darkgray")
        # self.parent_frame.pack(fill=tk.BOTH, expand=True)
        # 親としてcanvasを作成
        self.parent_canvas = tk.Canvas(self.parent_frame, background="lightgray")
        super().__init__(self.parent_canvas, *args, **kwargs)
        # 水平スクロールバー作成(option)
        if has_h_bar:
            hsb1 = tk.Scrollbar(self.parent_frame, orient=tk.HORIZONTAL, command=self.parent_canvas.xview)
            self.parent_canvas.configure(xscrollcommand=hsb1.set)
            hsb1.pack(side="bottom", fill="x")
        # 垂直スクロールバー作成
        vsb1 = tk.Scrollbar(self.parent_frame, orient=tk.VERTICAL, command=self.parent_canvas.yview)
        self.parent_canvas.config(yscrollcommand=vsb1.set)
        vsb1.pack(side="right", fill="y")
        self.parent_canvas.pack(side="left", fill="both", expand=True)
        # キャンバスにフレームを割り当て 0,0はanchor位置なのでnwを指定
        self.frame_id = self.parent_canvas.create_window(0, 0, anchor="nw", window=self)
        # bind
        self.bind_all("<MouseWheel>", self.on_frame_mouse_wheel, add=True)
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
        ScrolledFrmeオブジェクトが複数ある場合に備えて子供のイベントかどうか検査する
        """
        if event:
            # print(f"mouse wheel event:{event.widget}")   # for debug
            # イベントが発生したウィジェットがselfの子供かどうか検査する
            widget_ = event.widget
            while not (widget_ is self.parent_canvas):
                if isinstance(widget_.master, tk.Tk): return # 親がTk()ならそれ以上親はないので抜ける
                widget_ = widget_.master
            # scroll
            self.parent_canvas.yview_scroll(int(-1 * (event.delta / abs(event.delta))), "units")

if __name__ == '__main__':
    print("This module has: ")
    print(" TkinterLib class")
    print(" ScrolledFrame class")