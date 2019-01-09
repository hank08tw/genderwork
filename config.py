# coding:utf8
import warnings


class DefaultConfig(object):
    env = 'default'  # visdom 环境
    model = 'ResNet34'  # 使用的模型，名字必须与models/__init__.py中的名字一致

    train_data_root = './data/train'  # 训练集存放路径
    test_data_root = './data/test'  # 测试集存放路径
    visualize_data_root = './data/visualize'
    load_model_path = './checkpoints/resnet34_0108_17:35:50.pth' #'./checkpoints/resnet34_0103_11:48:12.pth'  # 加载预训练的模型的路径，为None代表不加载

    batch_size = 16  # batch size
    use_gpu = True  # user GPU or not
    num_workers = 4  # how many workers for loading data
    print_freq = 20  # print info every N batch

    debug_file = '/tmp/debug'  # if os.path.exists(debug_file): enter ipdb
    result_file = 'result.csv'

    max_epoch = 300
    lr = 0.001  # initial learning rate
    lr_decay = 0.9  # when val_loss increase, lr = lr*lr_decay
    weight_decay = 0e-5  # 损失函数

    lr_decay_epoch = 200 #多少個epoch會自動減少learning rate lr = lr * opt.lr_decay

    


def parse(self, kwargs):
    """
    根据字典kwargs 更新 config参数
    """
    for k, v in kwargs.items():
        if not hasattr(self, k):
            warnings.warn("Warning: opt has not attribut %s" % k)
        setattr(self, k, v)

    print('user config:')
    for k, v in self.__class__.__dict__.items():
        if not k.startswith('__'):
            print(k, getattr(self, k))


DefaultConfig.parse = parse
opt = DefaultConfig()
opt.parse = parse