

# for local testing
import asyncio
import aiohttp
import os
import runpod
from runpod import AsyncioEndpoint, AsyncioJob
import time
# add your api key and endpoint
runpod.api_key = "rpa_D9XRLH8KTWPKL5J7FFG7SXLCU8WENZQHRZ4NCUSUzrmx3c"
end_point='v5smla5kg7wwq7'
end_point='332ilg7hznghpa' #vid to vid
import base64
from PIL import Image
from io import BytesIO

def encode_video_to_base64(video_file_path):
    """
    Encodes a video file to a Base64 string.
    :param video_file_path: Path to the video file.
    :return: Base64 encoded string.
    """
    with open(video_file_path, 'rb') as video_file:
        # Read the video file as binary
        video_bytes = video_file.read()

        # Encode binary data to Base64
        base64_encoded = base64.b64encode(video_bytes).decode('utf-8')

    return base64_encoded

def decode_base64_to_video(base64_string, output_file_path):
    """
    Decodes a Base64 string to a video file.
    :param base64_string: Base64 encoded string.
    :param output_file_path: Path to save the decoded video file.
    """
    # Decode Base64 string to binary data
    video_bytes = base64.b64decode(base64_string)

    # Write the binary data to a video file
    with open(output_file_path, 'wb') as video_file:
        video_file.write(video_bytes)


vid=encode_video_to_base64('dataset/01.mp4')

async def main():
    start=time.time()
    async with aiohttp.ClientSession() as session:

        input_payload = {
            # "mode": "txt2video",
            "video": vid,
            "style":"ghibli"
            # "input_image": img,
            # "num_frames": 48,
            # "guidance_scale": 6,
            # "aspect_ratio": "1:1",
            # "num_inference_steps": 50,
            # "max_sequence_length": 226,
            # "fps": 8

        }
        endpoint = AsyncioEndpoint(end_point, session)
        job: AsyncioJob = await endpoint.run(input_payload)

        # Polling job status
        while True:
            status = await job.status()
            print(f"Current job status: {status}")
            if status == "COMPLETED":
                output = await job.output()
                print("Job output:", output)
                decode_base64_to_video(output,'output.mp4')
                break  # Exit the loop once the job is completed.
            elif status in ["FAILED"]:
                print("Job failed or encountered an error.")

                break
            else:
                print("Job in queue or processing. Waiting 3 seconds...")
                await asyncio.sleep(3)  # Wait for 3 seconds before polling again
    print("time elapsed:",time.time()-start)

if __name__ == "__main__":
    asyncio.run(main())
