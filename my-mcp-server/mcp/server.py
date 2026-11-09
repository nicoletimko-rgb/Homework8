from mcp.server.fastmcp import FastMCP
from nba_api.stats.endpoints import playerindex
import pandas as pd

mcp = FastMCP("nba-api-explorer")


@mcp.tool()
def inspect_nba_players() -> dict:
    """Inspect available columns and sample values from the NBA PlayerIndex API."""

    response = playerindex.PlayerIndex(active_nullable="1")
    df = response.get_data_frames()[0]

    fields = []

    for column in df.columns:
        values = df[column].dropna()

        fields.append({
            "name": column,
            "type": str(df[column].dtype),
            "sample": (
                None if values.empty
                else str(values.iloc[0])
            ),
            "missing_count": int(df[column].isna().sum())
        })

    return {
        "total_players": len(df),
        "fields": fields
    }


if __name__ == "__main__":
    mcp.run()