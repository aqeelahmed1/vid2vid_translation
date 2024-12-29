from invert import Inverter
from generate import Generator
from utils import load_config, init_model, seed_everything, get_frame_ids
# import config_path
import runpod
from utils import encode_video_to_base64,decode_base64_to_video
import yaml
import json
from pathlib import Path

# Default parameters
default_params = {
    "video_encoding":"",
    "sd_version": "2.1",
    "input_path": "data/dog.mp4",
    "work_dir": "outputs/dog",
    "height": 512,
    "width": 512,
    "inversion": {
        "save_path": "${work_dir}/latents",
        "prompt": "a dog walking on the ground near a bush.",
        "steps": 50,
        "save_intermediate": True,
        "save_steps": 50,
        "n_frames": 32
    },
    "generation": {
        "control": "pnp",
        "guidance_scale": 7.5,
        "n_timesteps": 50,
        "negative_prompt": "ugly, blurry, low res",
        "prompt": {
            "VG": "a dog walking on the ground near a bush, Van Gogh style.",
            "desert": "a dog walking in the desert near a bush."
        },
        "latents_path": "${work_dir}/latents",
        "output_path": "${work_dir}",
        "local_merge_ratio": 0.9,
        "global_merge_ratio": 0.8,
        "global_rand": 0.5
    },
    "seed": 123,
    "device": "cuda",
    "base_config": "configs/default.yaml",
    "float_precision": "fp16",
    "enable_xformers_memory_efficient_attention": True
}


def update_params_from_json(defaults, updates):
    """
    Updates default parameters with values from a JSON file.
    """

    def recursive_update(default, updates):
        for key, value in updates.items():
            if isinstance(value, dict) and isinstance(default.get(key), dict):
                recursive_update(default[key], value)
            else:
                default[key] = value

    recursive_update(defaults, updates)
    return defaults


def save_to_yaml(params, yaml_file):
    """
    Saves parameters to a YAML file.
    """
    with open(yaml_file, 'w') as f:
        yaml.dump(params, f, default_flow_style=False)


# # Input JSON file and output YAML file
# json_file = "updates.json"
# yaml_file = "parameters.yaml"

# Update parameters and save
# updated_params = update_params_from_json(default_params, json_file)
# save_to_yaml(updated_params, yaml_file)
# print(f"Updated parameters saved to '{yaml_file}'")


def handler(job):
    print('==start===')
    job_input = job['input']
    # Update parameters and save
    yaml_file='configs/user.yaml'
    # updated_params = update_params_from_json(default_params, job_input)
    if "video_encoding" in job_input:
        save_to_yaml(job_input, yaml_file)

        print(f"Updated parameters saved to '{yaml_file}'")
        decode_base64_to_video(job_input["video_encoding"],job_input["input_path"])
        del job_input["video_encoding"]

        config = load_config(yaml_file)
        pipe, scheduler, model_key = init_model(
            config.device, config.sd_version, config.model_key, config.generation.control, config.float_precision)
        config.model_key = model_key
        seed_everything(config.seed)

        print("Start inversion!")
        inversion = Inverter(pipe, scheduler, config)
        inversion(config.input_path, config.inversion.save_path)

        print("Start generation!")
        generator = Generator(pipe, scheduler, config)
        frame_ids = get_frame_ids(
            config.generation.frame_range, config.generation.frame_ids)
        path=generator(config.input_path, config.generation.latents_path,
                  config.generation.output_path, frame_ids=frame_ids)
        enc_out_vid=encode_video_to_base64(path)
        return enc_out_vid
    else:
        return {"test":"passed"}
runpod.serverless.start({"handler": handler})
