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

    style = job_input.get('style','ghibli')
    length=job_input.get('length',None)
    infile='input.mp4'
    outfile='out.mp4'

    if vid_base64 is not None:
        print('decoding')
        decode_base64_to_video(vid_base64,infile)
        main(infile,style,outfile,length)
        print('finished main')
        encoded_frames=encode_video_to_base64(outfile)
        print('finished')
        return encoded_frames
    else:
        return {"logs":"not processed"}


runpod.serverless.start({"handler": handler})
