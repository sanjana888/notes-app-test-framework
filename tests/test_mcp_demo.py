from utils.mcp_utils import MCPUtils


def test_mcp_data_generation():

    title = MCPUtils.generate_note_title()
    description = MCPUtils.generate_note_description()

    print("Generated Title:", title)
    print("Generated Description:", description)

    assert title.startswith("MCP_Note_")


def test_mcp_locator_suggestion():

    locator = MCPUtils.suggest_locator()

    print(locator)

    assert "primary_locator" in locator


def test_mcp_failure_analysis():

    result = MCPUtils.analyze_failure(
        "NoSuchElementException"
    )

    print(result)

    assert result == "Locator issue detected"
