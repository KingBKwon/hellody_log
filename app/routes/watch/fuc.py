from datetime import datetime
from app.load_file.get_txt import upload_s3
input_data = ''
i = 0
async def insert_s3(user_id: str, vod_id: int):
    global input_data
    global i
    start_time = datetime.now()
    user_id = user_id
    vod_id = vod_id

    input_data = input_data + f'{user_id},{vod_id},{start_time}\n'
    i += 1
    if i > 10:
        await upload_s3(input_data)
        i = 0
        input_data = ''
        return 's3 업로드'

# Example usage
# import asyncio
# asyncio.run(insert_s3("user123", 1))
