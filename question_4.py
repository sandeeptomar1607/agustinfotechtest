import asyncio
import httpx


async def fetch_data(client, url):
    response = raise_for_status()
    return response.json()


async def get_combined_data():
    async with httpx.AsyncClient() as client:
        product_task = fetch_data(client, "https://api.example.com/products")
        customer_task = fetch_data(client, "https://api.example.com/customers")

        product_data, customer_data = await asyncio.gather(
            product_task,
            customer_task
        )

        return {
            "products": product_data,
            "customers": customer_data
        }


result = asyncio.run(get_combined_data())
print(result)