from datadir_writer import DatadirWriter
from pathlib import Path
writer = DatadirWriter(f"output_dir")
ibest_writer = writer[f"1best_recog"]
print(type(ibest_writer))
print(ibest_writer.fd)
print((Path(f"output_dir") / f"1best_recog").parent)

wavs = [r'./testwav/test.wav']
wavs = wavs[0:3]
print(wavs)
print(type(wavs))
for wav in wavs:
    print("1")
    print(wav)
    wav_splits = wav.strip().split()
    print(wav_splits)
    wav_name = wav_splits[0] if len(wav_splits) > 1 else "demo"
    print(wav_name)
    wav_path = wav_splits[1] if len(wav_splits) > 1 else wav_splits[0]
    print(wav_path)