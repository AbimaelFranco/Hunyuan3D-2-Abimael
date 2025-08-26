
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

We present Hunyuan3D 2.0, an advanced large-scale 3D synthesis system for generating high-resolution textured 3D assets.
This system includes two foundation components: a large-scale shape generation model - Hunyuan3D-DiT, and a large-scale
texture synthesis model - Hunyuan3D-Paint.
The shape generative model, built on a scalable flow-based diffusion transformer, aims to create geometry that properly
aligns with a given condition image, laying a solid foundation for downstream applications.
The texture synthesis model, benefiting from strong geometric and diffusion priors, produces high-resolution and vibrant
texture maps for either generated or hand-crafted meshes.
Furthermore, we build Hunyuan3D-Studio - a versatile, user-friendly production platform that simplifies the re-creation
process of 3D assets. It allows both professional and amateur users to manipulate or even animate their meshes
efficiently.
We systematically evaluate our models, showing that Hunyuan3D 2.0 outperforms previous state-of-the-art models,
including the open-source models and closed-source models in geometry details, condition alignment, texture quality, and
e.t.c.



<p align="center">
  <img src="assets/images/system.jpg">
</p>

## ☯️ **Hunyuan3D 2.0**

### Architecture

Hunyuan3D 2.0 features a two-stage generation pipeline, starting with the creation of a bare mesh, followed by the
synthesis of a texture map for that mesh. This strategy is effective for decoupling the difficulties of shape and
texture generation and also provides flexibility for texturing either generated or handcrafted meshes.

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