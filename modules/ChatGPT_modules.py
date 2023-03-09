import random
import json
import openai
from loguru import logger
from pathlib import Path
import uuid

import sys

sys.path.append(str(Path(__file__).parent.parent))
from settings import openai_api_keys, openai_model


class CPTServer:
    def __init__(self, api_keys=openai_api_keys):
        self.__keys_pool = api_keys
        self.__chat_history = {}
        self.__current_key = api_keys[0]
        self.__token_count = {}
        openai.api_key = self.__current_key

    def add_api_key(self, api_key):
        if api_key in self.__keys_pool:
            logger.warning("Key already exists.")
        else:
            self.__keys_pool.append(api_key)

    def shuffle_api(self):
        logger.warning("API shuffled.")
        self.__current_key = random.choice(self.__keys_pool)
        openai.api_key = self.__current_key

    @staticmethod
    def parse_conversation(conversation, system_content='concise the response'):
        messages = [{
            'role': 'system',
            'content': system_content
        }]
        for c in conversation:
            messages.append(
                {
                    'role': c[0],
                    'content': c[1]
                }
            )
        return messages

    def ask(self, prompt, conversation_id=None, model=openai_model):
        if not conversation_id:
            conversation_id = uuid.uuid1().hex
        if conversation_id not in self.__chat_history:
            self.__chat_history[conversation_id] = []
            self.__token_count[conversation_id] = 0
        conversation = self.__chat_history[conversation_id]
        conversation.append(('user', prompt))
        res = openai.ChatCompletion.create(
            model=model,
            messages=self.parse_conversation(conversation)
        )
        # res = {'usage': 13}
        logger.debug(res)
        try:
            self.__token_count[conversation_id] += res['usage']['total_tokens']
            conversation.append(('assistant', res['choices'][0]['message']['content']))
        except Exception as e:
            logger.error(f"ERROR: Fail to get response. Exception: {str(e)}")
            logger.warning(json.dumps(res, indent=4, ensure_ascii=False))

        return res, conversation_id


if __name__ == "__main__":
    cptserver = CPTServer()
    cptserver.ask('Nihao')
    print(2)
