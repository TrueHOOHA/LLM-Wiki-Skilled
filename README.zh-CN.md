[English](./README.md)

# LLM Wiki

一个由 LLM 代理维护的个人知识库，遵循 [Karpathy's LLM Wiki](https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md) 中描述的模式。

**核心隐喻：** Obsidian 是 IDE，LLM 是程序员，Wiki 是代码库。你可以实时浏览结果——跟随链接、查看图谱视图、阅读更新的页面。LLM 完成所有繁琐的工作：总结、交叉引用、归档和记录。

## 使用场景

这种模式适用于任何你希望积累知识并使其保持有序而非散乱的场景：

- **个人用途**：追踪目标、健康、心理状态——归档日记条目、文章、播客笔记，构建关于自己的结构化画像。
- **研究用途**：深入探索某个主题数周——阅读论文、文章、报告，逐步构建一个包含不断演进的论点的综合 Wiki。
- **阅读书籍**：归档每一章，为角色、主题、情节线索创建页面。最终你会拥有一个丰富的伴读 Wiki（类似 [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page)）。
- **商业/团队**：内部 Wiki，整合 Slack 讨论、会议记录、项目文档、客户通话内容。LLM 完成没人愿意做的维护工作。
- **竞争分析、尽职调查、旅行计划、课程笔记、爱好深度研究**——任何知识会累积的场景。

## 快速开始

### 1. 添加来源

将文件放入 `raw/sources/` 目录（例如文章、论文或转录稿）。然后告诉你的 LLM 代理：

> "Ingest the source `raw/sources/my-article.md`."

代理将会：
- 阅读来源
- 与你讨论关键要点
- 在 `wiki/sources/` 中创建摘要
- 更新相关的实体和概念页面
- 更新索引和日志

### 2. 提问

> "What do we know about [topic] so far?"

代理将会：
- 在 `wiki/index.md` 中搜索相关页面
- 从多个页面读取并综合信息
- 使用维基链接引用来源
- 如果答案可复用，主动将其归档为新的综合页面

### 3. 健康检查

> "Lint the wiki."

代理将会：
- 扫描矛盾、过时声明、孤立页面和缺失的交叉引用
- 生成带有严重性评级的报告
- 与你讨论并应用修复

## 项目结构

```
LLM-wiki/
├── AGENTS.md          # 模式和约定（"系统提示"）
├── README.md          # 本文件
├── README.zh-CN.md    # 中文说明文件
├── raw/               # 你的不可变源文档
│   ├── sources/       # 文本来源
│   └── assets/        # 图片、数据文件
├── wiki/              # LLM 维护的知识库
│   ├── index.md       # 内容目录
│   ├── log.md         # 所有操作的时间线
│   ├── entities/      # 具体事物
│   ├── concepts/      # 抽象概念
│   ├── sources/       # 来源摘要
│   ├── syntheses/     # 跨来源分析
│   └── templates/     # 可复用的页面模板
└── .agents/           # 项目级技能定义
    └── skills/
        ├── llm-wiki-ingest/   # 摄入工作流技能
        ├── llm-wiki-query/    # 查询工作流技能
        └── llm-wiki-lint/     # 清理工作流技能
```

## 工作流

三个核心工作流记录在 `.agents/skills/` 中的技能文档里：

- **`.agents/skills/llm-wiki-ingest/SKILL.md`** — 如何将新来源添加到 Wiki
- **`.agents/skills/llm-wiki-query/SKILL.md`** — 如何使用 Wiki 回答问题
- **`.agents/skills/llm-wiki-lint/SKILL.md`** — 如何对 Wiki 进行健康检查

## 技巧

### Obsidian 设置

- **在 Obsidian 中打开 `wiki/`** 以获得最佳浏览体验。图谱视图显示页面之间的连接——哪些已连接、哪些页面是枢纽、哪些是孤立的。
- **图谱视图**：查看 Wiki 结构的最佳方式。在左侧边栏启用它。
- **网页剪辑器**：安装 [Obsidian Web Clipper](https://obsidian.md/clipper) 浏览器扩展，直接将网页文章保存到 `raw/sources/` 为 Markdown 格式。
- **本地下载图片**：在 Obsidian 设置 → 文件和链接中，将"附件文件夹路径"设置为 `raw/assets/`。然后在设置 → 快捷键中，搜索"Download"找到"为当前文件下载附件"并绑定快捷键（如 Ctrl+Shift+D）。剪辑文章后按下快捷键——所有图片都会下载到本地磁盘，这样 LLM 可以直接查看它们，而不依赖可能失效的 URL。
- **Dataview 插件**：安装 [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) 以查询页面 frontmatter。由于 LLM 会为每个页面添加 YAML frontmatter（标签、日期、来源计数），Dataview 可以跨 Wiki 生成动态表格和列表。
- **Marp 插件**：为 Obsidian 安装 [Marp](https://marp.app/) 以渲染 Markdown 幻灯片。可用于直接从 Wiki 内容生成演示文稿——查询答案可以输出为幻灯片。

### 查询输出格式

根据问题不同，答案可以采取不同形式：
- **Markdown 页面** — 带引用的标准散文
- **对比表格** — 并排分析
- **幻灯片（Marp）** — 用于演示或分享
- **图表（matplotlib）** — 用于数据可视化
- **Canvas** — 用于可视化关系映射

重要见解：**好的答案可以重新归档到 Wiki 中作为新的综合页面。** 比较、分析、发现的联系——这些都有价值，不应消失在聊天记录中。你的探索应该像摄入的来源一样在知识库中累积。

### 版本控制

这只是一个包含 Markdown 文件的 Git 仓库。你可以免费获得版本历史、分支和协作功能。定期提交。Wiki 就是代码——像对待代码一样对待它。

### 一般建议

- **模板**：使用 `wiki/templates/` 中的模板作为新页面的起点。
- **摄入风格**：交互式工作。阅读摘要、检查更新、指导 LLM 强调什么。你也可以批量摄入而较少监督——开发适合你风格的工作流。

## 工具

- **[qmd](https://github.com/tobi/qmd)**（可选）：本地 Markdown 搜索引擎，具有混合 BM25/向量搜索和 LLM 重排序，全部在本地运行。既有 CLI（供 LLM 调用）也有 MCP 服务器（原生工具集成）。小规模时索引文件就足够了；随着 Wiki 增长，qmd 会变得更有价值。

## 理念

维护知识库的繁琐之处不在于阅读或思考——而在于记录工作。更新交叉引用、保持摘要最新、注意矛盾、在数十个页面之间保持一致性。人类放弃 Wiki 是因为维护负担增长快于价值。LLM 不会感到无聊，不会忘记更新交叉引用，并且可以在一次操作中处理 15 个文件。

人类负责策划来源、指导分析、提出好问题并思考这一切意味着什么。LLM 负责其他一切。
