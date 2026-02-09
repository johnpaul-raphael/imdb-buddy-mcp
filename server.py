from mcp.server.fastmcp import FastMCP
import httpx
import os
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("MovieExplorer")

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

logger.info(f"Starting MovieExplorer MCP server")
logger.info(f"TMDB_API_KEY set: {bool(TMDB_API_KEY)}")

# Common TMDB Genre IDs
GENRES = {
    "action": 28, "adventure": 12, "animation": 16, "comedy": 35,
    "crime": 80, "documentary": 99, "drama": 18, "family": 10751,
    "fantasy": 14, "history": 36, "horror": 27, "mystery": 9648,
    "romance": 10749, "sci-fi": 878, "thriller": 53, "war": 10752, "western": 37
}

@mcp.tool()
async def find_movies(media_type: str = "movie", min_rating: float = 7.0, language: str = "en", genre_name: str = None) -> str:
    """
    Find movies or TV series based on rating, language, and genre.
    
    Args:
        media_type: Use 'movie' for films or 'tv' for web series/shows.
        min_rating: Minimum rating (0.0 to 10.0).
        language: ISO code like 'en', 'es', 'fr', 'hi'.
        genre_name: Optional genre like 'action', 'comedy', 'sci-fi', etc
    """
    if not TMDB_API_KEY:
        return "Error: TMDB_API_KEY not set in environment."

    endpoint = f"{TMDB_BASE_URL}/discover/{media_type}"
    
    # Setup query parameters
    params = {
        "api_key": TMDB_API_KEY,
        "vote_average.gte": min_rating,
        "with_original_language": language,
        "sort_by": "popularity.desc",
        "vote_count.gte": 50  # Ensures we get quality results, not obscure ones
    }

    # Add genre filter if provided
    if genre_name and genre_name.lower() in GENRES:
        params["with_genres"] = GENRES[genre_name.lower()]

    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, params=params)
        if response.status_code != 200:
            return f"Failed to fetch from TMDB: {response.text}"
        
        data = response.json()

    results = data.get("results", [])
    if not results:
        return f"No {media_type} found with rating > {min_rating} in {language}."

    # Format the dynamic response
    formatted_list = []
    for item in results[:8]:
        title = item.get("title") or item.get("name")
        date = item.get("release_date") or item.get("first_air_date", "Unknown")
        rating = item.get("vote_average")
        summary = item.get("overview", "No description available.")
        
        formatted_list.append(
            f"### {title} ({date[:4]})\n"
            f"⭐ **Rating:** {rating}/10\n"
            f"📝 **Plot:** {summary}\n"
        )

    return "\n---\n".join(formatted_list)

if __name__ == "__main__":
    # Use 'stdio' for Claude Desktop; switch to 'http' for remote/ChatGPT use
    # AWS Lambda Web Adapter will call this on port 8080
    port = int(os.environ.get("PORT", "8080"))
    logger.info(f"Starting server on port {port} with SSE transport")
    mcp.run(transport="sse")
