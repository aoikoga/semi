# SSH の設定

## 鍵の作成
```
ssh-keygen -k rsa -f ito_key
```

## .ssh/config の設定
```
Host ito
    Hostname ito.cc.kyushu-u.ac.jp
    User  hogehoge
    IdentityFile ~/.ssh/ito_key
    ForwardAgent yes
    AddKeysToAgent yes
```

## ito への接続
```
eval `ssh-agent`
ssh -A -Y ito
```