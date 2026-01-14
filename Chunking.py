

from pathlib import Path
from dataclasses import dataclass
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List, Optional, Dict, Any

import Load_Data

@dataclass(frozen=True)
class DataProcessing:
      file_path : Path
      chunk_size: int
      chunk_overlap: int

def chunks(cfg:DataProcessing) -> List[Document]:
    data = Load_Data.LoadData(cfg.file_path)
    docs = Load_Data.load_data(data)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size= cfg.chunk_size,
        chunk_overlap= cfg.chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""],
    )

    doc_chunk = text_splitter.split_documents(docs)

    return doc_chunk





