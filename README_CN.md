# 10 Hz rTMS vs iTBS 青少年抑郁症随机对照试验 — 实验程序

本仓库包含一项随机对照试验中使用的计算机化实验程序，该试验比较 10 Hz rTMS 与 iTBS 对青少年重性抑郁障碍的疗效。

## 临床试验注册

- 注册号：[待补充]
- 伦理批准：山东省精神卫生中心伦理委员会 (KYSJWLL2025-1-019)

---

## 内容概览

| 类别 | 程序 | 平台 |
|---|---|---|
| 临床问卷 | CDI, MASC, PSQI | Python v.3.11.7  |
| 认知任务 | 空间 N-back | Python v.3.11.7  |
|  | 威斯康星卡片分类测验 (WCST) | Python v.3.11.7  |
|  | 气球模拟风险任务 (BART) | Python v.3.11.7  |
| fMRI 任务 | 简单猜门任务 | PsychoPy (builder) v.2022.2.5 |


### Python 依赖库
|第三方库 | 版本 |
|---|---|
|Pandas| 2.2.1 |
|numpy | 1.23.5 | 
|pygame |2.5.2 | 
| PsychoPy (PyPI)  | 2023.1.3 |
| pypinyin | 0.51.0 |
| matplotlib | 3.8.3 |
| fpdf2 | 2.7.8 |

---

## 临床自评问卷

### 儿童抑郁量表 (CDI)
### 多维儿童焦虑量表 (MASC)
### 匹兹堡睡眠质量指数 (PSQI)

上述自评量表均在 PsychoPy 中实现，以标准化、计算机化形式呈现，确保施测一致性。

---

## 认知任务

### 1. 空间 N-back 任务

评估工作记忆。被试需判断当前方块位置是否与 N 步前一致。包含三种难度水平：1-back、2-back、3-back。

### 2. 威斯康星卡片分类测验 (WCST)

评估执行功能。被试根据颜色、形状或数量将反应卡与刺激卡匹配，分类规则在连续正确应答后不可预测地改变。记录反应时、正确率、持续性错误和完成分类数。

### 3. 气球模拟风险任务 (BART)

评估风险决策行为。被试对虚拟气球进行充气，每次充气增加收益但也增加爆炸风险。包含三种气球类型，对应不同爆炸概率。主要指标为每次充气次数。

---

## fMRI 任务

### 简单猜门任务

奖赏加工 fMRI 范式。被试在每次试次中选择两扇门中的一扇，随后收到收益或损失反馈。包含高奖赏与低奖赏条件，用于评估奖赏预期和结果加工阶段的神经活动。

---

## 仓库结构

```
├── questionnaires/
│   ├── cdi/
│   ├── masc/
│   └── psqi/
├── cognitive_tasks/
│   ├── n_back/
│   ├── wcst/
│   └── bart/
├── fmri_tasks/
│   └── guessing_task/
├── README.md
├── README_CN.md
└── LICENSE
```

## 运行环境

- PsychoPy ≥ [版本号]
- Python ≥ [版本号]

## 引用

如使用本仓库中的程序，请引用我们的研究方案论文：

> Tian X, Sun H, Li X, et al. A randomized controlled trial protocol comparing 10 Hz rTMS and iTBS for adolescent depression: clinical efficacy, neurocognitive and neurobiological mechanisms. [待补充]

## 联系方式

- 通讯作者：[待补充]
- 邮箱：[待补充]
