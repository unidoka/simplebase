import os
import httpx

async def send_sms(phone: str, text: str) -> bool:
    api_key = os.getenv("PHONE_TOKEN")
    sender = os.getenv("PHONE_NAME_SENDER")
    provider_url = os.getenv("PHONE_PROVIDER_URL")

    print(text, phone, sender, api_key)

    async with httpx.AsyncClient(timeout=10, trust_env=None) as client:
        response = await client.post(
            provider_url,
            json={
                "sms": [
                    {
                        "text": text,
                        "phone": phone,
                        "sender": sender,
                        "channel": "char"
                    }
                ],
                "apiKey": api_key
            },
        )

    try:
        # response.raise_for_status()
        return True
    except:
        return False