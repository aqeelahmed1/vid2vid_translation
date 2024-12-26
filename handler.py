""" Example handler file. """
print('************* loading imports *************')
from utils import encode_video_to_base64,decode_base64_to_video
import runpod
from vid2cartoon import main

print('************* loaded pipeline *************')


def handler(job):
    """ Handler function that will be used to process jobs. """
    print('==start===')
    job_input = job['input']
    print(job_input)
    vid_base64 = job_input.get('video',None)
    style = job_input.get('style','Ryo Takemas')
    infile='input.mp4'
    outfile='out.mp4'
    decode_base64_to_video(vid_base64,infile)
    main(infile,style,outfile)
    encoded_frames=encode_video_to_base64(outfile)
    return encoded_frames


runpod.serverless.start({"handler": handler})
