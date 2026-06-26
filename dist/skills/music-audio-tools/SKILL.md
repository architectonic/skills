---
name: music-audio-tools
description: Generate, analyze, and shape music and audio workflows. Use when the user wants songwriting prompts, AI song generation, music composition, sound effects, or audio inspection and visualization.
tags: [media, agent-skill]
type: Playbook
---

# music-audio-tools

Use this umbrella skill for music-centric creative and analytical work.

## Coverage
### Songwriting and prompting
- structure, hooks, rhyme, adaptation strategy
- turning lyrics or concepts into stronger generation prompts

### AI music and sound generation
- text-to-music workflows
- lyric-driven song generation
- sound effects and environmental audio
- model/tool choice based on quality, speed, and constraints

### Audio analysis and visualization
- spectrograms, mel/chroma/MFCC-style inspection
- visual QA on tracks, stems, and generated audio
- feature views for debugging or comparing outputs

## Provider and model selection
Do not hide available model/provider choice.

1. Discover what music/audio providers, APIs, local models, and keys are actually available.
2. Match the provider to the request:
   - lyric-heavy or prompt-driven song generation -> the strongest music-generation route available
   - sound design or environmental audio -> the strongest audio-generation route available
   - analysis / inspection -> local analysis tools or audio feature workflows
3. Prefer the best available model for the task rather than defaulting to a weaker generic route.
4. If no suitable provider is configured, tell the user what key, model, dependency, or local runtime is missing and how to add it.
5. Do not suppress knowledge of specific available routes just because a broad umbrella already exists.

## Selection guide
- User wants help writing lyrics or a stronger music prompt -> songwriting path
- User wants to create music or sound from text -> generation path
- User wants to inspect or visualize an audio file -> analysis path

## Operating rules
1. Separate creative writing from model execution from audio QA.
2. Check hardware/runtime constraints before promising local generation.
3. Report what was actually generated or analyzed, not generic praise.
4. Use inspection to verify quality when possible.
5. If a requested route is unavailable, explain the gap instead of dropping the capability.
6. If the user did not specify a provider or model, choose the best available one for the task.

## Practical routes to check
- Local/open-source text-to-music or sound generation models if installed
- Hosted music APIs if configured in the environment
- Audio analysis libraries for waveform, spectrogram, and feature inspection
- Specialized sound-design routes when the task is not song writing

## Pitfalls
- Requests often mix lyric writing, prompt engineering, and model execution; decide which layer the user actually wants.
- Open-source generation stacks can be VRAM-heavy and dependency-fragile.
- Spectrograms are diagnostic tools, not replacements for listening.
