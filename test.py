from run_vidtome import handler
from utils.utils import encode_video_to_base64,decode_base64_to_video
vid_enc=encode_video_to_base64('data/dog_inp.mp4')

inp_jason={
    "input":{
        "video_encoding":vid_enc,
        "input_path": "data/my_dogy.mp4",
        "prompt": {
            "desert": "a dog walking in the desert near a bush."
        }

    }
}

output=handler(inp_jason)
decode_base64_to_video(output,'data/dog_out.mp4')
