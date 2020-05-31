
from utils.model import Model
import os

m = Model(
        #使用os的路径，避免了路径找不到的问题
        # os.path.normpath('/root/couplet-master/data/dl-data/couplet/train/in.txt'),
        # os.path.normpath('/root/couplet-master/data/dl-data/couplet/train/out.txt'),
        # os.path.normpath('/root/couplet-master/data/dl-data/couplet/test/in.txt'),
        # os.path.normpath('/root/couplet-master/data/dl-data/couplet/test/out.txt'),
        # os.path.normpath('/root/couplet-master/data/dl-data/couplet/vocabs.txt'),
        os.path.normpath('../static/data/dl-data/couplet/train/in.txt'),
        os.path.normpath('../static/data/dl-data/couplet/train/out.txt'),
        os.path.normpath('../static/data/dl-data/couplet/test/in.txt'),
        os.path.normpath('../static/data/dl-data/couplet/test/out.txt'),
        os.path.normpath('../static/data/dl-data/couplet/vocabs.txt'),
        num_units=1024, layers=4, dropout=0.2,
        batch_size=10, learning_rate=0.001,
        output_dir=os.path.normpath('../static/data/dl-data/models/tf-lib/output_couplet'),
        restore_model=False)

m.train(5000000)
