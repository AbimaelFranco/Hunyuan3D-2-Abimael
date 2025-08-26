<p align="center">
  <img src="assets/images/system.jpg">
</p>

<div align="center">
  <a href="https://3d-models.hunyuan.tencent.com/" target="_blank"><img src="https://img.shields.io/badge/Oficial%20website-333399.svg?logo=homepage" height="22px"></a>
  <a href="https://github.com/Tencent-Hunyuan/Hunyuan3D-2" target="_blank"><img src="https://img.shields.io/badge/Original%20repo-2b6cb0.svg?logo=github" height="22px"></a>
</div>

## **Abstract** 

This repository provides an adaptation of Hunyuan3D 2.0 for use in Google Colab, making it easier to run, experiment, and generate 3D assets in a cloud environment.

Hunyuan3D 2.0, originally developed by Tencent, is a large-scale 3D synthesis system designed to generate high-resolution, textured 3D assets. It is built upon two foundation components:

Hunyuan3D-DiT – a scalable flow-based diffusion transformer for 3D shape generation, ensuring geometry aligns correctly with input conditions.

Hunyuan3D-Paint – a texture synthesis model leveraging geometric and diffusion priors to produce vivid, high-resolution texture maps for both generated and manually crafted meshes.

In addition, the system includes Hunyuan3D-Studio, a versatile production platform that simplifies 3D asset creation and manipulation. It is designed for both professionals and enthusiasts, supporting mesh editing, re-creation, and even animation workflows.

The original research demonstrates that Hunyuan3D 2.0 surpasses previous state-of-the-art models—both open-source and proprietary—in geometry detail, condition alignment, and texture quality.

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
!pip install -r /content/Hunyuan3D-2-Abimael/requirements.txt
!pip install -e /content/Hunyuan3D-2-Abimael/.
```

Check that the image paths are correct:

```bash
!cat Hunyuan3D-2-Abimael/shape_gen_multiview.py
```

Generate a 3D shape:

```bash
!python3 /content/Hunyuan3D-2-Abimael/fast_shape_gen_multiview.py
```
