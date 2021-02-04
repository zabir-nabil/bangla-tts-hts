# HTS bangla text to speech 

## hts_engine — HMM-based speech synthesis engine

### Instructions

* Install hts in linux machine

* run `python3 cmd_gen.py` 

* A `gen_wav.sh` file will be generated.

* Run `chmod +x gen_wav.sh; chmod +x Bengali_HTS.sh`

* Finally, run `sudo sh gen_wav.sh` 

* It can't handle punctuations, numeric values or any latin characters.

Ref: https://github.com/sankar-mukherjee/Bengali-HTS (this repo is a clone of Bengali-HTS with some modifications to work with multiple inputs and `bakta_bang` dataset)

**For better speech synthesis, use https://github.com/zabir-nabil/bangla-tts**
