#!/usr/bin/env python3

from llm_service import *

def run():
    chat_file = f"{env_var('alfred_workflow_data')}/chat.json"
    messages = read_chat(chat_file)
    assistant_message = next((message for message in reversed(messages) if message["role"] == "assistant"), None)
    if not assistant_message:
        return ""

    # Messages stored in chat history do not contain the assistant signature.
    # Previously we attempted to strip a non-existent prefix which resulted in
    # the first characters of the response being removed.
    return assistant_message["content"]

if __name__ == "__main__":
    print(run())