"""
함수로 두가지 버전을 만들어봤습니다.
첫 번째 버전, vgg_block을 만들고 하나씩 적어서 작성해봤습니다.
두 번째 버전, 함수 안에 vgg_block 함수를 넣어서 작성해 봤습니다.
세 번재 버전은 class 로 만들어볼 예정입니다
"""

def vgg_block(x, conv_num, channel):
    # conv2D layer
    for num in range(conv_num):
        x= Conv2D(channel, kernel_size=(3, 3), activation='relu', padding='same')(x)

    # Max pooling layer
    x = MaxPooling2D(pool_size=(2, 2), strides=2)(x)

    return x

# version01-VGG16
def VGG16():
    inputs = Input(shape=(224, 224, 3))

    vgg_block01 = vgg_block(inputs, 2, 64)
    vgg_block02 = vgg_block(vgg_block01, 2, 128)
    vgg_block03 = vgg_block(vgg_block02, 3, 256)
    vgg_block04 = vgg_block(vgg_block03, 3, 512)
    vgg_block05 = vgg_block(vgg_block04, 3, 512)

    vgg_flatten = Flatten()(vgg_block05)

    vgg_dense01 = Dense(4096)(vgg_flatten)
    vgg_dense02 = Dense(1000)(vgg_dense01)

    model = Model(inputs=inputs, outputs=vgg_dense02)


    return model

# version02-VGG16
def VGG16_02():
    
    x = Input(shape=(224, 224, 3))
    
    def vgg_block(x, conv_num, channel):
        # conv2D layer
        for num in range(conv_num):
            x= Conv2D(channel, kernel_size=(3, 3), activation='relu', padding='same')(x)
        
        # Max pooling layer
        x = MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    
        return x
    
    for num, channel_num in zip([2, 2, 3, 3, 3], [64, 128, 256, 512, 512]):
        x = vgg_block(x, num, channel_num)

    vgg_flatten = Flatten()(vgg_block05)

    vgg_dense01 = Dense(4096)(vgg_flatten)
    vgg_dense02 = Dense(1000)(vgg_dense01)

    model = Model(inputs=inputs, outputs=vgg_dense02)
    
    return model
