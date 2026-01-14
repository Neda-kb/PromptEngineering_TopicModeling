import os

from groq import Groq
from dataclasses import dataclass
from langchain_groq import ChatGroq

@dataclass(frozen=True)
class LLMSetting:
    MODEL: str
    TEMPERATURE :int

def setting(cfg:LLMSetting):

    # Groq LLM
    client = Groq(
        api_key=os.environ.get('GROQ_API_KEY'),
    )

    llm = ChatGroq(model=cfg.MODEL , temperature=cfg.TEMPERATURE)
    return llm
