from metagpt.actions import Action


class PrintOne(Action):
    name: str = "print the first"
    content: str = ""
    language: str = "english"

    async def run(self, content: str, *args, **kwargs):
        PRINT_PROMPT = """
        You are the print writer, we need you run the first action to print the content.
        """

        PRINT_CONTENT = PRINT_PROMPT + """
        Now I will give you the content, please use {language} to translate it and print it
        {content}
        """

        prompt = PRINT_CONTENT.format(content=content, language=self.language)
        return await self._aask(prompt=prompt)