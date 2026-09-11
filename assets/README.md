# 面试笔记配图

笔记里的 SVG 风格配图，由 HTML/CSS 排版后经无头 Chrome 截图生成（2x 分辨率）。

## 目录

- `*.png` —— 成品图，笔记直接引用
- `src/*.html` —— 图源，每张图一个文件，画布尺寸由 `<meta name="win" content="1000x470">` 声明
- `src/diagram.css` —— 共用样式（配色、桶、环形仓库、等待队伍、位格等组件）
- `src/render.sh` —— 批量渲染：逐个截图并自动裁掉上下白边
- `src/crop.py` —— 裁剪脚本（按亮度阈值找内容边界，避免极淡阴影撑大 bbox）

## 重新生成

```bash
bash assets/src/render.sh
```

依赖：Chrome/Edge（无头截图）+ Python3 + Pillow。改图只需编辑 `src/*.html`，
再跑一次脚本；新增图时在 HTML 里写明 `win` 尺寸即可自动纳入渲染。

## 命名

- `map-0N-*.png` —— map 扩容机制
- `chan-0N-*.png` —— channel 底层原理
