from langchain_core.tools import tool
from tavily import TavilyClient

from dotenv import load_dotenv
import os
from  app.api.monitor import monitor

load_dotenv()


tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY"),
)



@tool
def search_tavily(
        query: str,
        max_results: int = 3,
        topic: str = "all",
        include_raw_content: bool = False
                  ) :
    """
    根据用户问题检索互联网公开信息

    注意：本工具只用于外部公开网页、新闻、政策等信息，不用于查询业务数据库或 RAGFlow 私有知识库
    """

    monitor.report_tool(
        "search_tavily",
        {"query": query, "max_results": max_results, "topic": topic, "include_raw_content": include_raw_content}
    )

    return  tavily_client.search(
        query=query,
        max_results=max_results,
        topic=topic,
        include_raw_content=include_raw_content
    )