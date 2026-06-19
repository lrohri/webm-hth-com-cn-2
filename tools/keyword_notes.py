from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

# 配置示例数据
SAMPLE_URL = "https://webm-hth.com.cn"
SAMPLE_KEYWORD = "华体会"

@dataclass
class KeywordNote:
    """用 dataclass 组织关键词笔记"""
    keyword: str
    context: str
    url: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def summary(self) -> str:
        """返回简要摘要"""
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return f"[{self.keyword}] {self.context[:30]}... 标签: {tag_str}"

    def to_dict(self) -> dict:
        """转为字典，方便 JSON 输出"""
        return {
            "keyword": self.keyword,
            "context": self.context,
            "url": self.url,
            "tags": self.tags,
            "created_at": self.created_at,
        }


def format_note_table(notes: List[KeywordNote]) -> str:
    """生成格式化的笔记表格文本"""
    if not notes:
        return "（无笔记）"

    lines = []
    lines.append(f"{'关键词':<10} {'内容摘要':<30} {'标签':<20} {'日期':<20}")
    lines.append("-" * 80)

    for note in notes:
        context_preview = note.context[:28] + ".." if len(note.context) > 28 else note.context
        tag_str = ", ".join(note.tags[:3]) if note.tags else "-"
        lines.append(
            f"{note.keyword:<10} {context_preview:<30} {tag_str:<20} {note.created_at:<20}"
        )

    return "\n".join(lines)


def format_note_detailed(notes: List[KeywordNote]) -> str:
    """生成详细的笔记文本"""
    parts = []
    for i, note in enumerate(notes, 1):
        parts.append(
            f"笔记 {i}:\n"
            f"  关键词: {note.keyword}\n"
            f"  内容:   {note.context}\n"
            f"  URL:    {note.url}\n"
            f"  标签:   {', '.join(note.tags) if note.tags else '无'}\n"
            f"  创建:   {note.created_at}\n"
        )
    return "\n".join(parts)


def demo_notes() -> List[KeywordNote]:
    """生成一些示例笔记，包含配置中的 URL 和关键词"""
    return [
        KeywordNote(
            keyword=SAMPLE_KEYWORD,
            context="华体会是用户关注的重点关键词，常用于品牌或活动场景。",
            url=SAMPLE_URL,
            tags=["品牌", "活动", "热门"],
        ),
        KeywordNote(
            keyword="数据分析",
            context="分析关键词'华体会'的搜索趋势和用户画像。",
            url=SAMPLE_URL + "/analytics",
            tags=["分析", "趋势", "用户"],
        ),
        KeywordNote(
            keyword="内容策略",
            context="针对华体会关键词制定内容创作计划。",
            url=SAMPLE_URL + "/content-strategy",
            tags=["策略", "内容"],
        ),
    ]


if __name__ == "__main__":
    notes = demo_notes()
    print("=== 笔记表格 ===")
    print(format_note_table(notes))
    print("\n=== 笔记详情 ===")
    print(format_note_detailed(notes))