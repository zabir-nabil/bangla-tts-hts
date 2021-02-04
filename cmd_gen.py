import json

bang_f = json.load(open("bakta_bang.json"))

cmd = open("gen_wav.sh", "w")
cmd.write("#!/bin/bash\n")
cmd.write('echo "This script is about to run another script."\n')
cnt = 1
for sen in bang_f:
    # print(sen)
    f = open(f"out/input_{cnt}", "w")
    f.write(''.join(c for c in sen["Sentence"] if c not in ",:!।?-"))
    f.close()
    cmd.write(f"sh Bengali_HTS.sh out/input_{cnt} out/hts_{cnt}.wav\n")
    cnt += 1

cmd.write('echo "The wav files are generated inside out folder."\n')

cmd.close()