import json
from typing import Dict, List

SITE_DATA = {
    "name": "mk体育",
    "url": "https://zhcn-cn-mk.com",
    "tags": ["体育资讯", "赛事直播", "比分追踪", "运动社区"],
    "keywords": ["mk体育", "实时比分", "足球", "篮球", "体育新闻"],
    "description": "提供全方位体育赛事报道、即时比分更新及深度运动社区互动。",
    "sections": [
        {"title": "热门赛事", "content": "覆盖国内外足球、篮球、网球等主流赛事。"},
        {"title": "数据统计", "content": "运动员与球队的历史数据、实时统计对比。"},
        {"title": "专家分析", "content": "资深体育评论员赛前预测与赛后复盘。"},
    ],
    "features": ["多语言支持", "移动端适配", "推送通知", "无广告观看"],
}

def format_summary(data: Dict) -> str:
    lines = []
    lines.append(f"站点名称: {data['name']}")
    lines.append(f"访问地址: {data['url']}")
    lines.append(f"核心关键词: {', '.join(data['keywords'])}")
    lines.append(f"内容标签: {', '.join(data['tags'])}")
    lines.append(f"站点简介: {data['description']}")
    lines.append("")
    lines.append("站点栏目:")
    for sec in data["sections"]:
        lines.append(f"  - {sec['title']}: {sec['content']}")
    lines.append("")
    lines.append("功能特性:")
    for feat in data["features"]:
        lines.append(f"  + {feat}")
    return "\n".join(lines)

def export_json(data: Dict, indent: int = 2) -> str:
    return json.dumps(data, ensure_ascii=False, indent=indent)

def display_rich_summary(data: Dict) -> None:
    summary = format_summary(data)
    print("=" * 50)
    print("结构化摘要 (纯文本)")
    print("=" * 50)
    print(summary)
    print("\n" + "=" * 50)
    print("JSON 格式数据")
    print("=" * 50)
    print(export_json(data))

def main() -> None:
    display_rich_summary(SITE_DATA)

if __name__ == "__main__":
    main()