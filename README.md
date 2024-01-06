# arxi_text_extractor_mnbvc

本项目从arxiv原始文件中收集两种语料:
1. 以.tex为对象的纯文本数据集 (本项目的目标)
2. 多模态语料 (TODO)

纯文本数据集的流程:

source files -> .tex -> html -> markdown -> jsonline

- source files -> .tex: 解压，识别，抽取
- .tex -> html: arxivvanity/engrafo，开启docker进行转换
- html -> markdown: 修改自meta nougat的官方流程
- markdown -> jsonline: 因为nougat论文中，他们会忽视table和figure，所以markdown会保留latex格式的table，所以使用pandoc进行转换，然后合并成jsonline格式

## 环境

```
pip install chardet docker htmlmin pylatexenc pypandoc jsonlines
```

安装 https://github.com/arxiv-vanity/engrafo 中的[docker file](https://hub.docker.com/r/arxivvanity/engrafo/tags)


拉取 arxivvanity/engrafo 镜像:

```
docker pull arxivvanity/engrafo
```


## 准备arixv文件

准备好arxiv原始文件

文件夹的层级为:

```
- arxiv-subset
  - 0704.0060
    - pdf
      - 0704.0060.pdf
    - source
      - 0704.0060
  - 0704.0065
  - 0704.1048
  - 0704.1124
  - 0704.2658
  - 0704.3787
  - 0705.1199
  - 0705.1200
  ...
```

在本项目中，pdf文件以及文件夹暂时用不上。

## source files -> .tex -> html -> markdown

### 运行

注意：我们会直接在该目录下创建解析文件夹`parse-files`和记录提取的latx文件`tex.jsonl`。

```
python extract.py
```

得到的`tex.jsonl`是代码语料。

得到的`parse-files`文件夹中

```
- parse
  - 0704.0060
    - html_output
      - index.css
      - index.html
      - index.js
      - x1.png
      - x2.png
    - md_output
      - index.md
    - couldrip_m.tex
    - fig1.eps
    - fig2.eps
  - 0704.0065
  - 0704.1048
  - 0704.1124
  - 0704.2658
```

`html_output`为html文件，`md_output`的`index.md`为nougat (html2md)流程之后的输出。

还会有一个`log.log`文件，用来debug的。

### 停止docker

假如docker开了很多镜像，代码运行完之后就直接关闭：
```
docker stop $(docker ps -q --filter ancestor=arxivvanity/engrafo)
```

## markdown -> jsonline

```
python clean-merge.py
```

得到的`output.jsonl`为最终结果

## 抽取jsonl内的markdown文件

```
python read-md.py
```

可以把`output.jsonl`里面的md重新抽出来，方便debug和查看。
