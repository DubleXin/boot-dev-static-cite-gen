from src.nodes.textnode.text_type import TextType
from src.nodes.textnode.textnode import TextNode

tn = TextNode(
    text="This is some anchor text",
    text_type=TextType.ANCOR.value,
    url="https://www.boot.dev",
)

print(tn)
