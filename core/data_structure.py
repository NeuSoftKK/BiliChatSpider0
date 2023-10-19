from typing import List


class ReplyNode:
    def __init__(self, username: str, content: str):
        self.username: str = username
        self.content: str = content
        self.children: List[ReplyNode] = []

    def __dict__(self):
        return {
            "username": self.username,
            "content": self.content,
            "children": [child.__dict__() for child in self.children]
        }

    def __len__(self):
        count = len(self.children) + 1
        if len(self.children) != 0:
            for child in self.children:
                count += child.__len__()
        return count

    def add(self, node):
        if node is not None:
            self.children.append(node)

    def find(self, username):
        if self.username == username:
            return self

        for node in self.children:
            result = node.find(username)
            if result is not None:
                return result

        return None
