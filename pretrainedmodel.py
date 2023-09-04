!pip install anvil-uplink
'''Collecting anvil-uplink
  Downloading anvil_uplink-0.4.2-py2.py3-none-any.whl (90 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.1/90.1 kB 1.9 MB/s eta 0:00:00
Collecting argparse (from anvil-uplink)
  Downloading argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Requirement already satisfied: future in /usr/local/lib/python3.10/dist-packages (from anvil-uplink) (0.18.3)
Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from anvil-uplink) (1.16.0)
Collecting ws4py (from anvil-uplink)
  Downloading ws4py-0.5.1.tar.gz (51 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 51.4/51.4 kB 8.1 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: ws4py
  Building wheel for ws4py (setup.py) ... done
  Created wheel for ws4py: filename=ws4py-0.5.1-py3-none-any.whl size=45227 sha256=4feb5b8974ec19fe18373f3ca995a0cd4f1493b651067dd6e5413974d6021211
  Stored in directory: /root/.cache/pip/wheels/2e/7c/ad/d9c746276bf024d44296340869fcb169f1e5d80fb147351a57
Successfully built ws4py
Installing collected packages: ws4py, argparse, anvil-uplink
Successfully installed anvil-uplink-0.4.2 argparse-1.4.0 ws4py-0.5.1
'''

import anvil.server

anvil.server.connect("server_MK2NMXZ4WH6WJPOOU3QMQ7NF-DQXWEA7LS2KJRUZL")
'''Connecting to wss://anvil.works/uplink
Anvil websocket open
Connected to "Default Environment" as SERVER
'''
!pip install --upgrade huggingface_hub

from huggingface_hub import notebook_login
notebook_login()

'''Collecting huggingface_hub
  Downloading huggingface_hub-0.16.4-py3-none-any.whl (268 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 268.8/268.8 kB 5.6 MB/s eta 0:00:00
Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (3.12.2)
Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (2023.6.0)
Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (2.27.1)
Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (4.65.0)
Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (6.0.1)
Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (4.7.1)
Requirement already satisfied: packaging>=20.9 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (23.1)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (1.26.16)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (2023.7.22)
Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (3.4)
Installing collected packages: huggingface_hub
Successfully installed huggingface_hub-0.16.4
Hugging Face
Copy a token from your Hugging Face tokens page and paste it below.
Immediately click login after copying your token or it might be stored in plain text in this notebook file.
Token:
'''

!pip install -qq -U diffusers transformers

from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained('runwayml/stable-diffusion-v1-5').to('cuda')

import torch

'''━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 22.1 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.4/7.4 MB 97.2 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 72.4 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.8/7.8 MB 104.4 MB/s eta 0:00:00
The cache for model files in Transformers v4.22.0 has been updated. Migrating your old cache. This is a one-time only operation. You can interrupt this and resume the migration later on by calling `transformers.utils.move_cache()`.
0/0 [00:00<?, ?it/s]
Downloading (…)ain/model_index.json: 100%
541/541 [00:00<00:00, 25.4kB/s]
Fetching 15 files: 100%
15/15 [00:34<00:00, 2.36s/it]
Downloading (…)_encoder/config.json: 100%
617/617 [00:00<00:00, 24.6kB/s]
Downloading (…)tokenizer/merges.txt: 100%
525k/525k [00:00<00:00, 18.9MB/s]
Downloading model.safetensors: 100%
1.22G/1.22G [00:20<00:00, 64.0MB/s]
Downloading (…)okenizer_config.json: 100%
806/806 [00:00<00:00, 21.7kB/s]
Downloading (…)tokenizer/vocab.json: 100%
1.06M/1.06M [00:00<00:00, 26.5MB/s]
Downloading model.safetensors: 100%
492M/492M [00:10<00:00, 43.4MB/s]
Downloading (…)cheduler_config.json: 100%
308/308 [00:00<00:00, 5.67kB/s]
Downloading (…)_checker/config.json: 100%
4.72k/4.72k [00:00<00:00, 52.6kB/s]
Downloading (…)cial_tokens_map.json: 100%
472/472 [00:00<00:00, 6.47kB/s]
Downloading (…)rocessor_config.json: 100%
342/342 [00:00<00:00, 2.88kB/s]
Downloading (…)7f0/unet/config.json: 100%
743/743 [00:00<00:00, 16.2kB/s]
Downloading (…)ch_model.safetensors: 100%
3.44G/3.44G [00:31<00:00, 243MB/s]
Downloading (…)57f0/vae/config.json: 100%
547/547 [00:00<00:00, 6.37kB/s]
Downloading (…)ch_model.safetensors: 100%
335M/335M [00:09<00:00, 24.6MB/s]
Cannot initialize model with low cpu memory usage because `accelerate` was not found in the environment. Defaulting to `low_cpu_mem_usage=False`. It is strongly recommended to install `accelerate` for faster and less memory-intense model loading. You can do so with: 
```
pip install accelerate
```
.
Loading pipeline components...: 100%
7/7 [00:38<00:00, 5.66s/it]
`text_config_dict` is provided which will be used to initialize `CLIPTextConfig`. The value `text_config["id2label"]` will be overriden.
`text_config_dict` is provided which will be used to initialize `CLIPTextConfig`. The value `text_config["bos_token_id"]` will be overriden.
`text_config_dict` is provided which will be used to initialize `CLIPTextConfig`. The value `text_config["eos_token_id"]` will be overriden.
'''

@anvil.server.callable
def generate_moodboard(enter_prompt):
  #print(pipe(enter_prompt).images[0])
  # imggg = pipe(enter_prompt).images[0]
  # return imggg
  prompt = "Moodboard for " + enter_prompt
  imgg= pipe(prompt).images[0]
  imgg.show(imgg)
  imgg.save(prompt + '.jpg')
  return imgg

anvil.server.wait_forever()