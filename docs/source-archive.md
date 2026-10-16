# 完整制作档案

本目录说明对应 [source-archive/](../source-archive/) 中的完整制作材料。原资料包的 **307 个文件全部逐个保留**，目录和文件名保持原样；没有上传 ZIP，也没有省略原有文件。

原始解压体积为 38,574,651 字节（约 38.6 MB）。其中 216 个 PNG、21 个 GIF、1 个 MP4、38 个 JSON、29 个 Markdown 和 2 个 Python 脚本。

## 目录索引

| 位置 | 原文件数 | 内容 |
| --- | ---: | --- |
| [pet_request.json](../source-archive/pet_request.json) | 1 | 原始宠物需求、精灵布局、风格及生成参数 |
| [imagegen-jobs.json](../source-archive/imagegen-jobs.json) | 1 | 生成任务、依赖和当时记录的状态 |
| [references/](../source-archive/references/) | 13 | 基础角色及布局参考图 |
| [prompts/](../source-archive/prompts/) | 28 | 各动作、视线及修订提示词 |
| [decoded/](../source-archive/decoded/) | 23 | 生成条带、视线锚点及修订中间图 |
| [frames/](../source-archive/frames/) | 58 | 拆分单帧及清单 |
| [final/](../source-archive/final/) | 75 | 最终精灵图、单帧、预览和验证报告 |
| [qa/](../source-archive/qa/) | 108 | 检查图、报告、复核记录及两份辅助脚本 |

需要直接使用动画时，优先查看仓库根目录的 [README](../README.md) 与 [manifest.json](../manifest.json)。档案内包含早期版本、中间结果、警告和历史状态，应结合具体文件和日期理解；例如生成任务记录仍有 `pending` 字段，不代表当前发布动作未完成。

## 发布前的路径整理

为避免保留旧机器路径，共对 **27 个文本文件**做了可追踪的替换：

1. 将旧制作工作目录的绝对路径前缀统一替换为 `.`。所有这类路径应从 `source-archive/` 根目录解析，例如 `./frames/idle/00.png`。
2. 将预览脚本中的旧插件脚本目录替换为 `<external-work-pets-scripts>` 占位符。

文件名、目录、其他文本内容及全部图片/视频字节均保持不变。[逐文件清单](source-archive-inventory.json) 记录每个文件的原始与发布后 SHA-256、大小及发生的替换。`pet_request.json` 原样保留。

## 脚本与复现限制

这些脚本是制作过程的存档，不能据此认定整个项目可独立运行或一键重新生成。

- [qa/build_delivery_previews.py](../source-archive/qa/build_delivery_previews.py) 使用 Python、Pillow，以及外部模块 `render_animation_previews` 提供的 `ROW_DURATIONS` 和 `save_preview`。原资料包不含该模块；需自行提供等效实现并配置脚本中的占位路径。它依赖已有精灵图，运行后会写入 `final/encoded-frames/` 与 `final/previews/`。
- [qa/write_semantics.py](../source-archive/qa/write_semantics.py) 使用 Python 标准库，将脚本内既有的方向观察记录写入 `qa/direction-semantics.json`。它不会自动识别图片或重新执行视觉审查。
- 路径整理后的脚本以 `source-archive/` 为工作目录。执行脚本可能覆盖档案内的既有输出；建议先复制一份再实验。
- 图片生成流程依赖原制作工具与人工/视觉复核；原资料包只包含两份辅助脚本，不包含完整生成引擎或其外部依赖。

本次仅检查文件完整性、格式、路径替换和脚本语法；未运行会改写档案的脚本，也未重新生成图片。

## 完整性验证

在仓库根目录运行：

```sh
sha256sum -c SHA256SUMS
```

macOS 可用 `shasum -a 256 -c SHA256SUMS`。该清单覆盖所有已发布文件（不包含校验清单自身），包括完整制作档案。

[逐文件清单](source-archive-inventory.json) 中的 `files` 必须有 307 项，`omitted_original_files` 应为空。记录的原始 ZIP 哈希仅用于来源核对；ZIP 本身未上传。

## 权利

完整制作档案沿用根目录 [权利说明](../README.md#权利说明)。保留源材料不构成对 Snoopy / Peanuts 角色或商标的授权。
