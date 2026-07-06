# Running AI Coach (AI-KB)

一个基于心率 + 配速的跑步AI教练系统（MVP）

## 功能
- 根据心率区间推荐训练
- 根据疲劳状态调整训练强度
- 支持5K/10K/半马训练结构

## 架构
用户数据 → 教练规则引擎 → RAG知识库 → AI输出建议

## API
POST /coach
{
  "hr": 150,
  "pace": "5:30",
  "fatigue": 0.3
}

## 状态
MVP版本，可扩展为SaaS AI教练系统