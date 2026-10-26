from src.nodes.utils.block.block_type import BlockType


def block_to_block_type(block: str) -> BlockType:
    def check_heading() -> bool:
        is_heading = False
        for i, char in enumerate(block):
            if char == "#" and i < 6:
                continue
            if char == " ":
                is_heading = True
            break
        return is_heading

    def check_code() -> bool:
        return block[:4] == "```\n" and block[-3:] == "```"

    def check_quote() -> bool:
        for line in block.split("\n"):
            if not line:
                return False
            if line[0] != ">":
                return False
        return True

    def check_ul():
        for line in block.split("\n"):
            if not line:
                return False
            if line[:2] != "- ":
                return False
        return True

    def check_ol() -> bool:
        splitted = block.split("\n")
        last_dot_index = -1

        for i, line in enumerate(splitted):
            if not line:
                return False

            dot_index = line.index(".", 1) if "." in line[1:] else None

            if dot_index is None:
                return False

            if line[dot_index + 1 : dot_index + 2] != " ":
                return False

            if not line[:dot_index].isnumeric():
                return False

            if i > 0 and int(line[:dot_index]) - 1 != int(
                splitted[i - 1][:last_dot_index]
            ):
                return False

            last_dot_index = dot_index

        return True

    if not block or len(block) == 0:
        return BlockType.PARAGRAPH
    if block[0] == "#" and check_heading():
        return BlockType.HEADING
    if len(block) > 6 and check_code():
        return BlockType.CODE
    if len(block) > 0 and block[0] == ">" and check_quote():
        return BlockType.QUOTE
    if len(block) > 1 and block[:2] == "- " and check_ul():
        return BlockType.ULIST
    if len(block) > 1 and "." in block and check_ol():
        return BlockType.OLIST

    return BlockType.PARAGRAPH
