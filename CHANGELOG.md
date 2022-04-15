# Python-tkinter-libs Change Log

## [1.0.1] - 2022-04-15
### Changed
- ScrolledFrameクラスでCanvasをFrameでラップ(parent_frame プロパティ)  
  Wrapp canvas by frame in ScrolledFrame class(parent_frame property)

### Fixed
- ScrolledFrameオブジェクトが複数あってもマウスホイールが動作するようにした
	The mouse wheel now works even if there are multiple ScrolledFrame objects.