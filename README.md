
<div align="center">
  <a href=https://3d.hunyuan.tencent.com target="_blank"><img src=https://img.shields.io/badge/Official%20Site-333399.svg?logo=homepage height=22px></a>
  <a href=https://huggingface.co/spaces/tencent/Hunyuan3D-2  target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Demo-276cb4.svg height=22px></a>
  <a href=https://huggingface.co/tencent/Hunyuan3D-2 target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Models-d96902.svg height=22px></a>
  <a href=https://3d-models.hunyuan.tencent.com/ target="_blank"><img src= https://img.shields.io/badge/Page-bb8a2e.svg?logo=github height=22px></a>
  <a href=https://discord.gg/dNBrdrGGMa target="_blank"><img src= https://img.shields.io/badge/Discord-white.svg?logo=discord height=22px></a>
  <a href=https://arxiv.org/abs/2501.12202 target="_blank"><img src=https://img.shields.io/badge/Report-b5212f.svg?logo=arxiv height=22px></a>
  <a href=https://x.com/TencentHunyuan target="_blank"><img src=https://img.shields.io/badge/Hunyuan-black.svg?logo=x height=22px></a>
 <a href="#community-resources" target="_blank"><img src=https://img.shields.io/badge/Community-lavender.svg?logo=homeassistantcommunitystore height=22px></a>
</div>

[//]: # (  <a href=# target="_blank"><img src=https://img.shields.io/badge/Report-b5212f.svg?logo=arxiv height=22px></a>)

[//]: # (  <a href=# target="_blank"><img src= https://img.shields.io/badge/Colab-8f2628.svg?logo=googlecolab height=22px></a>)

[//]: # (  <a href="#"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/v/mulankit?logo=pypi"  height=22px></a>)

<br>


## **Abstract** 

This repository provides an adaptation of Hunyuan3D 2.0 for use in Google Colab, making it easier to run, experiment, and generate 3D assets in a cloud environment.

Hunyuan3D 2.0, originally developed by Tencent, is a large-scale 3D synthesis system designed to generate high-resolution, textured 3D assets. It is built upon two foundation components:

Hunyuan3D-DiT – a scalable flow-based diffusion transformer for 3D shape generation, ensuring geometry aligns correctly with input conditions.

Hunyuan3D-Paint – a texture synthesis model leveraging geometric and diffusion priors to produce vivid, high-resolution texture maps for both generated and manually crafted meshes.

In addition, the system includes Hunyuan3D-Studio, a versatile production platform that simplifies 3D asset creation and manipulation. It is designed for both professionals and enthusiasts, supporting mesh editing, re-creation, and even animation workflows.

The original research demonstrates that Hunyuan3D 2.0 surpasses previous state-of-the-art models—both open-source and proprietary—in geometry detail, condition alignment, and texture quality.

<p align="center">
  <img src="assets/images/system.jpg">
</p>

<p align="left">
  <img src="assets/images/arch.jpg">
</p>

### Get Started in Colab

Clone this repository in Colab:

```bash
!git clone https://github.com/AbimaelFranco/Hunyuan3D-2-Abimael.git
```

Install PyTorch (already included by default, but you can reinstall if needed):

```bash
!pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

Install the project requirements:

```bash
!pip install -r /content/Hunyuan3D-2/requirements.txt
!pip install -e /content/Hunyuan3D-2/.
```

Check that the image paths are correct:

```bash
!cat Hunyuan3D-2/shape_gen_multiview.py
```

Generate a 3D shape:

```bash
!python3 /content/Hunyuan3D-2/fast_shape_gen_multiview.py
```