import asyncio

from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.roles.role import RoleReactMode
from metagpt.schema import Message
from mytest.PrintOne import PrintOne
from mytest.PrintThird import PrintThird
from mytest.PrintTwo import PrintTwo


class FirstPrint(Role):
    name: str = "printFirst"
    profile: str = "printFirst"
    goal: str = "print first three content"
    constraints: str = "only print first three content"
    language: str = "chinese"

    topic: str = ""
    main_title: str = ""
    content: str = "heelo"
    total_content: str = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._init_actions([PrintOne,PrintTwo,PrintThird])
        self._set_react_mode(react_mode= RoleReactMode.REACT.value)

    async def _think(self) -> None:
        logger.info(self.rc.state)
        if self.rc.todo is None:
            self._set_state(0)
            return

        if self.rc.state + 1 < len(self.states):
            self._set_state(self.rc.state+1)
        else:
            self.rc.todo = None


    async def _act(self)-> Message:
        todo = self.rc.todo
        msg = self.rc.memory.get(k=1)[0]
        self.content = msg.content
        resp = await todo.run(content=self.content)
        logger.info(resp)
        if self.total_content != "":
            self.total_content += "\n\n\n"
        self.total_content += resp
        return Message(content=resp, role=self.profile)

    async def _react(self) -> Message:
        while True:
            await self._think()
            if self.rc.todo is None:
                break
            msg = await self._act()
            return msg

async def main():
    msg = "Git 教程"
    role = FirstPrint()
    logger.info(msg)
    result = await role.run(msg)
    logger.info(result)

asyncio.run(main())





