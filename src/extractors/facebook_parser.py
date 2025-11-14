thonimport logging
from .utils_time import timestamp_now

class FacebookParser:
    def __init__(self):
        logging.info("FacebookParser initialized.")

    def parse_profile(self, profile_url: str):
        # Simulated scraping logic
        logging.info(f"Simulating scrape for {profile_url}")

        # Mocked profile data
        return [
            {
                "id": "mock123",
                "name": "John Doe",
                "image_uri": "https://example.com/profile.jpg",
                "profile_url": profile_url,
                "subtitle_text": "Sample Location",
                "gender": "MALE",
                "friendship_status": "CAN_REQUEST",
                "short_name": "John",
                "scraped_at": timestamp_now(),
            }
        ]