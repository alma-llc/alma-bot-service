from app.prompts import BASE_SYSTEM_PROMPT


class PromptBuilder:
    def _get_system_prompt(self):
        return BASE_SYSTEM_PROMPT

    def build_chat_prompt(self):
        # TODO: Modify chat prompt
        return self._get_system_prompt()
