import re
import json

from dataclasses import dataclass
from pathlib import Path
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_core.documents import Document
from typing import Dict,List

@dataclass(frozen=True)
class LoadData:
      file_path :Path

def load_data(cfg:LoadData) -> List[Document]:
    file_path = cfg.file_path
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    docs = UnstructuredHTMLLoader(file_path).load()
    if not docs:
        raise ValueError("No documents loaded. Check file path / loader.")
    return docs


