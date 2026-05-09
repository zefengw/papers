# ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation

**Field**: AI (Computer Vision, Video Generation)
**Link**: http://arxiv.org/abs/2605.06667v1

## Summary
ActCam presents a zero-shot method for video generation that jointly controls both the character's motion and the camera trajectory. It works by generating pose and depth conditions from a source video and target camera motion, then using a single sampling process with a two-phase conditioning schedule (pose+depth early on, pose-only later) on any pretrained image-to-video diffusion model.

## Why it matters
Provides fine-grained, independent control of both the actor and the camera in video generation without requiring expensive paired training data or fine-tuning, directly enabling artistic and cinematic applications.

## Implementation Notes
As ActCam requires a pretrained image-to-video diffusion model, depth estimation, and pose estimation frameworks, a full implementation is beyond the scope of this repository.

The `impl/` folder contains a scaffold demonstrating the core algorithm's two-phase conditioning logic for the sampling loop, assuming an underlying diffusion model API.