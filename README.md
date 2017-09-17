# dqn_test

## Prepare Envirounment
activate
```
source /usr/local/git_local/virtualenv/dqn_test/bin/activate
```

install
```
 pip install --upgrade https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0-py3-none-any.whl
 pip install matplotlib
```

source change
dqn_agent.py's 66 rows:
```
before

after
 tf.initialize_all_variables
```

## reference
http://blog.algolab.jp/post/2016/08/01/tf-dqn-simple-1/