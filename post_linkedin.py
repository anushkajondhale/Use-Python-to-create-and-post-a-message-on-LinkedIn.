import os
import requests

# Load environment variables
access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")

# LinkedIn API endpoint for sharing posts
url = "https://api.linkedin.com/v2/ugcPosts"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}

# Replace with your LinkedIn ID (URN format: urn:li:person:<id>)
author = os.getenv("LINKEDIN_AUTHOR_URN")

post_data = {
    "author": author,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello LinkedIn 👋 - This post was published directly using Python! 🚀"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(url, headers=headers, json=post_data)

if response.status_code == 201:
    print("✅ Post created successfully on LinkedIn!")
else:
    print(f"❌ Failed to post. Status: {response.status_code}, Response: {response.text}")
