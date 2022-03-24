# Python-tkinter-libs
Tkinter�������C�u���� `en` Library for Tkinter

## �T�v Description
Tkinter�������C�u���� `en` Library for Tkinter

## ���e Contents

- ScrolledFrame�N���X `en` ScrolledFrame class
- TkinterLib�N���X `en` TkinterLib class
	- wrapped_grid()�N���X���\�b�h `en` wrapped_grid() class method

## ScrolledFrame�N���X ScrolledFrame class

### ���� Features

- �X�N���[���o�[�����t���[���N���X���  
	`en` Provides Frame class with scrollbars  
- �}�E�X�z�C�[���ŃX�N���[��  
	`en` Scroll with mouse wheel  

### �g���� Usage

```python
	from tkinter_libs import ScrolledFrame
	import tkinter as tk
	
	root = tk.Tk()
	scrolled_frame = ScrolledFrame(root)
```
### �R���X�g���N�^ Constructor
`ScrolledFrome(master, *args, has_h_bar=False, **kwargs)`  

## TkinterLib�N���X TkinterLib class

### ���\�b�h Method
- `wrapped_grid(cls, parent, *widgets, event=None, flex=False, force=False, divisions=None, **kwargs)`  

	- ���� `en` Argument
		- `parent`�F�e�E�B�W�F�b�g(�e�Ƃ��ĕ����擾����E�B�W�F�b�g)  
			&emsp;&emsp;`en` Parent widget (widget to get width as parent)
		- `*widgets`�F�q�E�B�W�F�b�g(����grid����Ă��邱�ƁB�������Ȃ��ƕ����m�肵�Ȃ�)  
			&emsp;&emsp;`en` Child widget (already gridded, otherwise the width will not be determined)
		- `flex`�F�q�E�B�W�F�b�g�̕����ςɂ��邩�iTrue�F�ρAFalse�F�Œ�j  
			&emsp;&emsp;`en` Whether to make the width of the child widget variable (True: variable, False: fixed)
		- `force`�F�e�E�B�W�F�b�g�ɃT�C�Y�ύX���Ȃ��Ă���������  
			��ʍ쐬���Ɏg���Ɨǂ�  
			&emsp;&emsp;`en` Run without resizing the parent widget
		- `divisions`�F`flex=True` �ɂ����ꍇ�̐e�E�B�W�F�b�g�̕��̕�����  
			�f�t�H���g��500�B�傫������ΐ����ɂȂ邪���܂�傫�����Ă������o�Ȃ�  
			&emsp;&emsp;`en` Number of divisions of the width of the parent widget when `flex = True` is set
		- `**kwargs`�Fgrid �ɏ�����  
			&emsp;&emsp;`en` Same as grid

	- ���� `en` Features

		- �e�E�B�W�F�b�g�̕��Ŏq�E�B�W�F�b�g�����b�v  
			`en` Wrap the child widget with the width of the parent widget  
		- �q�E�B�W�F�b�g�̕����ςƌŒ��I���ł���  
			`en` You can choose variable or fixed width for child widgets  

	- �g���� `en` Usage

```python
    self.frame.parent_canvas.bind("<Configure>", lambda event: TkinterLib.wrapped_grid(
        self.frame.parent_canvas, *self.labels, event=event, flex=flex), add=True)
```
## �ˑ��֌W Requirement

- Python 3.8.5  

## �v���O�����̐����T�C�g Program description site

- [�X�N���[���o�[�tFrame�ō��t�H���g�ꗗ�̍����yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/tkinter/scrolled-frame)  
- [�eFrame�̕��ɍ��킹��grid�������߂č��t�H���g�ꗗ�̍����yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/tkinter/wrapped-grid)


## ��� Authors
juu7g

## ���C�Z���X License
���̃\�t�g�E�F�A�́AMIT���C�Z���X�̂��ƂŌ��J����Ă��܂��BLICENSE.txt���m�F���Ă��������B  
`en` This software is released under the MIT License, see LICENSE.txt.