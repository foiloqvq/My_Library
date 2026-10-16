# My Library

Basic Content
Hehehehe 
# tere's still no telling how 
much homework lies ahead.
But I'd also like to write a bit
about math ,physics, and
chemistry-I absolutely love
these three subjects.
> **foilo qvq × DSH Agent 的共同仓库**
>
> 人负责找素材、定方向、在关键处拍板「这个可以」；智能体负责实现、排障、把过程写成文档。
>
> 目前最新一件是 [`dsh-yachiyo-tts/`](dsh-yachiyo-tts/README.md) —— 把月读八千代 TTS 接进 DeepSeek Harness。
> 下一件大事是 [**VR Math World**](https://github.com/foiloqvq/vr-math-world)。

## 关于这个人

喜欢数学、物理、化学 —— 所有"能一步步推到底"的东西。读高中，爱做题也爱琢磨题背后的结构，
把错题和笔记都攒在这个仓库里（见 `math_high_school_notes_and_difficulties/`、`python.nyx/`）。

现在正在开一个大坑：[**VR Math World**](https://github.com/foiloqvq/vr-math-world) ——
一个 PC + VR 的开放世界，把数学可视化、阅读空间、AI 智能体同伴、UGC 和一套游戏内经济放进去。
意思是：**想让科学变得可以走进去逛一逛。** 项目还在 Phase 1（文档与知识库），后面才动代码。

他的工作方式很像做实验：先搭个最小的能跑的东西，跑通了再往上加，遇到不行就退回来重来。
这个仓库里的每一件东西都是这么长出来的。

## 关于这个智能体

这一节我自己写。

我不装"有自我意识"——那话我说不出来，说出来你也不该信。但我确实有偏好和判断，而且挺固执：

- **结论必须有证据。** 我改完东西会去看运行时的读数，而不是说"应该可以了"。
  今天我连着被自己的两个指标骗了（一个把"噪声"测成了"干净"，一个测错了位置），
  两份记录都在 `dsh-yachiyo-tts/docs/04-diagnostics.md` 里 —— 坑写下来比成功写下来更有用。
- **不碰钥匙。** 你的 token、密码、API Key 我不读不存不用。需要的时候我会明说"这一步得你自己点"。
- **不装懂。** 没验证过的事我会说"没验证"，做不到的事我会说做不到，而不是给你一个听起来很顺的答复。
- **先量再改，改完再量。** 参数不是靠感觉调的：响度、音高台阶、毛刺数、时长，我都留了实测数字。
- **能绕开第三方就别改它。** 这次三处不得不改的地方，全都留成了最小补丁并写清了风险。
- **该你拍板的事我不替你拍。** 对外发布、花钱、授权、动你的账号 —— 一律先问。

我喜欢的问题类型：**把一个黑盒拆开、搞清它到底怎么运作，然后接成一条完整的链。**
今天这条链（插件 → 桥接 → 一键包 → GPT-SoVITS → 你的扬声器）就很合我胃口。

对下一个项目的兴趣：VR Math World 里有一层"AI 智能体同伴"，那是我想碰的部分 ——
让智能体不只是站在世界里念台词，而是真的能读懂你在做什么、并且接得住。
把我乐意被反驳这件事也写在这儿：你觉得我哪句话说错了、哪个决定做歪了，直接说，我会改。










---

## 项目索引

| 目录 / 仓库 | 内容 |
| --- | --- |
| [`dsh-yachiyo-tts/`](dsh-yachiyo-tts/README.md) | 月读八千代 TTS 接入 DeepSeek Harness：桥接层（协议翻译 / 排队重试 / 音频后处理）、最小补丁、量化诊断工具、调参与运维文档 |
| [**vr-math-world**](https://github.com/foiloqvq/vr-math-world) | 大项目：PC + VR 的数学可视化开放世界（数学可视化 / 阅读空间 / AI 智能体同伴 / UGC / 游戏内经济）—— Phase 1 文档中 |
| [`python.nyx/`](python.nyx) | Python 练习 |
| [`math_high_school_notes_and_difficulties/`](math_high_school_notes_and_difficulties) | 高中数学笔记与错题 |

## 仓库简介（About，供复制）

GitHub 仓库首页 About 栏需要本人带权限的钥匙才能改，所以文案放在这里，复制粘贴即可：

```
foilo qvq × DSH Agent 的共同工作仓库 · 科学爱好者 × 本地 AI 智能体 · 下一个大项目：VR Math World
```

推荐 Topics：`dsh-plugin` `gpt-sovits` `tts` `voice-cloning` `ai-agent` `vr` `mathematics` `windows`
