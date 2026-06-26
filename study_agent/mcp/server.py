from fastmcp import FastMCP
from study_agent.tools.pdf_reader import read_syllabus

mcp = FastMCP("VTU Study MCP")


@mcp.tool()
def get_syllabus():
    """
    Returns the complete VTU syllabus.
    """
    return read_syllabus()


if __name__ == "__main__":
    mcp.run()