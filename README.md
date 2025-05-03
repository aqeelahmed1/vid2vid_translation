# 🎬 VidToMe: Serverless Video Style Transfer with Stable Diffusion (RunPod Deployment)

This repository provides a serverless deployment template for **VidToMe (Video Token Merging)**, a zero-shot video editing technique based on **Stable Diffusion**, originally proposed in the CVPR 2024 paper:

> **VidToMe: Video Token Merging for Zero-Shot Video Editing**  
> [Paper](https://arxiv.org/abs/2312.06644) | [Official Code](https://github.com/VidToMe/VidToMe)

---

## 🚀 What This Repo Does

This repo adapts the original VidToMe implementation for **RunPod’s serverless GPU architecture**, enabling:

- 🎨 **Video style transfer**: Convert real-world videos into animations or other stylized forms.
- ⚙️ **Serverless deployment**: Easily run it as an API on [RunPod](https://www.runpod.io/).
- 🔁 **Efficient cloud inference**: Deploy without needing a local GPU.

---

## 🛠️ My Contribution

- ✅ Refactored the original VidToMe repo for RunPod serverless compatibility.
- ✅ Added `handler.py`, `Dockerfile`, and input handling for API endpoints.
- ✅ Provided a lightweight interface for style transfer using Stable Diffusion models.

---


## ⚙️ Deployment on RunPod

### 1. Clone this repo

```bash
git clone https://github.com/your-username/vidtome-runpod-deployment.git
cd vidtome-runpod-deployment
```

### 2. Set up a Serverless Endpoint

1. Go to [RunPod](https://www.runpod.io/).
2. Click **Serverless > Create Endpoint**.
3. Choose **"Custom Template"** and connect this repo.
4. RunPod will detect `handler.py` and the `Dockerfile`.

---

### 3. Input Example

```json
    {
        "video_encoding":"your base64 encoded video",
        "prompt": {
            "desert": "a dog walking in the desert near a bush."
        }
    }
```

---

## 📥 Test API Call

```bash
curl -X POST https://api.runpod.ai/v2/YOUR-ENDPOINT-ID/run \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d @test_input.json
```

---

## 📜 Acknowledgments

This implementation builds directly on:

> **VidToMe: Video Token Merging for Zero-Shot Video Editing**  
> CVPR 2024  
> Authors: Dongdong Chen, Mingyu Ding, Yujun Shen, et al.  
> [https://github.com/VidToMe/VidToMe](https://github.com/VidToMe/VidToMe)

Credit for the core method and model belongs entirely to the original authors. This repository simply adapts their amazing work for serverless deployment.

---

