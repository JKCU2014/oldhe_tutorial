# 【老何聊技术】线程锁

## 文章链接

[👉👉戳我获取文章👈👈](https://bytedance.feishu.cn/docx/doxcnE8TJxGDwpyX9q6iNVwacVf)

## 打开方式
`cd` 到本文件所在目录下，使用以下命令打开 jupyter notebook：

`jupyter-lab ./thread_lock_note.ipynb` 

## 说明
* 代码中有数量较多的 `time.sleep(0.1)`，目的是更好地演示线程编程中会暴露的问题

## 文件一览

```
lock
├── README.md
├── __init__.py
├── circular_queue              # 固定大小缓冲区实现主要源码
│	 ├── deadlock.py        # 会造成死锁的实现
│	 └── unsafe.py          # 线程不安全的实现
├── dinning_philosopher         # 哲学家就餐问题主要源码
│	 ├── fork.py            # 模拟哲学家左右两边的叉子
│	 └── philosopher.py     # 哲学家的几种实现方式，造成死锁和不会造成死锁的都有
└── thread_lock_note.ipynb      # 代码演示 notebook
```
